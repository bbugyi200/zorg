"""This file contains Zorg's domain model classes."""

from dataclasses import dataclass, field
import datetime as dt
from pathlib import Path
from typing import TYPE_CHECKING, Optional

from ..types import NoteType, TodoPriorityType


if TYPE_CHECKING:
    from ..messages.events import Event


@dataclass(frozen=True)
class TodoPayload:
    """Extra fields that are added to ZorgNotes that are todos."""

    priority: TodoPriorityType = "P2"
    status: NoteType = NoteType.OPEN_TODO


@dataclass
class Note:
    """A Zorg note."""

    body: str
    file_path: Path
    line_no: int

    areas: list[str] = field(default_factory=lambda: [])
    contexts: list[str] = field(default_factory=lambda: [])
    create_date: dt.date = field(default_factory=dt.date.today)
    links: list[str] = field(default_factory=lambda: [])
    modify_date: dt.date = field(default_factory=dt.date.today)
    people: list[str] = field(default_factory=lambda: [])
    projects: list[str] = field(default_factory=lambda: [])
    properties: dict[str, str] = field(default_factory=lambda: {})
    todo_payload: Optional[TodoPayload] = None
    zid: Optional[str] = None

    def __eq__(self, other: object) -> bool:  # noqa: D105
        return (
            isinstance(other, Note)
            and self.body == other.body
            and self.todo_payload == other.todo_payload
        )

    def to_string(self) -> str:
        """Convert a Note to a string that can be stored in a *.zo file."""
        note_type = (
            self.todo_payload.status if self.todo_payload else NoteType.BASIC
        )
        char = note_type.to_prefix_char()
        priority = (
            f" {self.todo_payload.priority}"
            if self.todo_payload
            and self.todo_payload.status
            not in [NoteType.CLOSED_TODO, NoteType.CANCELED_TODO]
            else ""
        )
        return f"{char}{priority} {self.body.strip()}\n"


@dataclass
class File:
    """A Zorg (i.e. *.zo) file."""

    path: Path
    has_errors: bool = False
    notes: list[Note] = field(default_factory=list)
    events: list["Event"] = field(default_factory=list)
