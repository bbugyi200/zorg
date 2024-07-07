"""Contains runners for the 'zorg db' command."""

from zorg.app.config import DbCreateConfig, DbReindexConfig
from zorg.domain.messages import commands
from zorg.service import messagebus

from ._runners import runner


@runner
def run_db_create(cfg: DbCreateConfig) -> int:
    """Runner for the 'db create' command."""
    messagebus.handle(
        cfg.zettel_dir,
        cfg.database_url,
        [
            commands.CreateDBCommand(
                cfg.zettel_dir,
                update_error_file_whitelist=cfg.update_error_file_whitelist,
            )
        ],
        verbose=cfg.verbose,
    )
    return 0


@runner
def run_db_reindex(cfg: DbReindexConfig) -> int:
    """Runner for the 'db reindex' command."""
    messagebus.handle(
        cfg.zettel_dir,
        cfg.database_url,
        [
            commands.ReindexDBCommand(
                zettel_dir=cfg.zettel_dir,
                paths=cfg.paths,
                verbose=bool(cfg.verbose),
            )
        ],
        verbose=cfg.verbose,
    )
    return 0
