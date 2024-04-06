"""Zorg events."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Event:
    """A zorg event."""
