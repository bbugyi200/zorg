"""Contains runners for the 'zorg compile' command."""

from dataclasses import asdict
from pprint import pprint
from typing import Any

from zorg.app.config import CompileConfig
from zorg.domain.models import Page
from zorg.service.compiler import walk_zorg_page

from ._runners import runner


@runner
def run_compile(cfg: CompileConfig) -> int:
    """Runner for the 'compile' command."""
    zorg_page = walk_zorg_page(cfg.zettel_dir, cfg.zo_path, verbose=True)
    zorg_page_dict = _convert_zorg_page_to_dict(zorg_page)
    pprint(zorg_page_dict)
    return 0


def _convert_zorg_page_to_dict(zorg_page: Page) -> dict[str, Any]:
    zorg_page_dict = asdict(zorg_page)
    for key in ["events", "has_errors", "path"]:
        del zorg_page_dict[key]

    for note_dict in zorg_page_dict["notes"]:
        for key in ["file_path", "line_no"]:
            del note_dict[key]
    return zorg_page_dict
