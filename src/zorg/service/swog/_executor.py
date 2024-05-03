"""Logic for executing zorg queries lives in this module."""

from typist import assert_never

from ...domain.types import NoteType, SelectType
from ...storage.sql.session import SQLSession
from ..compiler import build_zorg_query


def _to_prefix_char(note_type: NoteType) -> str:
    if note_type is NoteType.BASIC:
        return "-"
    elif note_type is NoteType.OPEN_TODO:
        return "o"
    elif note_type is NoteType.CLOSED_TODO:
        return "x"
    elif note_type is NoteType.CANCELED_TODO:
        return "~"
    elif note_type is NoteType.BLOCKED_TODO:
        return "<"
    elif note_type is NoteType.PARENT_TODO:
        return ">"
    else:
        assert_never(note_type)


def execute(session: SQLSession, query_string: str) -> str:
    """Execute a zorg query and then render it as the  .zo file.

    In other words, a Zorg query comes in and a Zorg file comes out.

    Arguments:
    ----------
    session: A zorg SQL session that MUST be instantiated (e.g. using `with
        session`) by the caller.
    query_string: A zorg query that MUST conform to the syntax defined by the
        [[src/zorg/grammar/zorg_query/ZorgQuery.g4]] grammar.

    Return:
    -------
    A string that MUST conform to the syntax defined by the
    [[src/zorg/grammar/zorg_file/ZorgFile.g4]] grammar's "body" parser rule.
    """
    query = build_zorg_query(query_string)
    result = ""
    with session:
        # (W)HERE
        filtered_notes = session.repo.get_by_query(query.where)

        # (S)ELECT
        if query.select is SelectType.NOTES:
            for note in filtered_notes:
                char = _to_prefix_char(
                    note.todo_payload.status
                    if note.todo_payload
                    else NoteType.BASIC
                )
                priority = (
                    f"{note.todo_payload.priority} "
                    if note.todo_payload
                    else ""
                )
                result += f"{char}{priority}{note.body}\n"

    return result
