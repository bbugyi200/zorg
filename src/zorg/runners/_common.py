"""Common utilities shared by multiple clack runners."""

import datetime as dt
from pathlib import Path
import tempfile
from typing import Any, Iterable, Mapping

import jinja2
from logrus import Logger
from typist import PathLike

from .. import common
from ..types import TemplatePatternMapType, VarMapType


logger = Logger(__name__)


def run_template_init(
    zettel_dir: PathLike,
    template_pattern_map: TemplatePatternMapType,
    new_path: PathLike,
    *,
    template: Path = None,
    var_map: VarMapType = None,
) -> None:
    zettel_dir = Path(zettel_dir)
    new_path = prepend_zdir(zettel_dir, [Path(new_path)])[0]
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
    tmpl_manager = ZorgTemplateManager(zettel_dir)
    contents = tmpl_manager.render(
        prepend_zdir(zettel_dir, [matched_template])[0],
        common.process_var_map(var_map),
    )
    new_path.parent.mkdir(parents=True, exist_ok=True)
    new_path.write_text(contents)


def prepend_zdir(zdir: PathLike, paths: Iterable[PathLike]) -> list[Path]:
    zdir_path = Path(zdir)
    new_paths = []
    for p in paths:
        path = Path(p)
        new_paths.append(
            path if zdir_path in path.parents else zdir_path / path
        )
    return new_paths


class ZorgTemplateManager:
    tmp_dir = tempfile.TemporaryDirectory()

    def __init__(self, zettel_dir: Path) -> None:
        tmp_dir_path = Path(self.tmp_dir.name)
        loader = jinja2.FileSystemLoader(searchpath=tmp_dir_path)

        self._temp_dir_path = tmp_dir_path
        self._template_env = jinja2.Environment(loader=loader)
        self._zettel_dir = zettel_dir

    def render(self, template_path: Path, var_map: Mapping[str, Any]) -> str:
        """Renders {template_path} using {var_map} for template variables."""
        var_map = {} if var_map is None else dict(var_map)
        self._build_template_in_dir(
            self._temp_dir_path, self._zettel_dir / template_path
        )
        template = self._template_env.get_template(template_path.name)
        return template.render(var_map | {"dt": dt})

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
