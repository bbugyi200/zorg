"""Logic for executing zorg queries lives in this module."""

from collections import defaultdict
from functools import partial
import itertools as it
import time
from typing import Callable, Iterable, Sequence, Union

from logrus import Logger
from typist import assert_never

from ...domain.models import Note, Query
from ...domain.types import (
    GroupByType,
    KeyFunc,
    OrderByType,
    SelectPropertyValues,
    SelectStaticType,
    SelectType,
)
from ...storage.sql.session import SQLSession
from ..compiler import build_zorg_query


_LOGGER = Logger(__name__)

GroupNoteMap = dict[str, "NoteGroup"]
NoteGroup = Union[list[Note], GroupNoteMap]
Selector = Callable[[list[Note]], list[str]]


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
        query.select,
        ordered_note_group,
        alpha_sort=set(query.order_by) == {OrderByType.ALPHA},
        num_of_levels=len(query.group_by),
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
    alpha_sort: bool,
    num_of_levels: int,
    level: int = 1,
) -> str:
    result = ""
    if isinstance(note_group, list):
        selector = _get_selector(select_type, alpha_sort=alpha_sort)
        result += "\n".join(selector(note_group)) + "\n\n"
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
                alpha_sort=alpha_sort,
                num_of_levels=num_of_levels,
            )
    return result


def _get_selector(select_type: SelectType, *, alpha_sort: bool) -> Selector:
    selector = _select_note
    if select_type is SelectStaticType.AREA:
        selector = partial(_select_tags, "areas", alpha_sort=alpha_sort)
    elif select_type is SelectStaticType.CONTEXT:
        selector = partial(_select_tags, "contexts", alpha_sort=alpha_sort)
    elif select_type is SelectStaticType.FILE:
        selector = _select_file
    elif select_type is SelectStaticType.NOTE:
        selector = _select_note
    elif select_type is SelectStaticType.PERSON:
        selector = partial(_select_tags, "people", alpha_sort=alpha_sort)
    elif select_type is SelectStaticType.PROJECT:
        selector = partial(_select_tags, "projects", alpha_sort=alpha_sort)
    elif select_type is SelectStaticType.PROPERTY:
        selector = partial(_select_prop_keys, alpha_sort=alpha_sort)
    elif select_type is SelectStaticType.LINKS:
        selector = partial(_select_links, alpha_sort=alpha_sort)
    elif isinstance(select_type, SelectPropertyValues):
        selector = partial(
            _select_prop_values, select_type.key, alpha_sort=alpha_sort
        )
    else:
        assert_never(select_type)
    return selector


def _select_note(notes: list[Note]) -> list[str]:
    note_strings = []
    for note in notes:
        note_strings.append(note.to_string().rstrip())
    return note_strings


def _select_tags(
    attr: str, notes: list[Note], *, alpha_sort: bool
) -> list[str]:
    tags: list[str] = []
    for note in notes:
        for tag in getattr(note, attr):
            if tag not in tags:
                tags.append(tag)
    return sorted(tags) if alpha_sort else tags


def _select_prop_keys(notes: list[Note], *, alpha_sort: bool) -> list[str]:
    prop_keys: list[str] = []
    for note in notes:
        for prop_key in note.properties.keys():
            if prop_key not in prop_keys:
                prop_keys.append(prop_key)
    return sorted(prop_keys) if alpha_sort else prop_keys


def _select_prop_values(
    prop_key: str, notes: list[Note], *, alpha_sort: bool
) -> list[str]:
    prop_values: list[str] = []
    for note in notes:
        if prop_key in note.properties:
            prop_value = note.properties[prop_key]
            if prop_value not in prop_values:
                prop_values.append(prop_value)
    return sorted(prop_values) if alpha_sort else prop_values


def _select_links(notes: list[Note], *, alpha_sort: bool) -> list[str]:
    links: list[str] = []
    for note in notes:
        for link in note.links:
            if link not in links:
                links.append(link)
    return sorted(links) if alpha_sort else links


def _select_file(notes: list[Note]) -> list[str]:
    file_paths: set[str] = set()
    for note in notes:
        assert note.file_path is not None
        file_paths.add(str(note.file_path))
    return sorted(file_paths)


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
