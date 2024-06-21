"""Contains runners for the 'zorg note' command."""

from logrus import Logger

from ...storage.sql.session import SQLSession
from ..config import NoteMoveConfig
from ._runners import runner


_LOGGER = Logger(__name__)


@runner
def run_note_move(cfg: NoteMoveConfig) -> int:
    """Runner for the 'note move' command."""
    with SQLSession(
        cfg.zettel_dir, cfg.database_url, verbose=cfg.verbose
    ) as session:
        note = session.repo.get_note_by_zid(cfg.zid)

    if note is None:
        _LOGGER.error("No Zorg note with the given ZID", zid=cfg.zid)
        return 1

    print(f"{str(note.file_path)}::{note.line_no}")
    return 0
