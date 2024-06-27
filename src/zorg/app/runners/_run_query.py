"""Contains runners for the 'zorg query' command."""

import os
from pathlib import Path
import tempfile

from ...domain.messages import commands
from ...service import messagebus, swog
from ...storage.sql.session import SQLSession
from ..config import QueryConfig
from ._runners import runner


@runner
def run_query(cfg: QueryConfig) -> int:
    """Runner for the 'query' command."""
    if cfg.open_in_editor:
        tmp_zorg_dir = "/tmp/zorg"
        os.makedirs(tmp_zorg_dir, exist_ok=True)
        with tempfile.NamedTemporaryFile(
            suffix=".zoq", dir=tmp_zorg_dir, delete=False
        ) as tmp_zoq:
            tmp_zoq_path = Path(tmp_zoq.name)
            tmp_zoq_path.write_text(f"# {cfg.query}\n")
            messagebus.handle(
                [
                    commands.EditCommand(
                        keep_alive_file=cfg.keep_alive_file,
                        paths=[tmp_zoq_path],
                        verbose=cfg.verbose,
                        vim_commands=cfg.vim_commands,
                        zettel_dir=cfg.zettel_dir,
                    ),
                ],
                SQLSession(cfg.zettel_dir, cfg.database_url),
            )
            return 0

    with SQLSession(
        cfg.zettel_dir, cfg.database_url, verbose=cfg.verbose
    ) as session:
        query_results = swog.execute(session, cfg.query)
        if query_results:
            print(query_results)
    return 0
