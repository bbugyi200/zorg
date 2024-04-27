"""Contains runners for the 'zorg query' command."""

from ..config import QueryConfig
from ._runners import runner


@runner
def run_query(cfg: QueryConfig) -> int:
    """Runner for the 'query' command."""
    del cfg
    return 0
