"""This file contains Zorg's domain model classes."""

from dataclasses import dataclass, field
import datetime as dt
from typing import Optional

from .types import TodoPriorityType, TodoStatus


@dataclass(frozen=True)
class ZorgFile:
    """A Zorg (i.e. *.zo) file."""

    notes: list["ZorgNote"]
    todos: list["ZorgTodo"]


@dataclass(frozen=True)
class ZorgNote:
    """A Zorg note."""

    body: str
    file: ZorgFile

    child_notes: list["ZorgNote"] = field(default_factory=lambda: [])
    context_tags: list[str] = field(default_factory=lambda: [])
    create_date: dt.date = dt.date.today()
    next_note: Optional["ZorgNote"] = None
    parent_note: Optional["ZorgNote"] = None
    people_tags: list[str] = field(default_factory=lambda: [])
    prev_note: Optional["ZorgNote"] = None
    project_tags: list[str] = field(default_factory=lambda: [])
    properties: dict[str, str] = field(default_factory=lambda: {})
    role_tags: list[str] = field(default_factory=lambda: [])


@dataclass(frozen=True)
class ZorgTodo(ZorgNote):
    """A Zorg todo."""

    done_date: Optional[dt.date] = None
    priority: TodoPriorityType = 'C'
    status: TodoStatus = TodoStatus.OPEN
