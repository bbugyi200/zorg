"""Contains runners for the 'zorg query' command."""

from ...service.compiler import compile_zorg_query
from ...storage.sql.session import SQLSession
from ..config import QueryConfig
from ._runners import runner


@runner
def run_query(cfg: QueryConfig) -> int:
    """Runner for the 'query' command."""
    session = SQLSession(cfg.zettel_dir, cfg.database_url)
    zorg_query = compile_zorg_query(cfg.query)
    if cfg.verbose:
        print(zorg_query)

    with session:
        for zorg_note in session.repo.get_by_query(zorg_query.where).unwrap():
            print(zorg_note)
    return 0
