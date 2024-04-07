"""Zorg events."""

from dataclasses import dataclass

from .types import Message


@dataclass(frozen=True)
class Event(Message):
    """A zorg event."""


@dataclass(frozen=True)
class NewZorgNotesEvent(Event):
    """This zorg event is broadcast when new zorg notes are indexed."""
