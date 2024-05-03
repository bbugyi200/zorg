"""Logic for executing zorg queries lives in this module."""

from ..service.compiler import build_zorg_query
from ..storage.sql.session import SQLSession


def execute(session: SQLSession, query_string: str) -> str:
    """Execute a zorg query and then render it as a .zo file.

    In other words, a Zorg query comes in and a Zorg file comes out.
    """
    zorg_query = build_zorg_query(query_string)
    with session:
        for zorg_note in session.repo.get_by_query(zorg_query.where).unwrap():
            print(zorg_note)
