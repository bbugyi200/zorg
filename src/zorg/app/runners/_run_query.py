"""Contains runners for the 'zorg query' command."""

from ...service import swog
from ...storage.sql.session import SQLSession
from ..config import QueryConfig
from ._runners import runner


@runner
def run_query(cfg: QueryConfig) -> int:
    """Runner for the 'query' command."""
    with SQLSession(
        cfg.zettel_dir, cfg.database_url, verbose=cfg.verbose
    ) as session:
        print(swog.execute(session, cfg.query))
    return 0
