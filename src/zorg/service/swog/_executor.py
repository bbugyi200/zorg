"""Logic for executing zorg queries lives in this module."""

from collections import defaultdict
import itertools as it
import time
from typing import Iterable, Sequence, Union

from logrus import Logger

from ...domain.models import Note
from ...domain.types import GroupByType, NoteType, SelectType
from ...storage.sql.session import SQLSession
from ..compiler import build_zorg_query


_LOGGER = Logger(__name__)


GroupNoteMap = dict[str, "GroupedNotes"]
GroupedNotes = Union[list[Note], GroupNoteMap]


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

    ### (W)HERE
    start_time = time.time()
    filtered_notes = session.repo.get_by_query(query.where)
    query_runtime = time.time() - start_time
    _LOGGER.debug(
        "Query complete",
        num_of_notes=len(filtered_notes),
        seconds=f"{query_runtime:.3f}",
        query=query,
    )

    ### (G)ROUP BY
    if query.group_by is None:
        grouped_notes = filtered_notes
    else:
        grouped_notes = _nested_note_group(filtered_notes, query.group_by)

    ### (O)RDER BY

    ### (S)ELECT
    result = _select(query.select, grouped_notes)

    return result


def _select(
    select_type: SelectType, grouped_notes: GroupedNotes, *, level: int = 1
) -> str:
    result = ""
    if select_type is SelectType.NOTE:
        if isinstance(grouped_notes, list):
            result += _select_note(grouped_notes)
        else:
            assert isinstance(grouped_notes, dict)
            for group_name, grouped_notes in grouped_notes.items():
                if group_name:
                    result += f"\n{_get_header(level)} {group_name}\n"
                result += _select(select_type, grouped_notes, level=level + 1)
    else:
        raise NotImplementedError(
            f"SELECT type is not implemented yet: {select_type}"
        )
    return result


def _select_note(filtered_notes: list[Note]) -> str:
    result = ""
    for note in filtered_notes:
        note_type = (
            note.todo_payload.status if note.todo_payload else NoteType.BASIC
        )
        char = note_type.to_prefix_char()
        priority = (
            f" [#{note.todo_payload.priority}]" if note.todo_payload else ""
        )
        result += f"{char}{priority} {note.body.strip()}\n"
    return result


def _get_header(level: int) -> str:
    if level == 1:
        return "#########"
    elif level == 2:
        return "======="
    elif level == 3:
        return "*****"
    elif level == 4:
        return "---"
    else:
        raise RuntimeError(
            "Zorg supports grouping notes by a MAXIMUM of 4 dimensions at"
            f" once | level={level}"
        )


def _nested_note_group(
    notes: Iterable[Note], group_by_types: Sequence[GroupByType]
) -> GroupedNotes:
    if not group_by_types:
        return list(notes)

    key = group_by_types[0].keyfunc
    rest_group_by_types = group_by_types[1:]
    sorted_notes = sorted(notes, key=key)
    grouped_notes: GroupNoteMap = defaultdict(list)
    for k, group in it.groupby(sorted_notes, key=key):
        if isinstance(k, list):
            k = " ".join(k)
        grouped_notes[k] = _nested_note_group(group, rest_group_by_types)
    return grouped_notes
