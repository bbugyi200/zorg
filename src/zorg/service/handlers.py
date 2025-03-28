"""Zorg's event and command handlers live here."""

import datetime as dt
import hashlib
import json
from operator import attrgetter
from pathlib import Path
import sys
from typing import Callable, Iterable, Iterator, Optional, Sequence

from logrus import Logger
from tqdm import tqdm
import vimala

from zorg import APP_NAME
from zorg.domain.messages import commands, events
from zorg.domain.models import Note, Page
from zorg.domain.types import Color
from zorg.service import swog
from zorg.service.compiler import walk_zorg_page
from zorg.shared import common as c, dates as zdt
from zorg.storage.sql import SQLSession

_LOGGER = Logger(__name__)

_AddThingToFirstLine = Callable[[str, str], str]
_GetThing = Callable[[Note], str]


def edit_files(cmd: commands.EditCommand, session: SQLSession) -> None:
    """Command handler for the EditCommand."""
    for path in cmd.paths:
        if path.suffix == ".zoq":
            swog.refresh_zoq_file_with_session(session, path)
    vimala.vim(
        *cmd.paths,
        commands=_process_vim_commands(cmd.zettel_dir, cmd.vim_commands),
        vim_exe=cmd.vim_exe,
    ).unwrap()
    session.add_message(  # pylint: disable=unreachable
        events.EditorClosedEvent(edit_cmd=cmd)
    )


def check_keep_alive_file(
    event: events.EditorClosedEvent, session: SQLSession
) -> None:
    """Check if the 'keep alive' file exists and, if so, reopens the editor."""
    keep_alive_file = event.edit_cmd.keep_alive_file
    if not keep_alive_file.exists():
        _LOGGER.debug(
            "No keep alive file found.",
            keep_alive_file=str(keep_alive_file),
        )
        return

    zdir = event.edit_cmd.zettel_dir
    vim_commands = list(event.edit_cmd.vim_commands)
    if keep_alive_file.stat().st_size == 0:
        _LOGGER.debug(
            "Empty keep alive file found.",
            keep_alive_file=str(keep_alive_file),
        )
        paths = event.edit_cmd.paths
    else:
        keep_alive_lines = list(keep_alive_file.read_text().split())
        focused_filename = keep_alive_lines.pop()
        vim_commands = [
            cmd for cmd in vim_commands if not cmd.startswith("edit ")
        ]
        vim_commands.append(f"edit {focused_filename}")
        new_paths = c.bulk_prepend_zdir(
            zdir, [Path(p.strip()) for p in keep_alive_lines]
        )
        _LOGGER.debug(
            "Editing files specified in the keep alive file.",
            keep_alive_file=str(keep_alive_file),
            old_paths=[str(p) for p in event.edit_cmd.paths],
            new_paths=[str(p) for p in new_paths],
        )
        paths = new_paths

    verbose = event.edit_cmd.verbose
    if verbose <= 1:
        _LOGGER.debug(
            "Unlinking keep-alive file", keep_alive_file=str(keep_alive_file)
        )
        keep_alive_file.unlink()
    else:
        _LOGGER.debug(
            "We are NOT deleting the keep-alive file",
            keep_alive_file=str(keep_alive_file),
        )
    session.add_last_message(
        commands.EditCommand(
            zettel_dir=zdir,
            paths=paths,
            keep_alive_file=keep_alive_file,
            verbose=verbose,
            vim_commands=vim_commands,
            vim_exe=event.edit_cmd.vim_exe,
        )
    )


