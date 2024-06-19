"""Logic for executing zorg queries lives in this module."""

from collections import defaultdict
from functools import partial
import itertools as it
import time
from typing import Iterable, Sequence, Union

from logrus import Logger
from typist import assert_never

from ...domain.models import Note, Query
from ...domain.types import (
    GroupByType,
    KeyFunc,
    NoteType,
    OrderByType,
    SelectType,
)
from ...storage.sql.session import SQLSession
from ..compiler import build_zorg_query


_LOGGER = Logger(__name__)

GroupNoteMap = dict[str, "NoteGroup"]
NoteGroup = Union[list[Note], GroupNoteMap]


def execute(session: SQLSession, query_string: str) -> str:
    """Execute a zorg query and then render it as a .zo file.

    In other words, a Zorg query goes in and a Zorg file comes out.

    Arguments:
    ----------
    session: A zorg SQL session that MUST be instantiated (e.g. using `with
        session`) by the caller.
    query_string: A zorg query that MUST conform to the syntax defined by the
        [[src/zorg/grammar/ZorgQuery.g4]] grammar.

    Return:
    -------
    A string that MUST conform to the syntax defined by the
    [[src/zorg/grammar/ZorgFile.g4]] grammar's "body" parser rule.
    """
    query = build_zorg_query(query_string)
    _LOGGER.debug(
        "Built query from string", query=query, query_string=query_string
    )

    ### (W)HERE
    notes = _get_notes_by_query(session, query)

    ### (G)ROUP BY
    note_group = _group_notes_by(notes, query.group_by)

    ### (O)RDER BY
    ordered_note_group = _order_notes_by(note_group, query.order_by)

    ### (S)ELECT
    result = _select(
        query.select, ordered_note_group, num_of_levels=len(query.group_by)
    )

    return result.strip()


def _get_notes_by_query(session: SQLSession, query: Query) -> list[Note]:
    start_time = time.time()
    notes = session.repo.get_notes_by_query(query.where)
    query_runtime = time.time() - start_time
    _LOGGER.info(
        "Query complete",
        num_of_notes=len(notes),
        seconds=f"{query_runtime:.3f}",
    )
    return notes


def _group_notes_by(
    notes: Iterable[Note], group_by_types: Sequence[GroupByType]
) -> NoteGroup:
    if not group_by_types:
        return list(notes)

    key = group_by_types[0].keyfunc
    rest_group_by_types = group_by_types[1:]
    sorted_notes = sorted(notes, key=key)
    note_group: GroupNoteMap = defaultdict(list)
    for k, group in it.groupby(sorted_notes, key=key):
        note_group[str(k)] = _group_notes_by(group, rest_group_by_types)
    return note_group


def _order_notes_by(
    note_group: NoteGroup, order_bys: Iterable[OrderByType]
) -> NoteGroup:
    keyfunc = _order_by_keyfunc(order_bys)
    if isinstance(note_group, list):
        return sorted(note_group, key=keyfunc)

    assert isinstance(note_group, dict)
    new_note_group = {}
    for k, v in note_group.items():
        new_note_group[k] = _order_notes_by(v, order_bys)
    return new_note_group


def _order_by_keyfunc(order_bys: Iterable[OrderByType]) -> KeyFunc:
    def keyfunc(note: Note) -> str:
        return " ".join(oby.keyfunc(note) for oby in order_bys)

    return keyfunc


def _select(
    select_type: SelectType,
    note_group: NoteGroup,
    *,
    num_of_levels: int,
    level: int = 1,
) -> str:
    result = ""
    if isinstance(note_group, list):
        selector = _select_note
        if select_type is SelectType.AREA:
            selector = partial(_select_tags, "areas")
        elif select_type is SelectType.BLOCK:
            raise NotImplementedError("Selecting blocks is not yet supported.")
        elif select_type is SelectType.CONTEXT:
            selector = partial(_select_tags, "contexts")
        elif select_type is SelectType.FILE:
            selector = _select_file
        elif select_type is SelectType.NOTE:
            selector = _select_note
        elif select_type is SelectType.PERSON:
            selector = partial(_select_tags, "people")
        elif select_type is SelectType.PROJECT:
            selector = partial(_select_tags, "projects")
        else:
            assert_never(select_type)

        result += selector(note_group) + "\n"
    else:
        assert isinstance(note_group, dict)
        for group_name, note_subgroup in note_group.items():
            if group_name:
                header = _get_header(level, num_of_levels=num_of_levels)
                result += f"{header} {group_name}\n"
            result += _select(
                select_type,
                note_subgroup,
                level=level + 1,
                num_of_levels=num_of_levels,
            )
    return result


def _select_note(notes: list[Note]) -> str:
    result = ""
    for note in notes:
        note_type = (
            note.todo_payload.status if note.todo_payload else NoteType.BASIC
        )
        char = note_type.to_prefix_char()
        priority = (
            f" {note.todo_payload.priority}" if note.todo_payload else ""
        )
        result += f"{char}{priority} {note.body.strip()}\n"
    return result


def _select_tags(attr: str, notes: list[Note]) -> str:
    tags: set[str] = set()
    for note in notes:
        for tag in getattr(note, attr):
            tags.add(tag)
    return "\n".join(sorted(tags))


def _select_file(notes: list[Note]) -> str:
    file_paths: set[str] = set()
    for note in notes:
        assert note.file_path is not None
        file_paths.add(str(note.file_path))
    return "\n".join(sorted(file_paths))


def _get_header(level: int, *, num_of_levels: int) -> str:
    newline = "\n" if num_of_levels > 1 else ""
    if level == 1:
        return f"{newline}{'#' * 32}"
    elif level == 2:
        return f"{'=' * 24}"
    elif level == 3:
        return f"{'+' * 16}"
    elif level == 4:
        return f"{'-' * 8}"
    else:
        raise RuntimeError(
            "Zorg supports grouping notes by a MAXIMUM of 4 dimensions at"
            f" once | level={level}"
        )
