"""This file contains Zorg's domain model classes."""

from dataclasses import dataclass, field
import datetime as dt
from pathlib import Path
from typing import Optional

from .types import TodoPriorityType, TodoStatus


@dataclass(frozen=True)
class ZorgFile:
    """A Zorg (i.e. *.zo) file."""

    path: Path
    notes: list["ZorgNote"] = field(default_factory=lambda: [])
    todos: list["ZorgTodo"] = field(default_factory=lambda: [])


@dataclass(frozen=True)
class ZorgNote:
    """A Zorg note."""

    body: str

    areas: list[str] = field(default_factory=lambda: [])
    child_notes: list["ZorgNote"] = field(default_factory=lambda: [])
    contexts: list[str] = field(default_factory=lambda: [])
    create_date: dt.date = field(default_factory=dt.date.today)
    next_note: Optional["ZorgNote"] = None
    parent_note: Optional["ZorgNote"] = None
    people: list[str] = field(default_factory=lambda: [])
    prev_note: Optional["ZorgNote"] = None
    projects: list[str] = field(default_factory=lambda: [])
    properties: dict[str, str] = field(default_factory=lambda: {})


@dataclass(frozen=True)
class ZorgTodo(ZorgNote):
    """A Zorg todo."""

    done_date: Optional[dt.date] = None
    priority: TodoPriorityType = "C"
    status: TodoStatus = TodoStatus.OPEN
