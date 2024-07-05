"""Contains runners for the 'zorg action' command."""

from pathlib import Path
import subprocess as sp
from typing import Final, Optional

from logrus import Logger

from ...service import common as c, dates as zdt, swog
from ...service.templates import init_from_template
from ...storage.sql.session import SQLSession
from ..config import OpenActionConfig
from ._runners import runner


_LOCAL_LINK_LEFT_MARK: Final = "[^"
_LOGGER = Logger(__name__)
_MSG_NOTHING_TO_OPEN: Final = (
    "We did not find anything zorg knows how to open on line"
)
_SEARCH_END: Final = "\\ze\\(\\s\\|[),.?!;:]\\|$\\)"


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
        is_link = word.find("[[") >= 0 and word.find("]]") >= 0
        # Is this word a ZID that should be considered as a target? We consider
        # any ZID that is NOT the primary ZID to be targetable. In *.zoq files,
        # every ZID is targetable.
        zid_word = word.strip("[]")
        is_targetable_zid = zdt.is_zid(zid_word) and (
            found_primary_zid or is_zoq_file or i == 0
        )
        is_id_link = word.find("[#") >= 0 and word.find("]") >= 0
        is_rid_link = word.find("[@") >= 0 and word.find("]") >= 0
        is_cite_key_link = word.startswith("z::")
        if (
            is_link
            or _is_local_link(word)
            or is_id_link
            or is_rid_link
            or is_cite_key_link
        ):
            all_targets_in_line.append(word)
        elif is_targetable_zid:
            all_targets_in_line.append(zid_word)
        elif (
            not found_primary_zid
            and not _is_prefix_symbol(word)
            and not _is_priority(word)
            and not zdt.is_short_date_spec(word)
            and not zdt.is_zid(word)
        ):
            found_primary_zid = True

    # If the provided line is a zorg query...
    if (
        zo_line.startswith(("# S ", "# W "))
        and not zo_line.startswith(("# S = ", "# W = "))
        and is_zoq_file
    ):
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
                return _open_file_link(cfg, zo_path, target)
            elif _is_local_link(target):
                return _open_local_link(target)
            elif target.startswith("[#") and target.endswith("]"):
                return _open_global_link(cfg, target)
            elif target.startswith("[@") and target.endswith("]"):
                return _open_rid_link(cfg, target)
            elif target.startswith("z::"):
                return _open_cite_key_link(cfg.zettel_dir, target)
            else:
                return _open_zid_link(cfg, target)
    # Else we tell vim to echo an error message.
    else:
        print(f"ECHO {_MSG_NOTHING_TO_OPEN} #{cfg.line_number}")

    return 0


def _is_local_link(word: str) -> bool:
    left_idx = word.find(_LOCAL_LINK_LEFT_MARK)
    right_idx = word.find("]")
    return left_idx >= 0 and right_idx >= 0


def _open_file_link(cfg: OpenActionConfig, zo_path: Path, link: str) -> int:
    link_parts = link.split("#")
    link_base = (
        link_parts[0][2:-2] if len(link_parts) == 1 else link_parts[0][2:]
    )
    link_base = link_base if "." in link_base else f"{link_base}.zo"
    link_path = c.prepend_zdir(cfg.zettel_dir, [Path(link_base)])[0]

    if not link_path.exists():
        parent = c.simplify_fname(cfg.zettel_dir, zo_path)
        init_from_template(
            cfg.zettel_dir,
            cfg.template_pattern_map,
            link_path,
            var_map={"parent": parent},
        )
    elif link_path.suffix == ".zoq":
        _refresh_zoq_file(cfg, link_path)

    print(f"EDIT {link_path}")
    if len(link_parts) > 1:
        print(f"SEARCH LID::{link_parts[1][:-2]}")

    return 0


def _open_cite_key_link(zdir: Path, z_cite_key: str) -> int:
    cite_key = z_cite_key.split("::")[1]
    sp.Popen(
        ["papis", "--cc", "zotero", "import", "-s", str(zdir / "zotero")]
    ).communicate()
    popen = sp.Popen(
        ["papis", "list", "-a", f"ref:{cite_key}"], stdout=sp.PIPE
    )
    stdout, _ = popen.communicate()
    papis_item_dir = stdout.decode().strip().split("\n", maxsplit=1)[0]
    print(f"EDIT {papis_item_dir}/info.yaml")
    return 0


def _open_local_link(local_link: str) -> int:
    lid_value = local_link[len(_LOCAL_LINK_LEFT_MARK) : -1]
    print(f"SEARCH LID::{lid_value}{_SEARCH_END}")
    return 0


def _open_global_link(cfg: OpenActionConfig, id_link: str) -> int:
    id_key = id_link[2:-1]
    with SQLSession(
        cfg.zettel_dir, cfg.database_url, verbose=cfg.verbose
    ) as session:
        notes = session.repo.get_notes_by_id(id_key)

    if not notes:
        print(f"ECHO No notes with found with the ID::{id_key} property")
        return 1

    pages = list({note.file_path for note in notes})
    if len(pages) > 1:
        matched_files = " ".join(sorted({str(page) for page in pages}))
        print(
            "ECHO Multiple pages found containing notes with the"
            f" ID::{id_key} property: {matched_files}"
        )
        return 1

    page = pages[0]
    full_page_path = c.prepend_zdir(cfg.zettel_dir, [page])[0]
    print(f"EDIT {full_page_path}")
    print(f"SEARCH ID::{id_key}{_SEARCH_END}")

    return 0


def _open_rid_link(cfg: OpenActionConfig, rid_link: str) -> int:
    rid_key = rid_link[2:-1]
    with SQLSession(
        cfg.zettel_dir, cfg.database_url, verbose=cfg.verbose
    ) as session:
        notes = session.repo.get_notes_by_id(rid_key, id_key="RID")

    if not notes:
        print(f"ECHO No notes with found with the RID::{rid_key} property")
        return 1

    if len(notes) > 1:
        matched_files = " ".join(sorted({str(n.file_path) for n in notes}))
        print(
            f"ECHO Multiple notes found the with the ID::{rid_key} property:"
            f" {matched_files}"
        )
        return 1

    note = notes[0]
    assert note.file_path is not None
    note_file_path = c.prepend_zdir(cfg.zettel_dir, [note.file_path])[0]
    print(f"EDIT {note_file_path}")
    print(f"SEARCH RID::{rid_key}{_SEARCH_END}")

    return 0


def _open_zid_link(cfg: OpenActionConfig, zid: str) -> int:
    with SQLSession(
        cfg.zettel_dir, cfg.database_url, verbose=cfg.verbose
    ) as session:
        note = session.repo.get_note_by_zid(zid)

    if note is None:
        return 1

    assert note.file_path is not None
    note_file_path = c.prepend_zdir(cfg.zettel_dir, [note.file_path])[0]
    print(f"EDIT {note_file_path}")
    print(f"SEARCH \\s\\zs{zid}")

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
