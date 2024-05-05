"""Contains runners for the 'zorg action' command."""

from pathlib import Path
from typing import Final

from ...service.common import prepend_zdir
from ...service.templates import init_from_template
from ..config import OpenActionConfig
from ._runners import runner


_MSG_NOTHING_TO_OPEN: Final = (
    "We did not find anything zorg knows how to open on line"
)


@runner
def run_action_open(cfg: OpenActionConfig) -> int:
    """Runner for the 'action open' command."""
    zo_path = prepend_zdir(cfg.zettel_dir, [cfg.zo_path])[0]
    zo_lines = zo_path.read_text().split("\n")
    zo_line = zo_lines[cfg.line_number - 1]
    for word in zo_line.split(" "):
        left_find = word.find("[[")
        right_find = word.find("]")
        if left_find >= 0 and right_find >= 0:
            link_base = word[left_find + 2 : right_find].split("::")[0]
            link_base = link_base if "." in link_base else f"{link_base}.zo"
            link_path = prepend_zdir(cfg.zettel_dir, [Path(link_base)])[0]
            init_from_template(
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
    else:
        print(f"ECHO {_MSG_NOTHING_TO_OPEN} #{cfg.line_number}")

    return 0
