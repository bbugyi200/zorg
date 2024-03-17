"""Contains runners for the 'zorg template' command."""

from ..config import TemplateInitConfig, TemplateRenderConfig
from ._common import (
    ZorgTemplateManager,
    run_template_init as _run_template_init,
)
from ._registry import runner


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
    tmpl_manager = ZorgTemplateManager(cfg.zettel_dir)
    print(tmpl_manager.render(cfg.template, cfg.var_map))
    return 0
