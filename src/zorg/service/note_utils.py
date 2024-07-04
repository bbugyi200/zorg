"""Miscellaneous utilities for working with Notes live here."""


def note_body_has_tag(note_body: str, tag: str) -> bool:
    """Returns True iff {note} contains {tag} in its body."""
    for note_word in note_body.split():
        if tag == note_word.rstrip("),.?!;:").lstrip("("):
            return True
    return False
