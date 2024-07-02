"""Contains runners for the 'zorg file' command."""

from ..config import FileRenameConfig
from ._runners import runner


@runner
def run_file_rename(cfg: FileRenameConfig) -> int:
    del cfg
    return 0
