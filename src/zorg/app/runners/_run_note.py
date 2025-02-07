"""Contains runners for the 'zorg note' command."""

from typing import Final

from logrus import Logger

from zorg.app.config import NoteMoveConfig, NotePromoteConfig
from zorg.service.note_utils import (
    convert_note_to_page,
    get_note_by_zid,
    move_note,
)
from zorg.shared import common as c

from ._runners import runner

_LOGGER: Final = Logger(__name__)


@runner
def run_note_move(cfg: NoteMoveConfig) -> int:
    """Runner for the 'note move' command."""
    return move_note(
        cfg.zettel_dir,
        cfg.database_url,
        cfg.template_pattern_map,
        zid=cfg.zid,
        new_page=cfg.new_page,
        note_type=cfg.note_type,
        verbose=cfg.verbose,
    )


@runner
def run_note_promote(cfg: NotePromoteConfig) -> int:
    """Runner for the 'note promote' command."""
    note = get_note_by_zid(cfg.zettel_dir, cfg.database_url, cfg.zid)
    if note is None:
        _LOGGER.error("No note with the given ZID was found.", zid=cfg.zid)
        return 1

    new_page_name = cfg.new_page_name or note.properties.get("ID")
    if new_page_name is None:
        _LOGGER.error(
            "Note does not defined the ID property and NO new page name was"
            " provided on the command-line.",
            note_properties=note.properties,
        )
        return 1

    parent_page_name = cfg.parent_page_name or c.strip_zdir(
        cfg.zettel_dir, note.file_path
    )

    page = convert_note_to_page(
        cfg.zettel_dir, note, new_page_name, parent_page_name
    )
    _LOGGER.info("Converted note to page", zid=note.zid, page=str(page.path))
    return 0
