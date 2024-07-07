"""Contains runners for the 'zorg query' command."""

import os
from pathlib import Path
import random
import string

from zorg.app.config import QueryConfig
from zorg.domain.messages import commands
from zorg.service import messagebus, swog
from zorg.storage.sql.session import SQLSession

from ._runners import runner


@runner
def run_query(cfg: QueryConfig) -> int:
    """Runner for the 'query' command."""
    if cfg.open_in_editor or cfg.store_in_file:
        tmp_zorg_dir = str(cfg.zettel_dir / "query/tmp")
        tmp_zoq_path = Path(_create_temp_query_page(tmp_zorg_dir))
        tmp_zoq_path.write_text(f"# {cfg.query}\n")
        sql_session = SQLSession(cfg.zettel_dir, cfg.database_url)
        if cfg.open_in_editor:
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
                sql_session,
            )
        elif cfg.store_in_file:
            with sql_session as session:
                swog.refresh_zoq_file(session, tmp_zoq_path)
            print(str(tmp_zoq_path))
        return 0

    with SQLSession(
        cfg.zettel_dir, cfg.database_url, verbose=cfg.verbose
    ) as session:
        query_results = swog.execute(session, cfg.query)
        if query_results:
            print(query_results)
    return 0


def _create_temp_query_page(directory: str) -> str:
    # Ensure the directory exists
    os.makedirs(directory, exist_ok=True)

    # Generate a random string for the filename
    random_string = "".join(
        random.choices(string.ascii_uppercase + string.digits, k=3)
    )

    # Construct the full path for the new temporary file
    file_path = os.path.join(directory, f"tmp_{random_string}.zoq")

    # Create a new empty file at the specified path
    with open(file_path, "w") as temp_file:
        # You can write data to the file if necessary
        temp_file.write("")  # Just creates an empty file for now

    # Return the path of the newly created file
    return file_path
