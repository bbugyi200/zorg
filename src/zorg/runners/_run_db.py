"""Contains runners for the 'zorg db' command."""

from ..config import DbInfoConfig
from ._runners import runner


@runner
def run_db_info(cfg: DbInfoConfig) -> int:
    """Runner for the 'db info' command."""
    del cfg
    return 0
