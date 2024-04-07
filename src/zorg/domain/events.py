"""Zorg events."""

from dataclasses import dataclass

from . import commands
from .types import Message


@dataclass(frozen=True)
class Event(Message):
    """A zorg event."""


@dataclass(frozen=True)
class EditorClosedEvent(Event):
    """Broadcast when the user closes their editor."""

    # The EditCommand that caused the editor to open in the first place.
    edit_cmd: commands.EditCommand


@dataclass(frozen=True)
class NewZorgNotesEvent(Event):
    """This zorg event is broadcast when new zorg notes are indexed."""