def create_database(
    cmd: commands.CreateDBCommand, session: SQLSession
) -> None:
    """Create a new zorg DB from scratch."""
    zorg_pages = []
    total_num_notes = 0
    error_file_whitelist = _get_error_file_whitelist(cmd.zettel_dir)
    old_error_files = error_file_whitelist.read_text().split("\n")
    error_files = []
    for zo_path in tqdm(
        _get_zo_paths_to_index(cmd.zettel_dir),
        desc="Reading notes from zorg files",
        file=sys.stdout,
    ):
        _LOGGER.info("Starting to walk zorg file", zorg_page=str(zo_path))
        zorg_page = walk_zorg_page(cmd.zettel_dir, zo_path)
        num_notes = len(zorg_page.notes)
        total_num_notes += num_notes
        _LOGGER.info(
            "Finished walking zorg file",
            zorg_page=zo_path.name,
            num_notes=num_notes,
            total_num_notes=total_num_notes,
        )
        session.repo.add_file(zorg_page)
        zorg_pages.append(zorg_page)
        zorg_page_path_str = c.strip_zdir(cmd.zettel_dir, zorg_page.path)
        if zorg_page.has_errors and (
            zorg_page_path_str in old_error_files
            or cmd.update_error_file_whitelist
        ):
            error_files.append(zorg_page_path_str)
        elif zorg_page.has_errors:
            raise RuntimeError(
                f"Previously valid Zorg file now has errors!: {zorg_page.path}"
            )
        elif (
            not zorg_page.has_errors and zorg_page_path_str in old_error_files
        ):
            c.zprint(
                "PREVIOUSLY BROKEN ZORG FILE HAS BEEN FIXED!",
                zorg_page_path_str,
                fg_color=Color.WHITE,
                bg_color=Color.GREEN,
            )

    _LOGGER.info(
        "Finished reading zettel org directory",
        good_files=len(zorg_pages) - len(error_files),
        bad_files=len(error_files),
        notes=total_num_notes,
    )
    file_hash_path = _get_file_hash_path(cmd.zettel_dir)
    file_to_hash = _get_file_hash_map(cmd.zettel_dir)
    _write_file_hash_to_disk(file_hash_path, file_to_hash)
    error_file_whitelist.write_text("\n".join(sorted(error_files)))
    session.commit()


def reindex_database(
    cmd: commands.ReindexDBCommand, session: SQLSession
) -> None:
    """Reindex an existing zorg database."""
    file_to_hash = _get_file_hash_map(
        cmd.zettel_dir, paths=cmd.paths if cmd.paths else None
    )
    file_hash_path = _get_file_hash_path(cmd.zettel_dir)
    old_file_to_hash: dict[str, str] = (
        json.loads(file_hash_path.read_bytes())
        if file_hash_path.exists()
        else {}
    )

    error_file_whitelist = _get_error_file_whitelist(cmd.zettel_dir)
    error_files = error_file_whitelist.read_text().split("\n")

    num_of_updates = 0
    for zorg_page_name, hash_ in file_to_hash.copy().items():
        # If this file has never been indexed OR the file contents have changed
        # since the last time it was indexed.
        if (
            zorg_page_name not in old_file_to_hash.keys()
            or old_file_to_hash[zorg_page_name] != hash_
        ):
            num_of_updates += 1
            old_zorg_page = session.repo.remove_file_by_name(zorg_page_name)
            if old_zorg_page is not None:
                _LOGGER.debug("Removing file from DB", file=zorg_page_name)
                c.zprint(
                    "UPDATING EXISTING FILE",
                    zorg_page_name,
                    fg_color=Color.BLACK,
                    bg_color=Color.YELLOW,
                )
            else:
                c.zprint(
                    "ADDING NEW FILE",
                    zorg_page_name,
                    fg_color=Color.WHITE,
                    bg_color=Color.GREEN,
                )

            zorg_page = walk_zorg_page(
                cmd.zettel_dir, Path(zorg_page_name), verbose=cmd.verbose
            )
            zorg_page_path_str = c.strip_zdir(cmd.zettel_dir, zorg_page.path)
            if not zorg_page.has_errors and zorg_page_path_str in error_files:
                c.zprint(
                    "PREVIOUSLY BROKEN ZORG FILE HAS BEEN FIXED!",
                    zorg_page_path_str,
                    fg_color=Color.WHITE,
                    bg_color=Color.GREEN,
                )
                error_files.remove(zorg_page_path_str)
            elif (
                zorg_page.has_errors and zorg_page_path_str not in error_files
            ):
                raise RuntimeError(f"Zorg file has errors!: {zorg_page.path}")

            _check_for_modified_notes(cmd.zettel_dir, zorg_page, old_zorg_page)
            _LOGGER.debug("Adding zorg file", file=zorg_page_name)
            session.repo.add_file(zorg_page)
            session.commit()

    if num_of_updates == 0:
        c.zprint("NO ZORG FILES HAVE BEEN MODIFIED")

    _write_file_hash_to_disk(file_hash_path, file_to_hash)
    error_file_whitelist.write_text("\n".join(sorted(error_files)))
    session.commit()


