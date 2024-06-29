"""Contains runners for the 'zorg note' command."""

from logrus import Logger

from ...service.compiler import build_zorg_query, build_zorg_mutate
from ...storage.file import FileManager
from ...storage.sql.session import SQLSession
from ..config import NoteMoveConfig, NoteMutateConfig
from ._runners import runner


_LOGGER = Logger(__name__)


@runner
def run_note_move(cfg: NoteMoveConfig) -> int:
    """Runner for the 'note move' command."""
    with SQLSession(
        cfg.zettel_dir, cfg.database_url, verbose=cfg.verbose
    ) as session:
        return _move_note(cfg, session)


@runner
def run_note_mutate(cfg: NoteMutateConfig) -> int:
    """Runner for the 'note move' command."""
    with SQLSession(
        cfg.zettel_dir, cfg.database_url, verbose=cfg.verbose
    ) as session:
        return _mutate_notes(cfg, session)


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


def _mutate_notes(cfg: NoteMutateConfig, session: SQLSession) -> int:
    where_query = build_zorg_query(cfg.where_query).where
    notes = session.repo.get_notes_by_query(where_query)
    mutate = build_zorg_mutate(cfg.mutate)
    for note in notes:
        print(mutate.mutate_note(note).to_string())
    return 0
