"""Contains this project's clack runners."""

from __future__ import annotations

from pathlib import Path
import tempfile
from typing import Any, Iterable, Iterator, Mapping

import antlr4
from clack.types import ClackRunner
import jinja2
from logrus import Logger
import metaman
from typist import PathLike
import vimala

from . import common
from .config import (
    CompileConfig,
    DbInfoConfig,
    EditConfig,
    OpenActionConfig,
    TemplateInitConfig,
    TemplateRenderConfig,
)
from .file_groups import expand_file_group_paths
from .grammar.zorg_file.ZorgFileListener import ZorgFileListener
from .grammar.zorg_file.ZorgFileLexer import ZorgFileLexer
from .grammar.zorg_file.ZorgFileParser import ZorgFileParser
from .types import TemplatePatternMapType, VarMapType


logger = Logger(__name__)

RUNNERS: list[ClackRunner] = []
runner = metaman.register_function_factory(RUNNERS)


class ZorgFileCompiler(ZorgFileListener):
    """Listener that compiles zorg files into zorc files."""

    def enterBlock(self, ctx: ZorgFileParser.BlockContext) -> None:
        del ctx
        return


@runner
def run_compile(cfg: CompileConfig) -> int:
    """Runner for the 'compile' command."""
    stream = antlr4.FileStream(str(cfg.zo_path))
    lexer = ZorgFileLexer(stream)
    tokens = antlr4.CommonTokenStream(lexer)
    parser = ZorgFileParser(tokens)
    tree = parser.prog()
    compiler = ZorgFileCompiler()
    walker = antlr4.ParseTreeWalker()
    walker.walk(compiler, tree)
    return 0


@runner
def run_action_open(cfg: OpenActionConfig) -> int:
    """Runner for the 'action open' command."""
    zo_path = _prepend_zdir(cfg.zettel_dir, [cfg.zo_path])[0]
    zo_line = zo_path.read_text().split("\n")[cfg.line_number - 1]
    for word in zo_line.split(" "):
        left_find = word.find("[[")
        right_find = word.find("]")
        if left_find >= 0 and right_find >= 0:
            link_base = word[left_find + 2 : right_find].split("::")[0]
            link_base = link_base if "." in link_base else f"{link_base}.zo"
            link_path = _prepend_zdir(cfg.zettel_dir, [Path(link_base)])[0]
            _run_template_init(
                cfg.zettel_dir,
                cfg.template_pattern_map,
                link_path,
                var_map={
                    "parent": (
                        str(zo_path)
                        .replace(".zo", "")
                        .replace(str(cfg.zettel_dir) + "/", "")
                    )
                },
            )
            print(f"EDIT {link_path}")
            break
    return 0


@runner
def run_db_info(cfg: DbInfoConfig) -> int:
    """Runner for the 'db info' command."""
    del cfg
    return 0


@runner
def run_edit(cfg: EditConfig) -> int:
    """Runner for the 'edit' command."""
    zo_paths = expand_file_group_paths(
        cfg.zo_paths, file_group_map=cfg.file_group_map
    )
    zo_paths = _prepend_zdir(cfg.zettel_dir, zo_paths)
    for zo_path in zo_paths:
        _run_template_init(cfg.zettel_dir, cfg.template_pattern_map, zo_path)

    _start_vim_loop(zo_paths, cfg=cfg)
    return 0


@runner
def run_template_init(cfg: TemplateInitConfig) -> int:
    _run_template_init(
        cfg.zettel_dir,
        cfg.template_pattern_map,
        cfg.new_path,
        template=cfg.template,
        var_map=cfg.var_map,
    )
    return 0


@runner
def run_template_render(cfg: TemplateRenderConfig) -> int:
    """Runner for the 'template' command."""
    tmpl_manager = _ZorgTemplateManager(cfg.zettel_dir)
    print(tmpl_manager.render(cfg.template, cfg.var_map))
    return 0


def _run_template_init(
    zettel_dir: PathLike,
    template_pattern_map: TemplatePatternMapType,
    new_path: PathLike,
    *,
    template: Path = None,
    var_map: VarMapType = None,
) -> None:
    zettel_dir = Path(zettel_dir)
    new_path = _prepend_zdir(zettel_dir, [Path(new_path)])[0]
    var_map = {} if var_map is None else dict(var_map)

    if new_path.exists():
        return

    matched_template = template
    for pattern, tmpl_path in template_pattern_map.items():
        if match := pattern.match(new_path.name):
            matched_template = tmpl_path
            var_map |= match.groupdict()
            break

    if matched_template is None:
        logger.warn(
            "Unable to match new filename with any registered templates.",
            template_pattern_map=template_pattern_map,
            new_path=new_path,
        )
        return

    logger.info(
        "Creating new file using zorg template.",
        new_file=new_path,
        template=matched_template,
    )
    tmpl_manager = _ZorgTemplateManager(zettel_dir)
    contents = tmpl_manager.render(
        _prepend_zdir(zettel_dir, [matched_template])[0],
        common.process_var_map(var_map),
    )
    new_path.parent.mkdir(parents=True, exist_ok=True)
    new_path.write_text(contents)


def _prepend_zdir(zdir: PathLike, paths: Iterable[PathLike]) -> list[Path]:
    zdir_path = Path(zdir)
    new_paths = []
    for p in paths:
        path = Path(p)
        new_paths.append(
            path if zdir_path in path.parents else zdir_path / path
        )
    return new_paths


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
            new_paths = _prepend_zdir(
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


class _ZorgTemplateManager:
    tmp_dir = tempfile.TemporaryDirectory()

    def __init__(self, zettel_dir: Path) -> None:
        tmp_dir_path = Path(self.tmp_dir.name)
        loader = jinja2.FileSystemLoader(searchpath=tmp_dir_path)

        self._temp_dir_path = tmp_dir_path
        self._template_env = jinja2.Environment(loader=loader)
        self._zettel_dir = zettel_dir

    def render(self, template_path: Path, var_map: Mapping[str, Any]) -> str:
        """Renders {template_path} using {var_map} for template variables."""
        self._build_template_in_dir(
            self._temp_dir_path, self._zettel_dir / template_path
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
