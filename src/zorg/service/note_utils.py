"""Miscellaneous utilities for working with Notes live here."""

from dataclasses import dataclass, replace
from pathlib import Path
from typing import Final, Optional

from logrus import Logger
from typist import PathLike

from zorg.domain.models import Note, Page, TodoPayload
from zorg.domain.types import (
    DoneTodoTypeChar,
    MetadataType,
    NoteType,
    TemplatePatternMapType,
    cast_tag_name,
)
from zorg.service.templates import init_from_template
from zorg.shared import common as c
from zorg.storage.file import FileManager
from zorg.storage.sql import SQLSession


_LOGGER: Final = Logger(__name__)


def convert_note_to_page(
    zdir: PathLike,
    db_url: str,
    note: Note,
    new_page_name: str,
    parent_page_name: str,
) -> Page:
    """Converts a Note into a Page."""
    del db_url, note, parent_page_name

    zdir = Path(zdir)
    new_page_path = c.prepend_zdir(zdir, new_page_name)

    # Create new <ZO_PAGE> and add a related file link (key: ^) to the page
    # header.
    pass  # pylint: disable=unnecessary-pass

    # Determine the next available related file link <KEY> from the parent
    # page.
    pass  # pylint: disable=unnecessary-pass

    # Add a new related file link using <KEY> to the parent page.
    pass  # pylint: disable=unnecessary-pass

    # Get a list of all L1 <BULLETS> from the target note and filter any
    # property bullets from this list.
    pass  # pylint: disable=unnecessary-pass

    # Add <BULLETS> to <ZO_PAGE> as notes.
    pass  # pylint: disable=unnecessary-pass

    # Get a list (<INLINE_PROPS>) of all properties that can be inlined via the
    # [foo::bar] syntax. Include CDATE:: and MDATE:: properties in this list.
    pass  # pylint: disable=unnecessary-pass

    # Add <INLINE_PROPS> to <ZO_PAGE>'s header.
    pass  # pylint: disable=unnecessary-pass

    # Get a list (<BULLET_PROPS>) of all properties that contain spaces.
    pass  # pylint: disable=unnecessary-pass

    # Add <BULLET_PROPS> to <ZO_PAGE>'s header.
    pass  # pylint: disable=unnecessary-pass

    # Replace all instances of [#<new_page_name>] or [<note.zid>] with
    # [[<new_page_name>]].
    pass  # pylint: disable=unnecessary-pass

    # Delete the newly promoted note from the page it used to be contained in.
    pass  # pylint: disable=unnecessary-pass

    return Page(new_page_path)


def move_note(
    zdir: PathLike,
    db_url: str,
    template_pattern_map: TemplatePatternMapType,
    *,
    zid: str,
    new_page: PathLike,
    note_type: Optional[DoneTodoTypeChar],
    verbose: int = 0,
) -> int:
    """Move note associated with {zid} to {new_page}."""
    zdir = Path(zdir)
    new_page = Path(new_page)
    with SQLSession(zdir, db_url, verbose=verbose) as session:
        return _move_note(
            new_page=new_page,
            note_type=note_type,
            session=session,
            template_pattern_map=template_pattern_map,
            zid=zid,
        )


def get_notes_by_id(
    zdir: PathLike,
    db_url: str,
    id_: str,
    *,
    id_key: str = "ID",
    verbose: int = 0,
) -> list[Note]:
    """Fetch a list of notes using an id:: property."""
    zdir = Path(zdir)
    with SQLSession(zdir, db_url, verbose=verbose) as session:
        return session.repo.get_notes_by_id(id_, id_key=id_key)


def get_note_by_zid(
    zdir: PathLike, db_url: str, zid: str, *, verbose: int = 0
) -> Optional[Note]:
    """Fetch a single note using its unique ZID."""
    zdir = Path(zdir)
    with SQLSession(zdir, db_url, verbose=verbose) as session:
        return session.repo.get_note_by_zid(zid)


@dataclass(frozen=True)
class _MetadataMutate:
    """Mutates a tag/link."""

    mtype: MetadataType
    value: str


def _move_note(
    *,
    new_page: Path,
    note_type: Optional[DoneTodoTypeChar],
    session: SQLSession,
    template_pattern_map: TemplatePatternMapType,
    zid: str,
) -> int:
    note = session.repo.get_note_by_zid(zid)

    if note is None:
        _LOGGER.error("No Zorg note with the given ZID", zid=zid)
        return 1

    _LOGGER.debug(
        f"Note with ZID={zid} found | {str(note.file_path)}::{note.line_no}"
    )

    new_note = note
    if note_type is not None:
        new_note = _to_done_note(new_note, note_type)
    new_note = _add_hidden_metadata(new_note)

    if not new_page.exists():
        init_from_template(session.zdir, template_pattern_map, new_page)

    file_man = FileManager(session.zdir)
    if error := file_man.add_note(new_note, new_page):
        _LOGGER.error("Failed to add note to page", error=f"'{error.upper()}'")
        return 1

    if error := file_man.delete_note(note):
        _LOGGER.error(
            "Failed to delete note from page", error=f"'{error.upper()}'"
        )
        return 1
    return 0


def _to_done_note(note: Note, done_type: DoneTodoTypeChar) -> Note:
    """Changes the note type of {note} to {done_type}."""
    new_note = replace(note)
    new_note.todo_payload = TodoPayload(status=NoteType(done_type))
    return new_note


def _add_hidden_metadata(note: Note) -> Note:
    """Modifies the body of {note} by adding hidden metadata to it."""
    new_note = replace(note)
    extra_tags = ""
    for mdata_mutate in _get_hidden_metadata_mutates(note):
        prefix_chars: str = ""
        suffix_chars: str = ""
        mtype = mdata_mutate.mtype
        if mtype == "areas":
            prefix_chars = "#"
        elif mtype == "contexts":
            prefix_chars = "@"
        elif mtype == "projects":
            prefix_chars = "+"
        elif mtype == "people":
            prefix_chars = "%"
        elif mtype == "links":
            prefix_chars = "[["
            suffix_chars = "]]"
        elif mtype == "properties":
            pass
        extra_tags += f" {prefix_chars}{mdata_mutate.value}{suffix_chars}"

    if extra_tags != "":
        assert new_note.zid is not None
        new_note.body = new_note.body.replace(
            new_note.zid, f"{new_note.zid}{extra_tags}"
        )
    return new_note


def _get_hidden_metadata_mutates(note: Note) -> list[_MetadataMutate]:
    metadata_mutates = []
    for ch, tag_name, tags in [
        ("+", cast_tag_name("projects"), note.projects),
        ("#", cast_tag_name("areas"), note.areas),
        ("@", cast_tag_name("contexts"), note.contexts),
        ("%", cast_tag_name("people"), note.people),
    ]:
        for tag in sorted(tags):
            tag_word = f"{ch}{tag}"
            if not _note_body_has_tag(note.body, tag_word):
                metadata_mutates.append(
                    _MetadataMutate(mtype=tag_name, value=tag)
                )

    for key, value in sorted(note.properties.items()):
        prop_value = f"{key}::{value}"
        if f"{key}::" not in note.body:
            metadata_mutates.append(
                _MetadataMutate(mtype="properties", value=prop_value)
            )
    return metadata_mutates


def _note_body_has_tag(note_body: str, tag: str) -> bool:
    """Returns True iff {note} contains {tag} in its body."""
    for note_word in note_body.split():
        if tag == note_word.rstrip("),.?!;:").lstrip("("):
            return True
    return False
