"""Contains runners for the 'zorg compile' command."""

from dataclasses import asdict
from pprint import pprint
from typing import Any, Final

from zorg.app.config import CompileConfig
from zorg.domain.models import Page
from zorg.service.compiler import walk_zorg_page

from ._runners import runner

_BAD_NOTE_DICT_KEYS: Final[tuple[str, ...]] = ("file_path", "line_no")


@runner
def run_compile(cfg: CompileConfig) -> int:
    """Runner for the 'compile' command."""
    page = walk_zorg_page(cfg.zettel_dir, cfg.zo_path, verbose=True)
    zorg_page_dict = _convert_zorg_page_to_dict(page)
    pprint(zorg_page_dict)
    return 0


def _convert_zorg_page_to_dict(page: Page) -> dict[str, Any]:
    zorg_page_dict = asdict(page)
    for key in ["events", "has_errors", "path"]:
        del zorg_page_dict[key]

    h1_dicts = list(zorg_page_dict["h1s"])
    if zorg_page_dict["h0"]:
        h1_dicts = [zorg_page_dict["h0"]] + h1_dicts
    block_dicts = []
    for h1_dict in h1_dicts:
        block_dicts.extend(h1_dict["blocks"])
        for h2_dict in h1_dict["h2s"]:
            block_dicts.extend(h2_dict["blocks"])
            for h3_dict in h2_dict["h3s"]:
                block_dicts.extend(h3_dict["blocks"])
                for h4_dict in h3_dict["h4s"]:
                    block_dicts.extend(h4_dict["blocks"])
    for block_dict in block_dicts:
        for note_dict in block_dict["notes"]:
            for bad_key in _BAD_NOTE_DICT_KEYS:
                if bad_key in note_dict:
                    del note_dict[bad_key]
    return zorg_page_dict
