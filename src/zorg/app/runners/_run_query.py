"""Contains runners for the 'zorg query' command."""

from ...service.query_executor import execute
from ...storage.sql.session import SQLSession
from ..config import QueryConfig
from ._runners import runner


@runner
def run_query(cfg: QueryConfig) -> int:
    """Runner for the 'query' command."""
    session = SQLSession(cfg.zettel_dir, cfg.database_url)
    print(execute(session, cfg.query))
    return 0
