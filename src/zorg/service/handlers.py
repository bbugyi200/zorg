"""Zorg's event and command handlers live here."""

from pathlib import Path
from typing import Iterable, Iterator

from logrus import Logger
import vimala

from ..domain import commands, events
from ..storage.sql.session import SQLSession
from .common import prepend_zdir


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


def _process_vim_commands(
    zettel_dir: Path, vim_commands: Iterable[str]
) -> Iterator[str]:
    for vim_cmd in vim_commands:
        if "{zdir}" in vim_cmd:
            yield vim_cmd.format(zdir=zettel_dir)
        else:
            yield vim_cmd
