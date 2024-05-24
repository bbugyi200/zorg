"""Contains runners for the 'zorg action' command."""

import datetime as dt
from functools import partial
import itertools as it
from pathlib import Path
from typing import Final, Optional

from logrus import Logger

from ...service import common as c, swog
from ...service.templates import init_from_template
from ...storage.sql.session import SQLSession
from ..config import OpenActionConfig
from ._runners import runner


_LOGGER = Logger(__name__)
_MSG_NOTHING_TO_OPEN: Final = (
    "We did not find anything zorg knows how to open on line"
)


@runner
def run_action_open(cfg: OpenActionConfig) -> int:
    """Runner for the 'action open' command."""
    zo_path = c.prepend_zdir(cfg.zettel_dir, [cfg.zo_path])[0]
    zo_lines = zo_path.read_text().split("\n")
    zo_line = zo_lines[cfg.line_number - 1]
    link_word_idx_map: dict[str, tuple[int, int]] = {}
    for word in zo_line.split(" "):
        left_idx = word.find("[[")
        right_idx = word.find("]]")
        if left_idx >= 0 and right_idx >= 0:
            link_word_idx_map[word] = (left_idx, right_idx)

    if link_word_idx_map:
        word_left_right: Optional[tuple[str, int, int]] = None
        if len(link_word_idx_map) == 1:
            word = list(link_word_idx_map.keys())[0]
            left_idx, right_idx = link_word_idx_map[word]
            word_left_right = word, left_idx, right_idx
        elif cfg.option_idx is None:
            link_choice_msg_part = " ".join(link_word_idx_map.keys())
            print(f"PROMPT {link_choice_msg_part}")
        else:
            for i, (word, (left_idx, right_idx)) in enumerate(
                link_word_idx_map.items()
            ):
                if i + 1 == cfg.option_idx:
                    word_left_right = word, left_idx, right_idx
                    break
            else:
                _LOGGER.warning(
                    "Unknown option selected", option=cfg.option_idx
                )

        if word_left_right is not None:
            word, left_idx, right_idx = word_left_right
            link_parts = word[left_idx + 2 : right_idx].split("::")
            link_base = link_parts[0]
            link_base = link_base if "." in link_base else f"{link_base}.zo"
            link_path = c.prepend_zdir(cfg.zettel_dir, [Path(link_base)])[0]

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
            if len(link_parts) > 1:
                print(f"SEARCH id::{link_parts[1]}")

    else:
        if zo_line.startswith(("# S ", "# W ")):
            query_string = zo_line.strip()[2:]
            with SQLSession(
                cfg.zettel_dir, cfg.database_url, verbose=cfg.verbose
            ) as session:
                query_results = swog.execute(session, query_string)

            date_spec = dt.datetime.now().strftime("%Y-%m-%d at %H:%M:%S")
            stats_line_start = "# Saved query generated on"
            old_header_lines = it.takewhile(
                partial(_is_zoq_header_line, stats_line_start),
                zo_lines,
            )
            old_header = "\n".join(old_header_lines)
            stats_line = f"{stats_line_start} {date_spec}."
            maybe_hash_line = "" if old_header.endswith("#") else "#\n"
            zoq_contents = (
                f"{old_header}\n"
                f"{maybe_hash_line}"
                f"{stats_line}\n\n"
                f"{query_results}"
            )
            with zo_path.open("w") as f:
                f.write(zoq_contents)

            print(f"EDIT {zo_path}")
        else:
            print(f"ECHO {_MSG_NOTHING_TO_OPEN} #{cfg.line_number}")

    return 0


def _is_zoq_header_line(end_marker: str, line: str) -> bool:
    return line.startswith("#") and not line.startswith(end_marker)
