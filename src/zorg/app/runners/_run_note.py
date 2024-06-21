"""Contains runners for the 'zorg note' command."""

from ..config import NoteMoveConfig
from ._runners import runner


@runner
def run_note_move(cfg: NoteMoveConfig) -> int:
    """Runner for the 'note move' command."""
    del cfg
    return 0