def reindex_database_after_edit(
    event: events.EditorClosedEvent, session: SQLSession
) -> None:
    """Reindex the zorg database after an edit."""
    session.add_message(
        commands.ReindexDBCommand(event.edit_cmd.zettel_dir, paths=[])
    )


def add_zids_to_notes_in_file(
    event: events.NewZorgNotesEvent, session: SQLSession
) -> None:
    """Adds ZIDs to new zorg notes."""
    del session

    _update_zo_file(
        zdir=event.zettel_dir,
        zo_path=event.zorg_page_path,
        notes_to_update=event.new_notes,
        add_thing_to_first_line=_add_zid_to_line,
        get_thing=attrgetter("zid"),
        log_message="Adding ZIDs to zorg file",
    )


def update_note_modify_dates(
    event: events.ModifiedZorgNotesEvent, session: SQLSession
) -> None:
    """Creates or updates note modify dates."""
    del session
    today_short_date = zdt.to_short_date_spec(dt.date.today())
    _update_zo_file(
        zdir=event.zettel_dir,
        zo_path=event.zorg_page_path,
        notes_to_update=event.modified_notes,
        add_thing_to_first_line=_add_or_update_modify_date,
        get_thing=lambda _: today_short_date,
        log_message="Updating modify dates",
    )


def _get_zo_paths_to_index(zdir: Path) -> list[Path]:
    return sorted(zdir.rglob("*.zo"), key=lambda p: p.name)


def _get_file_hash_map(
    zdir: Path, *, paths: Iterable[Path] = None
) -> dict[str, str]:
    if paths is None:
        paths = _get_zo_paths_to_index(zdir)
    file_to_hash: dict[str, str] = {}
    for path in paths:
        key = c.strip_zdir(zdir, path)
        file_to_hash[key] = _hash_file(path)
    return file_to_hash


def _get_file_hash_path(zdir: Path) -> Path:
    zorg_data_dir = _get_data_dir(zdir)
    return zorg_data_dir / "file_hash.json"


def _get_error_file_whitelist(zdir: Path) -> Path:
    zorg_data_dir = _get_data_dir(zdir)
    error_file_whitelist = zorg_data_dir / "error_file_whitelist.txt"
    error_file_whitelist.touch()
    return error_file_whitelist


def _get_data_dir(zdir: Path) -> Path:
    zorg_data_dir = zdir / f".{APP_NAME}"
    zorg_data_dir.mkdir(parents=True, exist_ok=True)
    return zorg_data_dir


def _write_file_hash_to_disk(
    file_hash_path: Path, file_to_hash: dict[str, str]
) -> None:
    _LOGGER.debug("Writing hash map to disk", file=str(file_hash_path))
    with file_hash_path.open("w") as f:
        json.dump(dict(sorted(file_to_hash.items())), f, indent=4)


def _add_zid_to_line(zid: str, line: str) -> str:
    words = line.split(" ")
    line_before_zid = _pop_line_before_zid(words)

    # Remove a YYYY-MM-DD create date if one existed prior to adding a ZID to
    # the note.
    if len(words[0]) == 10:
        dash_idices = (4, 7)
        for i, ch in enumerate(words[0][:10]):
            if i not in dash_idices and not ch.isdigit():
                break
        else:
            words.pop(0)

    return f"{line_before_zid}{zid} {' '.join(words)}"


