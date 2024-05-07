"""Contains runners for the 'zorg template' command."""

from pathlib import Path
from typing import Any, Iterable

from ...domain.types import VarMapType
from ...service import common as c
from ...service.templates import ZorgTemplateManager, init_from_template
from ..config import (
    TemplateInitConfig,
    TemplateListConfig,
    TemplateRenderConfig,
)
from ._runners import runner


@runner
def run_template_init(cfg: TemplateInitConfig) -> int:
    """Runner for the 'template init' command."""
    template = (
        _get_zot_path(cfg.zettel_dir, cfg.template) if cfg.template else None
    )
    init_from_template(
        cfg.zettel_dir,
        cfg.template_pattern_map,
        cfg.new_path,
        template=template,
        var_map=cfg.var_map,
    )
    return 0


@runner
def run_template_render(cfg: TemplateRenderConfig) -> int:
    """Runner for the 'template render' command."""
    template = _get_zot_path(cfg.zettel_dir, cfg.template)
    tmpl_manager = ZorgTemplateManager(cfg.zettel_dir)
    var_map = _prompt_for_missing_vars(
        cfg.var_map, sorted(_get_zot_vars(template))
    )
    print(tmpl_manager.render(template, var_map))
    return 0


@runner
def run_template_list(cfg: TemplateListConfig) -> int:
    """Runner for the 'template list' command."""
    for zot_path in sorted(Path(cfg.zettel_dir).rglob("*.zot")):
        print(zot_path.name.replace(".zot", ""))
        for var in sorted(_get_zot_vars(zot_path)):
            print(f"  - {var}")
    return 0


def _get_zot_path(zettel_dir: Path, template: Path) -> Path:
    maybe_zot_file = str(template)
    zot_file = (
        maybe_zot_file
        if maybe_zot_file.endswith(".zot")
        else f"{maybe_zot_file}.zot"
    )
    zot_path = c.prepend_zdir(zettel_dir, [zot_file])[0]
    return zot_path


def _prompt_for_missing_vars(
    var_map: VarMapType, required_vars: Iterable[str]
) -> dict[str, Any]:
    new_var_map = dict(var_map)
    for var in required_vars:
        if var not in new_var_map:
            v = input(f"{var}: ")
            new_var_map[var] = v
    return new_var_map


def _get_zot_vars(zot_path: Path) -> set[str]:
    variables: set[str] = set()
    banned_vars: set[str] = set()
    for line in zot_path.read_text().split("\n"):
        if line.startswith("{% set "):
            banned_vars.add(line.split(" ")[2])

        found_var = False
        for token in line.split(" "):
            if found_var:
                found_var = False
                var = token.split(".")[0]
                if var not in banned_vars:
                    variables.add(var)
            elif token.startswith("{{") and token.endswith("}}"):
                var = token.split(".")[0][2:-2]
                if var not in banned_vars:
                    variables.add(var)
            elif token.endswith("{{"):
                found_var = True
    return variables
