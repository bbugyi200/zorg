"""Contains runners for the 'zorg template' command."""

from pathlib import Path
import sys
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
        should_overwrite_existing=cfg.should_overwrite_existing,
        template=template,
        var_map=cfg.var_map,
    )
    return 0


@runner
def run_template_list(cfg: TemplateListConfig) -> int:
    """Runner for the 'template list' command."""
    for zot_path in sorted(Path(cfg.zettel_dir).rglob("*.zot")):
        print(zot_path.name.replace(".zot", ""))
        for var in sorted(_get_zot_vars(zot_path)):
            print(f"  - {var}")
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


def _get_zot_path(zettel_dir: Path, template: Path) -> Path:
    zot_path = c.prepend_zdir(zettel_dir, [template])[0]
    if not zot_path.exists() or not zot_path.is_file():
        matched_zot_paths: list[Path] = []
        for some_zot_path in sorted(zettel_dir.rglob("*.zot")):
            if str(zot_path) in str(some_zot_path):
                matched_zot_paths.append(some_zot_path)
        if not matched_zot_paths:
            raise RuntimeError(f"Unknown template path: {template}")

        if len(matched_zot_paths) == 1:
            zot_path = matched_zot_paths[0]
        else:
            prompt = ""
            for i, candidate_zot_path in enumerate(matched_zot_paths):
                candidate_zot_name = c.strip_zdir(
                    zettel_dir, candidate_zot_path
                ).replace(".zot", "")
                # Use 'spaces' to align the template names.
                spaces = " " * (
                    len(str(len(matched_zot_paths))) - len(str(i + 1))
                )
                prompt += f"{i + 1}){spaces} {candidate_zot_name}\n"
            prompt += "\nSelect a zot template: "
            idx = int(c.zinput(prompt)) - 1
            print(file=sys.stderr)
            zot_path = matched_zot_paths[idx]
    return zot_path


def _prompt_for_missing_vars(
    var_map: VarMapType, required_vars: Iterable[str]
) -> dict[str, Any]:
    new_var_map = dict(var_map)
    found_missing_vars = False
    for var in required_vars:
        if var not in new_var_map:
            found_missing_vars = True
            v = c.zinput(f"{var}: ")
            new_var_map[var] = v
    if found_missing_vars:
        print(file=sys.stderr)
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
            elif "{{" in token and "}}" in token:
                left_idx = token.find("{{") + 2
                right_idx = token.find("}}")
                if left_idx < right_idx:
                    var = token.split(".")[0][left_idx:right_idx]
                    if var not in banned_vars:
                        variables.add(var)
            elif token.endswith("{{"):
                found_var = True
    return variables
