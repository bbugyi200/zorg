"""Contains runners for the 'zorg db' command."""

from ...domain.messages import commands
from ...service import messagebus
from ...storage.sql.session import SQLSession
from ..config import DbCreateConfig, DbReindexConfig
from ._runners import runner


@runner
def run_db_create(cfg: DbCreateConfig) -> int:
    """Runner for the 'db create' command."""
    session = SQLSession(
        cfg.zettel_dir, cfg.database_url, should_delete_existing_db=True
    )
    messagebus.handle([commands.CreateDBCommand(cfg.zettel_dir)], session)
    return 0


@runner
def run_db_reindex(cfg: DbReindexConfig) -> int:
    """Runner for the 'db reindex' command."""
    session = SQLSession(cfg.zettel_dir, cfg.database_url)
    messagebus.handle(
        [
            commands.ReindexDBCommand(
                zettel_dir=cfg.zettel_dir,
                paths=cfg.paths,
                verbose=bool(cfg.verbose),
            )
        ],
        session,
    )
    return 0
