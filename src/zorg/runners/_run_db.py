"""Contains runners for the 'zorg db' command."""

import sys

from logrus import Logger
from tqdm import tqdm

from ..compiler import walk_zorg_file
from ..config import DbCreateConfig
from ._runners import runner


logger = Logger(__name__)


@runner
def run_db_create(cfg: DbCreateConfig) -> int:
    """Runner for the 'db create' command."""
    zorg_files = []
    total_num_notes = 0
    total_num_todos = 0
    for zo_path in tqdm(
        sorted(cfg.zettel_dir.rglob("*.zo"), key=lambda p: p.name),
        desc="Reading notes from zorg files",
        file=sys.stdout,
    ):
        logger.info("Starting to walk zorg file", zorg_file=zo_path.name)
        zorg_file = walk_zorg_file(zo_path)
        num_notes = len(zorg_file.notes)
        num_todos = len(
            [note for note in zorg_file.notes if note.todo_payload]
        )
        total_num_notes += num_notes
        total_num_todos += num_todos
        logger.info(
            "Finished walking zorg file",
            zorg_file=zo_path.name,
            num_notes=num_notes,
            num_todos=num_todos,
        )
        zorg_files.append(zorg_file)
    logger.info(
        "Finished reading zettel org directory",
        num_files=len(zorg_files),
        num_notes=total_num_notes,
        num_todos=total_num_todos,
    )
    return 0
