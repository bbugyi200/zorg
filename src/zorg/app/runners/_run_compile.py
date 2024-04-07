"""Contains runners for the 'zorg compile' command."""

from dataclasses import asdict
from pprint import pprint
from typing import Any

from ...domain.models import ZorgFile
from ...service.compiler import walk_zorg_file
from ..config import CompileConfig
from ._runners import runner


@runner
def run_compile(cfg: CompileConfig) -> int:
    """Runner for the 'compile' command."""
    zorg_file = walk_zorg_file(cfg.zo_path)
    zorg_file_dict = _convert_zorg_file_to_dict(zorg_file)
    pprint(zorg_file_dict)
    return 0


def _convert_zorg_file_to_dict(zorg_file: ZorgFile) -> dict[str, Any]:
    zorg_file_dict = asdict(zorg_file)
    for key in ["ident", "messages", "path"]:
        del zorg_file_dict[key]
    return zorg_file_dict
