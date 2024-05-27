"""Contains runners for the 'zorg action' command."""

from pathlib import Path
from typing import Final, Optional

from logrus import Logger

from ...service import common as c, dates as zdt, swog
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
    is_zoq_file = zo_path.suffix == ".zoq"
    zo_lines = zo_path.read_text().split("\n")
    zo_line = zo_lines[cfg.line_number - 1]

    all_targets_in_line: list[str] = []
    found_primary_zid = False
    for i, word in enumerate(
        [w.strip("(),.?!;:") for w in zo_line.split(" ")]
    ):
        left_idx = word.find("[[")
        right_idx = word.find("]]")
        is_link = left_idx >= 0 and right_idx >= 0
        is_targetable_zid = zdt.is_zid(word) and (
            found_primary_zid or is_zoq_file or i == 0
        )
        if is_link or is_targetable_zid:
            all_targets_in_line.append(word)
        elif (
            not found_primary_zid
            and not _is_prefix_symbol(word)
            and not _is_priority(word)
            and not zdt.is_short_date_spec(word)
            and not zdt.is_zid(word)
        ):
            found_primary_zid = True

    # If the provided line is a zorg query...
    if zo_line.startswith(("# S ", "# W ")) and is_zoq_file:
        _refresh_zoq_file(cfg, zo_path)
        print(f"EDIT {zo_path}")
    # Else if the provided line contains targets (e.g. links)...
    elif all_targets_in_line:
        target: Optional[str] = None
        if len(all_targets_in_line) == 1:
            word = list(all_targets_in_line)[0]
            target = word
        elif cfg.option_idx is None:
            link_choice_msg_part = " ".join(all_targets_in_line)
            print(f"PROMPT {link_choice_msg_part}")
        else:
            for i, (word) in enumerate(all_targets_in_line):
                if i + 1 == cfg.option_idx:
                    target = word
                    break
            else:
                _LOGGER.warning(
                    "Unknown option selected", option=cfg.option_idx
                )
                return 1

        if target is not None:
            if target.startswith("[[") and target.endswith("]]"):
                return _open_link(cfg, zo_path, target)
            else:
                return _open_zid(cfg, target)
    # Else we tell vim to echo an error message.
    else:
        print(f"ECHO {_MSG_NOTHING_TO_OPEN} #{cfg.line_number}")

    return 0


def _open_link(cfg: OpenActionConfig, zo_path: Path, link: str) -> int:
    link_parts = link.split("::")
    link_base = (
        link_parts[0][2:-2] if len(link_parts) == 1 else link_parts[0][2:]
    )
    link_base = link_base if "." in link_base else f"{link_base}.zo"
    link_path = c.prepend_zdir(cfg.zettel_dir, [Path(link_base)])[0]

    if not link_path.exists():
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
    elif link_path.suffix == ".zoq":
        _refresh_zoq_file(cfg, link_path)

    print(f"EDIT {link_path}")
    if len(link_parts) > 1:
        print(f"SEARCH id::{link_parts[1][:-2]}")

    return 0


def _open_zid(cfg: OpenActionConfig, zid: str) -> int:
    with SQLSession(
        cfg.zettel_dir, cfg.database_url, verbose=cfg.verbose
    ) as session:
        note = session.repo.get_by_zid(zid)

    if note is None:
        return 1

    assert note.file_path is not None
    note_file_path = c.prepend_zdir(cfg.zettel_dir, [note.file_path])[0]
    print(f"EDIT {note_file_path}")
    print(f"SEARCH {zid}")

    return 0


def _refresh_zoq_file(cfg: OpenActionConfig, zoq_path: Path) -> None:
    with SQLSession(
        cfg.zettel_dir, cfg.database_url, verbose=cfg.verbose
    ) as session:
        swog.refresh_zoq_file(session, zoq_path)


def _is_priority(word: str) -> bool:
    return len(word) == 2 and word[0] == "P" and word[1].isdigit()


def _is_prefix_symbol(word: str) -> bool:
    return word in ["-", "<", ">", "o", "x"]
