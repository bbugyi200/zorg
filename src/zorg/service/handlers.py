"""Zorg's event and command handlers live here."""

from functools import partial
import hashlib
import json
from pathlib import Path
import sys
from typing import Iterable, Iterator

from logrus import Logger
from tqdm import tqdm
import vimala

from . import common
from .. import APP_NAME
from ..domain.messages import commands, events
from ..storage.sql.session import SQLSession
from .compiler import walk_zorg_file
from .zid_manager import ZIDManager


logger = Logger(__name__)


def edit_files(cmd: commands.EditCommand, session: SQLSession) -> None:
    """Command handler for the EditCommand."""
    vimala.vim(
        *cmd.paths,
        commands=_process_vim_commands(cmd.zettel_dir, cmd.vim_commands),
    ).unwrap()
    session.add_message(events.EditorClosedEvent(edit_cmd=cmd))


def check_keep_alive_file(
    event: events.EditorClosedEvent, session: SQLSession
) -> None:
    """Check if the 'keep alive' file exists and, if so, reopens the editor."""
    keep_alive_file = event.edit_cmd.keep_alive_file
    if not keep_alive_file.exists():
        logger.debug(
            "No keep alive file found.",
            keep_alive_file=keep_alive_file,
        )
        return

    zdir = event.edit_cmd.zettel_dir
    prepend_zdir = partial(common.prepend_zdir, zdir)
    vim_commands = list(event.edit_cmd.vim_commands)
    if keep_alive_file.stat().st_size == 0:
        logger.debug(
            "Empty keep alive file found.",
            keep_alive_file=keep_alive_file,
        )
        paths = event.edit_cmd.paths
    else:
        keep_alive_lines = list(keep_alive_file.read_text().split())
        focused_filename = keep_alive_lines.pop()
        vim_commands = [
            cmd for cmd in vim_commands if not cmd.startswith("edit")
        ]
        vim_commands.append(f"edit {focused_filename}")
        new_paths = prepend_zdir([Path(p.strip()) for p in keep_alive_lines])
        logger.debug(
            "Editing files specified in the keep alive file.",
            keep_alive_file=keep_alive_file,
            old_paths=event.edit_cmd.paths,
            new_paths=new_paths,
        )
        paths = new_paths

    verbose = event.edit_cmd.verbose
    if verbose <= 1:
        logger.debug(
            "Unlinking keep-alive file", keep_alive_file=keep_alive_file
        )
        keep_alive_file.unlink()
    else:
        logger.debug(
            "We are NOT deleting the keep-alive file",
            keep_alive_file=keep_alive_file,
        )
    session.add_last_message(
        commands.EditCommand(
            zettel_dir=zdir,
            paths=paths,
            keep_alive_file=keep_alive_file,
            verbose=verbose,
            vim_commands=vim_commands,
        )
    )


def create_database(
    cmd: commands.CreateDBCommand, session: SQLSession
) -> None:
    """Create a new zorg DB from scratch."""
    zorg_files = []
    total_num_notes = 0
    total_num_todos = 0
    for zo_path in tqdm(
        sorted(cmd.zettel_dir.rglob("*.zo"), key=lambda p: p.name),
        desc="Reading notes from zorg files",
        file=sys.stdout,
    ):
        logger.info("Starting to walk zorg file", zorg_file=zo_path.name)
        zorg_file = walk_zorg_file(cmd.zettel_dir, zo_path)
        num_notes = len(zorg_file.notes)
        num_todos = len(
            [note for note in zorg_file.notes if note.todo_payload]
        )
        total_num_notes += num_notes
        total_num_todos += num_todos
        logger.info(
            "Finished walking zorg file",
            zorg_file=zo_path.name,
            num_notes=num_notes,
            num_todos=num_todos,
            total_num_notes=total_num_notes,
            total_num_todos=total_num_todos,
        )
        session.repo.add(zorg_file)
        zorg_files.append(zorg_file)
    logger.info(
        "Finished reading zettel org directory",
        num_files=len(zorg_files),
        num_notes=total_num_notes,
        num_todos=total_num_todos,
    )
    session.commit()
    session.add_message(events.DBModifiedEvent(cmd.zettel_dir))


