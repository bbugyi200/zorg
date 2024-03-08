"""Contains this project's clack runners."""

from __future__ import annotations

from pathlib import Path
import tempfile
from typing import Any, Iterable, Iterator, Mapping

from clack.types import ClackRunner
import jinja2
from logrus import Logger
import metaman
from typist import PathLike
import vimala

from . import common
from .config import Config, EditConfig, TemplateRenderConfig
from .file_groups import expand_file_group_paths


logger = Logger(__name__)

RUNNERS: list[ClackRunner] = []
runner = metaman.register_function_factory(RUNNERS)


@runner
def run_edit(cfg: EditConfig) -> int:
    """Runner for the 'edit' command."""
    tmpl_manager = _ZorgTemplateManager(cfg)
    zo_paths = expand_file_group_paths(
        cfg.zo_paths, file_group_map=cfg.file_group_map
    )
    zo_paths = _add_paths_to_zdir(cfg.zettel_dir, zo_paths)
    for zo_path in zo_paths:
        for pattern, tmpl_path in cfg.template_pattern_map.items():
            if match := pattern.match(zo_path.stem):
                if not zo_path.exists():
                    logger.info(
                        "Creating new file using registered template.",
                        new_file=zo_path,
                        template=tmpl_path,
                    )
                    contents = tmpl_manager.render(
                        tmpl_path, common.process_var_map(match.groupdict())
                    )
                    zo_path.parent.mkdir(parents=True, exist_ok=True)
                    zo_path.write_text(contents)
                break

    _start_vim_loop(zo_paths, cfg=cfg)
    return 0


def _add_paths_to_zdir(
    zdir: PathLike, paths: Iterable[PathLike]
) -> list[Path]:
    zdir_path = Path(zdir)
    new_paths = []
    for p in paths:
        path = Path(p)
        new_paths.append(
            path if zdir_path in path.parents else zdir_path / path
        )
    return new_paths


def _start_vim_loop(zo_paths: Iterable[Path], cfg: EditConfig) -> None:
    cfg.keep_alive_file.parent.mkdir(parents=True, exist_ok=True)
    cfg.keep_alive_file.touch()
    logger.debug(
        "Vim loop will run as long as the keep alive file exists.",
        keep_alive_file=cfg.keep_alive_file,
    )
    last_paths = zo_paths
    while cfg.keep_alive_file.exists():
        if cfg.keep_alive_file.stat().st_size == 0:
            paths = last_paths
        else:
            new_paths = [
                Path(p.strip())
                for p in cfg.keep_alive_file.read_text().split()
            ]
            logger.debug(
                "Editing files specified in the keep alive file.",
                keep_alive_file=cfg.keep_alive_file,
                old_paths=last_paths,
                new_paths=new_paths,
            )
            paths = last_paths = new_paths

        cfg.keep_alive_file.unlink()
        vimala.vim(
            *_add_paths_to_zdir(cfg.zettel_dir, paths),
            commands=_process_vim_commands(cfg.zettel_dir, cfg.vim_commands),
        ).unwrap()


def _process_vim_commands(
    zettel_dir: Path, vim_commands: Iterable[str]
) -> Iterator[str]:
    for vim_cmd in vim_commands:
        if "{zdir}" in vim_cmd:
            yield vim_cmd.format(zdir=zettel_dir)
        else:
            yield vim_cmd


@runner
def run_template_render(cfg: TemplateRenderConfig) -> int:
    """Runner for the 'template' command."""
    tmpl_manager = _ZorgTemplateManager(cfg)
    print(tmpl_manager.render(cfg.template, cfg.var_map))
    return 0


class _ZorgTemplateManager:
    tmp_dir = tempfile.TemporaryDirectory()

    def __init__(self, cfg: Config) -> None:
        tmp_dir_path = Path(self.tmp_dir.name)
        loader = jinja2.FileSystemLoader(searchpath=tmp_dir_path)

        self._temp_dir_path = tmp_dir_path
        self._template_env = jinja2.Environment(loader=loader)
        self._cfg = cfg

    def render(self, template_path: Path, var_map: Mapping[str, Any]) -> str:
        """Renders {template_path} using {var_map} for template variables."""
        self._build_template_in_dir(
            self._temp_dir_path, self._cfg.zettel_dir / template_path
        )
        template = self._template_env.get_template(template_path.name)
        return template.render(var_map)

    @classmethod
    def _build_template_in_dir(
        cls, tmp_dir: Path, template_path: Path
    ) -> None:
        temp_template_path = tmp_dir / template_path.name
        new_lines = []
        blank_line_found = False
        for line in template_path.open("r"):
            if not blank_line_found and not line.strip():
                blank_line_found = True
                continue
            if blank_line_found:
                new_lines.append(
                    line[1:]
                    if line.startswith("## ") or line.strip() == "##"
                    else line
                )
        temp_template_path.write_text("".join(new_lines))
