"""Zorg events."""

from dataclasses import dataclass
from pathlib import Path

from . import commands
from ..models import ZorgNote


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

    zorg_file_path: Path
    new_notes: list[ZorgNote]


@dataclass(frozen=True)
class DBModifiedEvent(Event):
    """Broadcast when the zorg database is done being initialized."""

    zettel_dir: Path
