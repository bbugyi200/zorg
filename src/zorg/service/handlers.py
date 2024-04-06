"""Zorg's event and command handlers live here."""

from pathlib import Path
from typing import Iterable, Iterator

from logrus import Logger
import vimala

from ..domain import commands
from ..storage.sql.session import ZorgSQLSession
from .common import prepend_zdir


logger = Logger(__name__)


def start_vim_loop(cmd: commands.EditCommand, session: ZorgSQLSession) -> None:
    del session
    def run_vim(paths: Iterable[Path]) -> None:
        vimala.vim(
            *paths,
            commands=_process_vim_commands(cmd.zettel_dir, cmd.vim_commands),
        ).unwrap()

    run_vim(cmd.paths)

    logger.debug(
        "Vim loop will run as long as the keep alive file exists.",
        keep_alive_file=cmd.keep_alive_file,
    )
    last_paths = cmd.paths
    while cmd.keep_alive_file.exists():
        if cmd.keep_alive_file.stat().st_size == 0:
            paths = last_paths
        else:
            new_paths = prepend_zdir(
                cmd.zettel_dir,
                [
                    Path(p.strip())
                    for p in cmd.keep_alive_file.read_text().split()
                ],
            )
            logger.debug(
                "Editing files specified in the keep alive file.",
                keep_alive_file=cmd.keep_alive_file,
                old_paths=last_paths,
                new_paths=new_paths,
            )
            paths = last_paths = new_paths

        cmd.keep_alive_file.unlink()
        run_vim(paths)


def _process_vim_commands(
    zettel_dir: Path, vim_commands: Iterable[str]
) -> Iterator[str]:
    for vim_cmd in vim_commands:
        if "{zdir}" in vim_cmd:
            yield vim_cmd.format(zdir=zettel_dir)
        else:
            yield vim_cmd
