"""Logic for executing zorg queries lives in this module."""

from ..service.compiler import build_zorg_query
from ..storage.sql.session import SQLSession


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
    zorg_query = build_zorg_query(query_string)
    with session:
        for zorg_note in session.repo.get_by_query(zorg_query.where).unwrap():
            print(zorg_note)
