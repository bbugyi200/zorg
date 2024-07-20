"""Zorg events."""

from dataclasses import dataclass
from pathlib import Path

from zorg.domain.messages import commands
from zorg.domain.models import Note


@dataclass(frozen=True)
class Event:
    """A zorg event."""


@dataclass(frozen=True)
class EditorClosedEvent(Event):
    """Broadcast when the user closes their editor."""

    # The EditCommand that caused the editor to open in the first place.
    edit_cmd: commands.EditCommand


@dataclass(frozen=True)
class NewZorgNotesEvent(Event):
    """Broadcast when new zorg notes are indexed."""

    zettel_dir: Path
    zorg_page_path: Path
    new_notes: list[Note]


@dataclass(frozen=True)
class ModifiedZorgNotesEvent(Event):
    """Broadcast when zorg notes should have their modify date updated."""

    zettel_dir: Path
    zorg_page_path: Path
    modified_notes: list[Note]
