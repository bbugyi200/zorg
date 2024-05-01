"""This file contains Zorg's domain model classes."""

from dataclasses import dataclass, field
import datetime as dt
from pathlib import Path
from typing import TYPE_CHECKING, Optional

from ..types import NoteStatus, TodoPriorityType


if TYPE_CHECKING:
    from ..messages.events import Event


@dataclass(frozen=True)
class TodoPayload:
    """Extra fields that are added to ZorgNotes that are todos."""

    priority: TodoPriorityType = "C"
    status: NoteStatus = NoteStatus.OPEN_TODO


@dataclass
class ZorgNote:
    """A Zorg note."""

    body: str

    areas: list[str] = field(default_factory=lambda: [])
    child_note_ids: list[int] = field(default_factory=lambda: [])
    contexts: list[str] = field(default_factory=lambda: [])
    create_date: dt.date = field(default_factory=dt.date.today)
    line_no: Optional[int] = None
    links: list[str] = field(default_factory=lambda: [])
    next_note_id: Optional[int] = None
    parent_note_id: Optional[int] = None
    people: list[str] = field(default_factory=lambda: [])
    prev_note_id: Optional[int] = None
    projects: list[str] = field(default_factory=lambda: [])
    properties: dict[str, str] = field(default_factory=lambda: {})
    todo_payload: Optional[TodoPayload] = None
    zid: Optional[str] = None


@dataclass
class ZorgFile:
    """A Zorg (i.e. *.zo) file."""

    path: Path
    has_errors: bool = False
    notes: list[ZorgNote] = field(default_factory=list)
    events: list["Event"] = field(default_factory=list)
