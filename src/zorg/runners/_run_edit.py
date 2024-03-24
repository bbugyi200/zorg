"""Contains runners for the 'zorg edit' command."""

from pathlib import Path
from typing import Iterable, Iterator

from logrus import Logger
import vimala

from ..config import EditConfig
from ..file_groups import expand_file_group_paths
from ._common import prepend_zdir, run_template_init
from ._registry import runner


logger = Logger(__name__)


@runner
def run_edit(cfg: EditConfig) -> int:
    """Runner for the 'edit' command."""
    zo_paths = expand_file_group_paths(
        cfg.zo_paths, file_group_map=cfg.file_group_map
    )
    zo_paths = prepend_zdir(cfg.zettel_dir, zo_paths)
    for zo_path in zo_paths:
        run_template_init(cfg.zettel_dir, cfg.template_pattern_map, zo_path)

    _start_vim_loop(zo_paths, cfg=cfg)
    return 0


def _start_vim_loop(zo_paths: Iterable[Path], cfg: EditConfig) -> None:
    def run_vim(paths: Iterable[Path]) -> None:
        vimala.vim(
            *paths,
            commands=_process_vim_commands(cfg.zettel_dir, cfg.vim_commands),
        ).unwrap()

    run_vim(zo_paths)

    logger.debug(
        "Vim loop will run as long as the keep alive file exists.",
        keep_alive_file=cfg.keep_alive_file,
    )
    last_paths = zo_paths
    while cfg.keep_alive_file.exists():
        if cfg.keep_alive_file.stat().st_size == 0:
            paths = last_paths
        else:
            new_paths = prepend_zdir(
                cfg.zettel_dir,
                [
                    Path(p.strip())
                    for p in cfg.keep_alive_file.read_text().split()
                ],
            )
            logger.debug(
                "Editing files specified in the keep alive file.",
                keep_alive_file=cfg.keep_alive_file,
                old_paths=last_paths,
                new_paths=new_paths,
            )
            paths = last_paths = new_paths

        cfg.keep_alive_file.unlink()
        run_vim(paths)


def _process_vim_commands(
    zettel_dir: Path, vim_commands: Iterable[str]
) -> Iterator[str]:
    for vim_cmd in vim_commands:
        if "{zdir}" in vim_cmd:
            yield vim_cmd.format(zdir=zettel_dir)
        else:
            yield vim_cmd
