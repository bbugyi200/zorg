"""Contains runners for the 'zorg note' command."""

from zorg.app.config import NoteMoveConfig
from zorg.service.note_utils import move_note

from ._runners import runner


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
