"""Contains runners for the 'zorg action' command."""

import datetime as dt
from pathlib import Path
from tempfile import NamedTemporaryFile
from typing import Final

from ...service.common import prepend_zdir
from ...service.compiler import build_zorg_query
from ...service.swog import execute
from ...service.templates import init_from_template
from ...storage.sql.session import SQLSession
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
        name_sep = " | "
        if zo_line.startswith(("# S ", "# W ")) and name_sep in zo_line:
            query_string, query_name = zo_line.strip()[2:].split(name_sep)
            with SQLSession(
                cfg.zettel_dir, cfg.database_url, verbose=cfg.verbose
            ) as session:
                query_results = execute(session, query_string)

            query_dir = cfg.zettel_dir / "query"
            query_dir.mkdir(exist_ok=True)
            query_path = query_dir / f"{query_name}.zo"

            date_spec = dt.datetime.now().strftime("%Y-%m-%d at %H:%M:%S")
            if cfg.zo_path == query_path:
                parent_link = ""
            else:
                parent_link = f"from [[{cfg.zo_path}]] ".replace(".zo", "")
            with query_path.open("w") as f:
                f.write(
                    f"# {query_string} | {query_name}\n#\n# Saved query"
                    f" generated {parent_link}on"
                    f" {date_spec}.\n\n{query_results}"
                )

            print(f"EDIT {query_path}")
        else:
            print(f"ECHO {_MSG_NOTHING_TO_OPEN} #{cfg.line_number}")

    return 0