def _hash_file(filepath: Path, chunk_size: int = 8192) -> str:
    """Hashes a file using SHA256 algorithm and returns the hash value.

    Arguments:
    ----------
    filepath: Path to the file to be hashed.
    chunk_size: Size of chunks to read the file. Default is 8192 bytes.

    Return:
    -------
    A SHA256 hash of the file's contents.
    """
    hasher = hashlib.sha256()  # Initialize the hasher
    with filepath.open("rb") as file:
        while chunk := file.read(chunk_size):
            hasher.update(chunk)
    return hasher.hexdigest()


def _process_vim_commands(
    zettel_dir: Path, vim_commands: Iterable[str]
) -> Iterator[str]:
    for vim_cmd in vim_commands:
        if "{zdir}" in vim_cmd:
            yield vim_cmd.format(zdir=zettel_dir)
        else:
            yield vim_cmd


def _check_for_modified_notes(
    zdir: Path, zorg_page: Page, old_zorg_page: Optional[Page]
) -> None:
    today = dt.date.today()
    modified_notes: list[Note] = []
    notes = old_zorg_page.notes if old_zorg_page else []
    old_zid_map = {note.zid: note for note in notes if note.zid is not None}
    for note in zorg_page.notes:
        old_note = old_zid_map.get(note.zid, None) if note.zid else None
        note_has_changed = old_note and note != old_note
        if note.modify_date != today and note_has_changed:
            note.modify_date = today
            modify_short_date = zdt.to_short_date_spec(dt.date.today())
            # If the modify date is the same as the create date, then no modify
            # date spec should exist yet...
            assert old_note is not None
            if old_note.modify_date == note.create_date:
                old_body = f"{note.body.lstrip()}"
            # Otherwise, we need to remove the old modify date spec before
            # adding the new one.
            else:
                old_body = " ".join(note.body.lstrip().split(" ")[1:])
            note.body = f"{modify_short_date} {old_body}"
            modified_notes.append(note)
    if modified_notes:
        zorg_page.events.append(
            events.ModifiedZorgNotesEvent(zdir, zorg_page.path, modified_notes)
        )


def _add_or_update_modify_date(short_modify_date: str, line: str) -> str:
    words = line.split(" ")
    line_before_zid = _pop_line_before_zid(words)
    if words and len(words[0]) == 6 and all(ch.isdigit() for ch in words[0]):
        old_modify_date = words.pop(0)
        _LOGGER.debug(
            "Removing old modify date", old_modify_date=old_modify_date
        )
    return f"{line_before_zid}{short_modify_date} {' '.join(words)}"


def _pop_line_before_zid(words: list[str]) -> str:
    num_spaces = 0
    while words[0] == "":
        num_spaces += 1
        words.pop(0)
    spaces = " " * num_spaces

    symbol = words.pop(0)

    priority = ""
    if len(words[0]) == 2 and words[0][0] == "P" and words[0][1].isdigit():
        priority = f"{words.pop(0)} "
    return f"{spaces}{symbol} {priority}"


def _update_zo_file(
    *,
    zdir: Path,
    zo_path: Path,
    notes_to_update: Sequence[Note],
    add_thing_to_first_line: _AddThingToFirstLine,
    get_thing: _GetThing,
    log_message: str,
) -> None:
    zlines = zo_path.read_text().split("\n")
    for note in notes_to_update:
        assert note.zid is not None
        assert note.line_no is not None

        start_idx = note.line_no - 1
        end_idx = note.line_no + len(note.body.split("\n")) - 1
        new_note_lines = zlines[start_idx:end_idx]
        first_note_line = new_note_lines[0]
        new_note_lines[0] = add_thing_to_first_line(
            get_thing(note), first_note_line
        )
        zlines = zlines[:start_idx] + new_note_lines + zlines[end_idx:]

    _LOGGER.info(
        log_message,
        zorg_page=str(zo_path),
        notes_to_update=len(notes_to_update),
    )
    zo_path.write_text("\n".join(zlines))

    _write_file_hash_to_disk(
        _get_file_hash_path(zdir), _get_file_hash_map(zdir)
    )
