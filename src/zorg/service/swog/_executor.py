"""Logic for executing zorg queries lives in this module."""

from collections import defaultdict
import itertools as it
import time
from typing import Iterable, Sequence, Union

from logrus import Logger

from ...domain.models import Note
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


# TODO(bugyi): Reduce package to single swog.py file
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
    start_time = time.time()
    filtered_notes = session.repo.get_by_query(query.where)
    query_runtime = time.time() - start_time
    _LOGGER.info(
        "Query complete",
        num_of_notes=len(filtered_notes),
        seconds=f"{query_runtime:.3f}",
    )

    ### (G)ROUP BY
    note_group = _group_notes_by(filtered_notes, query.group_by)

    ### (O)RDER BY
    ordered_note_group = _order_notes_by(note_group, query.order_by)

    ### (S)ELECT
    result = _select(query.select, ordered_note_group)

    return result.strip()


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
    select_type: SelectType, note_group: NoteGroup, *, level: int = 1
) -> str:
    result = ""
    if select_type is SelectType.NOTE:
        if isinstance(note_group, list):
            result += _select_note(note_group) + "\n"
        else:
            assert isinstance(note_group, dict)
            for group_name, note_subgroup in note_group.items():
                if group_name:
                    result += f"{_get_header(level)} {group_name}\n"
                result += _select(select_type, note_subgroup, level=level + 1)
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
            f" {note.todo_payload.priority}" if note.todo_payload else ""
        )
        result += f"{char}{priority} {note.body.strip()}\n"
    return result


def _get_header(level: int) -> str:
    if level == 1:
        return "\n#########"
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
