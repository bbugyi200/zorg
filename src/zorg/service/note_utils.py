"""Miscellaneous utilities for working with Notes live here."""

from zorg.domain.models import Note
from zorg.domain.types import DoneTodoTypeChar


def note_body_has_tag(note_body: str, tag: str) -> bool:
    """Returns True iff {note} contains {tag} in its body."""
    for note_word in note_body.split():
        if tag == note_word.rstrip("),.?!;:").lstrip("("):
            return True
    return False


def to_done_note(note: Note, done_type: DoneTodoTypeChar) -> Note:
    """TODO.

    Arguments:
    ----------
    note: TODO
    done_type: TODO

    Return:
    -------
    TODO
    """
