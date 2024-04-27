"""Contains runners for the 'zorg query' command."""

from ...service.compiler import compile_zorg_query
from ..config import QueryConfig
from ._runners import runner


@runner
def run_query(cfg: QueryConfig) -> int:
    """Runner for the 'query' command."""
    print(compile_zorg_query(cfg.query))
    return 0
