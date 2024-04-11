"""Zorg's event and command handlers live here."""

from pathlib import Path
import sys
from typing import Iterable, Iterator

from logrus import Logger
from tqdm import tqdm
import vimala

from ..domain.messages import commands, events
from ..storage.sql.session import SQLSession
from .common import prepend_zdir
from .compiler import walk_zorg_file
from .zid_manager import ZIDManager


logger = Logger(__name__)


def edit_files(cmd: commands.EditCommand, session: SQLSession) -> None:
    """Command handler for the EditCommand."""
    vimala.vim(
        *cmd.paths,
        commands=_process_vim_commands(cmd.zettel_dir, cmd.vim_commands),
    ).unwrap()
    session.add_message(events.EditorClosedEvent(edit_cmd=cmd))


def check_keep_alive_file(
    event: events.EditorClosedEvent, session: SQLSession
) -> None:
    """Check if the 'keep alive' file exists and, if so, reopens the editor."""
    if not event.edit_cmd.keep_alive_file.exists():
        logger.debug(
            "No keep alive file found.",
            keep_alive_file=event.edit_cmd.keep_alive_file,
        )
        return

    if event.edit_cmd.keep_alive_file.stat().st_size == 0:
        logger.debug(
            "Empty keep alive file found.",
            keep_alive_file=event.edit_cmd.keep_alive_file,
        )
        paths = event.edit_cmd.paths
    else:
        new_paths = prepend_zdir(
            event.edit_cmd.zettel_dir,
            [
                Path(p.strip())
                for p in event.edit_cmd.keep_alive_file.read_text().split()
            ],
        )
        logger.debug(
            "Editing files specified in the keep alive file.",
            keep_alive_file=event.edit_cmd.keep_alive_file,
            old_paths=event.edit_cmd.paths,
            new_paths=new_paths,
        )
        paths = new_paths

    event.edit_cmd.keep_alive_file.unlink()
    session.add_message(
        commands.EditCommand(
            zettel_dir=event.edit_cmd.zettel_dir,
            paths=paths,
            keep_alive_file=event.edit_cmd.keep_alive_file,
            vim_commands=event.edit_cmd.vim_commands,
        )
    )


def create_database(
    cmd: commands.CreateDBCommand, session: SQLSession
) -> None:
    """Create a new zorg DB from scratch."""
    zorg_files = []
    total_num_notes = 0
    total_num_todos = 0
    for zo_path in tqdm(
        sorted(cmd.zettel_dir.rglob("*.zo"), key=lambda p: p.name),
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
            total_num_notes=total_num_notes,
            total_num_todos=total_num_todos,
        )
        session.repo.add(zorg_file)
        zorg_files.append(zorg_file)
    logger.info(
        "Finished reading zettel org directory",
        num_files=len(zorg_files),
        num_notes=total_num_notes,
        num_todos=total_num_todos,
    )
    session.commit()
    session.add_message(events.DBCreatedEvent(cmd.zettel_dir))


def add_zorg_ids_to_notes_in_file(
    event: events.NewZorgNotesEvent, session: SQLSession
) -> None:
    """Adds IDs to new zorg notes."""
    del session

    zfile_lines = event.zorg_file_path.read_text().split("\n")
    for note in event.new_notes:
        body_line_count = len(note.body.split("\n"))


def increment_zorg_id_counters(
    event: events.DBCreatedEvent, session: SQLSession
) -> None:
    """Increment the date-specific zorg ID counters.

    These are stored in a directory in your zettel dir and are used when
    generating new IDs (they are the XX in the YYMMDD#XX ID format).
    """
    del session
    id_gen = ZIDManager(event.zettel_dir)
    id_gen.write_to_disk()


def _process_vim_commands(
    zettel_dir: Path, vim_commands: Iterable[str]
) -> Iterator[str]:
    for vim_cmd in vim_commands:
        if "{zdir}" in vim_cmd:
            yield vim_cmd.format(zdir=zettel_dir)
        else:
            yield vim_cmd
