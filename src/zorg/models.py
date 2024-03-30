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


@dataclass
class ZorgNote:
    """A Zorg note."""

    body: str

    areas: list[str] = field(default_factory=lambda: [])
    child_note_ids: list[int] = field(default_factory=lambda: [])
    contexts: list[str] = field(default_factory=lambda: [])
    create_date: dt.date = field(default_factory=dt.date.today)
    ident: Optional[int] = None
    links: list[str] = field(default_factory=lambda: [])
    next_note_id: Optional[int] = None
    parent_note_id: Optional[int] = None
    people: list[str] = field(default_factory=lambda: [])
    prev_note_id: Optional[int] = None
    projects: list[str] = field(default_factory=lambda: [])
    properties: dict[str, str] = field(default_factory=lambda: {})


@dataclass
class ZorgTodo(ZorgNote):
    """A Zorg todo."""

    done_date: Optional[dt.date] = None
    priority: TodoPriorityType = "C"
    status: TodoStatus = TodoStatus.OPEN
