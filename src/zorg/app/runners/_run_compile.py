"""Contains runners for the 'zorg compile' command."""

from dataclasses import asdict
from pprint import pprint
from typing import Any

from ...domain.models import File
from ...service.compiler import walk_zorg_file
from ..config import CompileConfig
from ._runners import runner


@runner
def run_compile(cfg: CompileConfig) -> int:
    """Runner for the 'compile' command."""
    zorg_file = walk_zorg_file(cfg.zettel_dir, cfg.zo_path, verbose=True)
    zorg_file_dict = _convert_zorg_file_to_dict(zorg_file)
    pprint(zorg_file_dict)
    return 0


def _convert_zorg_file_to_dict(zorg_file: File) -> dict[str, Any]:
    zorg_file_dict = asdict(zorg_file)
    for key in ["events", "has_errors", "path"]:
        del zorg_file_dict[key]

    for note_dict in zorg_file_dict["notes"]:
        for key in ["file_path", "line_no"]:
            del note_dict[key]
    return zorg_file_dict
