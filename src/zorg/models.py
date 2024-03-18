"""This file contains Zorg's domain model classes."""

from dataclasses import dataclass, field
import datetime as dt
from pathlib import Path
from typing import Optional

from .types import TodoPriorityType, TodoStatus


@dataclass(frozen=True)
class Note:
    """A Zorg note."""

    body: str
    file: Path

    child_notes: list["Note"] = field(default_factory=lambda: [])
    context_tags: list[str] = field(default_factory=lambda: [])
    create_date: dt.date = dt.date.today()
    next_note: Optional["Note"] = None
    parent_note: Optional["Note"] = None
    people_tags: list[str] = field(default_factory=lambda: [])
    prev_note: Optional["Note"] = None
    project_tags: list[str] = field(default_factory=lambda: [])
    properties: dict[str, str] = field(default_factory=lambda: {})
    role_tags: list[str] = field(default_factory=lambda: [])


@dataclass(frozen=True)
class Todo(Note):
    """A Zorg todo."""

    done_date: Optional[dt.date] = None
    priority: TodoPriorityType = 'C'
    status: TodoStatus = TodoStatus.OPEN

@dataclass(frozen=True)
class ZorgFile:
    """A Zorg (i.e. *.zo) file."""
