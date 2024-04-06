"""Zorg's event and command handlers live here."""

from pathlib import Path
from typing import Iterable, Iterator

from logrus import Logger
import vimala

from ..domain import commands
from ..storage.sql.session import ZorgSQLSession
from .common import prepend_zdir


logger = Logger(__name__)


def edit_zorg_files(
    cmd: commands.EditCommand, session: ZorgSQLSession
) -> None:
    """Command handler for the EditCommand."""
    session.add_message(
        commands.CheckKeepAliveFileCommand(
            zettel_dir=cmd.zettel_dir,
            paths=cmd.paths,
            keep_alive_file=cmd.keep_alive_file,
            vim_commands=cmd.vim_commands,
        )
    )
    vimala.vim(
        *cmd.paths,
        commands=_process_vim_commands(cmd.zettel_dir, cmd.vim_commands),
    ).unwrap()


def check_keep_alive_file(
    cmd: commands.CheckKeepAliveFileCommand, session: ZorgSQLSession
) -> None:
    """Command handler for the CheckKeepAliveFileCommand."""
    if not cmd.keep_alive_file.exists():
        logger.debug(
            "No keep alive file found.", keep_alive_file=cmd.keep_alive_file
        )
        return

    if cmd.keep_alive_file.stat().st_size == 0:
        logger.debug(
            "Empty keep alive file found.", keep_alive_file=cmd.keep_alive_file
        )
        paths = cmd.paths
    else:
        new_paths = prepend_zdir(
            cmd.zettel_dir,
            [Path(p.strip()) for p in cmd.keep_alive_file.read_text().split()],
        )
        logger.debug(
            "Editing files specified in the keep alive file.",
            keep_alive_file=cmd.keep_alive_file,
            old_paths=cmd.paths,
            new_paths=new_paths,
        )
        paths = new_paths

    cmd.keep_alive_file.unlink()
    session.add_message(
        commands.EditCommand(
            zettel_dir=cmd.zettel_dir,
            paths=paths,
            keep_alive_file=cmd.keep_alive_file,
            vim_commands=cmd.vim_commands,
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
