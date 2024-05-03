"""Logic for executing zorg queries lives in this module."""

from ...domain.types import NoteType
from ...storage.sql.session import SQLSession
from ..compiler import build_zorg_query


# Mapping from a note to its corresponding prefix symbol
_NOTE_SYMBOL_MAP: dict[NoteType, str] = {NoteType}


def _to_prefix_char(note_type: NoteType) -> str:
    pass


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
    with session:
        # (W)HERE
        filtered_todos = session.repo.get_by_query(query.where)

        # (S)ELECT
