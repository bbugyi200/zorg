"""Contains runners for the 'zorg action' command."""

from pathlib import Path

from ..config import OpenActionConfig
from ._common import prepend_zdir, run_template_init
from ._registry import runner


@runner
def run_action_open(cfg: OpenActionConfig) -> int:
    """Runner for the 'action open' command."""
    zo_path = prepend_zdir(cfg.zettel_dir, [cfg.zo_path])[0]
    zo_line = zo_path.read_text().split("\n")[cfg.line_number - 1]
    for word in zo_line.split(" "):
        left_find = word.find("[[")
        right_find = word.find("]")
        if left_find >= 0 and right_find >= 0:
            link_base = word[left_find + 2 : right_find].split("::")[0]
            link_base = link_base if "." in link_base else f"{link_base}.zo"
            link_path = prepend_zdir(cfg.zettel_dir, [Path(link_base)])[0]
            run_template_init(
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
