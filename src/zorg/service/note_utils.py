"""Miscellaneous utilities for working with Notes live here."""

from dataclasses import dataclass, replace

from zorg.domain.models import Note, TodoPayload
from zorg.domain.types import (
    cast_tag_name,
    DoneTodoTypeChar,
    MetadataType,
    NoteType,
)


def to_done_note(note: Note, done_type: DoneTodoTypeChar) -> Note:
    """Changes the note type of {note} to {done_type}."""
    new_note = replace(note)
    new_note.todo_payload = TodoPayload(status=NoteType(done_type))
    return new_note


def add_hidden_metadata(note: Note) -> Note:
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


@dataclass(frozen=True)
class _MetadataMutate:
    """Mutates a tag/link."""

    mtype: MetadataType
    value: str


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
