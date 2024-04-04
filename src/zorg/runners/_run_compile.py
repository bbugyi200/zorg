"""Contains runners for the 'zorg compile' command."""

from dataclasses import asdict
from pprint import pprint

from ..compiler import walk_zorg_file
from ..config import CompileConfig
from ._runners import runner


@runner
def run_compile(cfg: CompileConfig) -> int:
    """Runner for the 'compile' command."""
    zorg_file = walk_zorg_file(cfg.zo_path)
    zorg_file_dict = asdict(zorg_file)
    del zorg_file_dict["path"]
    pprint(zorg_file_dict)
    return 0
