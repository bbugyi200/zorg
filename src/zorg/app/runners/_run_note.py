"""Contains runners for the 'zorg note' command."""

from logrus import Logger

from ...storage.sql.session import SQLSession
from ...storage.file import FileManager
from ..config import NoteMoveConfig
from ._runners import runner


_LOGGER = Logger(__name__)


@runner
def run_note_move(cfg: NoteMoveConfig) -> int:
    """Runner for the 'note move' command."""
    with SQLSession(
        cfg.zettel_dir, cfg.database_url, verbose=cfg.verbose
    ) as session:
        return _move_note(cfg, session)


def _move_note(cfg: NoteMoveConfig, session: SQLSession) -> int:
    note = session.repo.get_note_by_zid(cfg.zid)

    if note is None:
        _LOGGER.error("No Zorg note with the given ZID", zid=cfg.zid)
        return 1

    _LOGGER.debug(
        f"Note with ZID={cfg.zid} found |"
        f" {str(note.file_path)}::{note.line_no}"
    )

    file_man = FileManager(cfg.zettel_dir, session)
    if error := file_man.add_note(note, cfg.new_page):
        _LOGGER.error("Failed to add note to page", error=f"'{error.upper()}'")
        return 1
    file_man.delete_note(note)
    return 0