def reindex_database(
    cmd: commands.ReindexDBCommand, session: SQLSession
) -> None:
    """Reindex an existing zorg database."""
    paths = cmd.paths if cmd.paths else sorted(cmd.zettel_dir.rglob("*.zo"))
    file_to_hash: dict[str, str] = {}
    for path in paths:
        key = common.strip_zdir(cmd.zettel_dir, path)
        file_to_hash[key] = _hash_file(path)

    zorg_data_dir = cmd.zettel_dir / f".{APP_NAME}"
    zorg_data_dir.mkdir(parents=True, exist_ok=True)
    file_hash_path = zorg_data_dir / "file_hash.json"
    old_file_to_hash: dict[str, str] = (
        json.loads(file_hash_path.read_bytes())
        if file_hash_path.exists()
        else {}
    )

    for file, hash_ in file_to_hash.copy().items():
        if (
            file not in old_file_to_hash.keys()
            or old_file_to_hash[file] != hash_
        ):
            logger.info("Changed file", file=file)
            old_zorg_file = session.repo.get(file).unwrap()
            if old_zorg_file is not None:
                logger.info("Removing file from DB", file=file)
                session.repo.remove_by_key(str(old_zorg_file.path))

            zorg_file = walk_zorg_file(
                cmd.zettel_dir, Path(file), verbose=cmd.verbose
            )
            logger.info("Adding zorg file", file=file)
            session.repo.add(zorg_file)

    logger.debug("Writing hash map to disk", file=str(file_hash_path))
    with file_hash_path.open("w") as f:
        json.dump(dict(sorted(file_to_hash.items())), f, indent=4)

    session.commit()
    session.add_message(events.DBModifiedEvent(cmd.zettel_dir))


def reindex_database_after_edit(
    event: events.EditorClosedEvent, session: SQLSession
) -> None:
    """Reindex the zorg database after an edi."""
    session.add_message(
        commands.ReindexDBCommand(event.edit_cmd.zettel_dir, paths=[])
    )


def add_zids_to_notes_in_file(
    event: events.NewZorgNotesEvent, session: SQLSession
) -> None:
    """Adds IDs to new zorg notes."""
    del session

    zlines = event.zorg_file_path.read_text().split("\n")
    for note in event.new_notes:
        assert note.zid is not None
        assert note.line_no is not None

        start_idx = note.line_no - 1
        end_idx = note.line_no + len(note.body.split("\n")) - 1
        new_note_lines = zlines[start_idx:end_idx]
        first_note_line = new_note_lines[0]
        new_note_lines[0] = _add_zid_to_line(note.zid, first_note_line)
        zlines = zlines[:start_idx] + new_note_lines + zlines[end_idx:]

    logger.info(
        "Adding ZIDs to zorg file",
        zorg_file=event.zorg_file_path,
        new_notes=len(event.new_notes),
    )
    event.zorg_file_path.write_text("\n".join(zlines))


def increment_zid_counters(
    event: events.DBModifiedEvent, session: SQLSession
) -> None:
    """Increment the date-specific zorg ID counters.

    These are stored in a directory in your zettel dir and are used when
    generating new IDs (they are the XX in the YYMMDD#XX ID format).
    """
    del session
    zid_manager = ZIDManager(event.zettel_dir)
    zid_manager.write_to_disk()


def _add_zid_to_line(zid: str, line: str) -> str:
    all_words = line.split(" ")

    num_spaces = 0
    while all_words[0] == "":
        num_spaces += 1
        all_words.pop(0)
    spaces = " " * num_spaces

    symbol = all_words[0]
    words = all_words[1:]

    priority = ""
    if words[0].startswith("[#"):
        priority = f"{words.pop(0)} "

    if len(words[0]) == 10:
        dash_idices = (4, 7)
        for i, ch in enumerate(words[0][:10]):
            if i not in dash_idices and not ch.isdigit():
                break
        else:
            words.pop(0)

    return f"{spaces}{symbol} {priority}{zid} {' '.join(words)}"


def _hash_file(filepath: Path, chunk_size: int = 8192) -> str:
    """Hashes a file using SHA256 algorithm and returns the hash value.

    Args:
        filepath: Path to the file to be hashed.
        chunk_size: Size of chunks to read the file. Default is 8192 bytes.

    Returns:
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
