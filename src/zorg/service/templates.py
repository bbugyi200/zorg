"""Common utilities shared by multiple clack runners."""

import datetime as dt
from pathlib import Path
import tempfile
from typing import Any, Mapping

import jinja2
from logrus import Logger
from typist import PathLike

from . import common
from ..domain.types import TemplatePatternMapType, VarMapType


_LOGGER = Logger(__name__)


def init_from_template(
    zdir: PathLike,
    template_pattern_map: TemplatePatternMapType,
    new_path: PathLike,
    *,
    template: Path = None,
    var_map: VarMapType = None,
    should_overwrite_existing: bool = False,
) -> None:
    """Initialize a new file by rendering a template if necessary.

    Args:
        zdir: The zettel directory where this file will be created.
        template_pattern_map: A map of filename patterns to .zot template files
            used to determine which template to use if the {template} argument
            is not provided.
        new_path: The path of the file you want to initialize.
        should_overwrite_existing: If {new_path} exists, should we overwrite
            its contents or return early?
        template: Optional path to a .zot template file that should be used to
            render {new_path}.
        var_map: A map of template variable keys to values.
    """
    zdir = Path(zdir)
    new_path = common.prepend_zdir(zdir, [Path(new_path)])[0]
    var_map = {} if var_map is None else dict(var_map)

    if new_path.exists() and not should_overwrite_existing:
        return

    matched_template = template
    for pattern, tmpl_path in template_pattern_map.items():
        if match := pattern.match(common.strip_zdir(zdir, new_path)):
            matched_template = tmpl_path
            var_map |= match.groupdict()
            break

    if matched_template is None:
        _LOGGER.warn(
            "Unable to match new filename with any registered templates.",
            template_pattern_map=template_pattern_map,
            new_path=new_path,
        )
        return

    _LOGGER.info(
        "Creating new file using zorg template.",
        new_file=new_path,
        template=matched_template,
    )
    tmpl_manager = ZorgTemplateManager(zdir)
    contents = tmpl_manager.render(
        common.prepend_zdir(zdir, [matched_template])[0],
        common.process_var_map(var_map),
    )
    new_path.parent.mkdir(parents=True, exist_ok=True)
    new_path.write_text(contents)


class ZorgTemplateManager:
    """Manages the rendering of all zorg (i.e. *.zot) templates."""

    tmp_dir = tempfile.TemporaryDirectory()

    def __init__(self, zdir: Path) -> None:
        tmp_dir_path = Path(self.tmp_dir.name)
        loader = jinja2.FileSystemLoader(searchpath=tmp_dir_path)

        self._temp_dir_path = tmp_dir_path
        self._template_env = jinja2.Environment(loader=loader)
        self._zdir = zdir

    def render(self, template_path: Path, var_map: Mapping[str, Any]) -> str:
        """Renders {template_path} using {var_map} for template variables."""
        var_map = {} if var_map is None else dict(var_map)
        self._build_template_in_dir(
            self._temp_dir_path, self._zdir / template_path
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
