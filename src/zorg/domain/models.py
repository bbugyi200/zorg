"""This file contains Zorg's domain model classes."""

from dataclasses import dataclass, field
import datetime as dt
from pathlib import Path
from typing import TYPE_CHECKING, Iterable, Optional

from .types import (
    DescOperator,
    PropertyOperator,
    PropertyValueType,
    TodoPriorityType,
    TodoStatus,
)


if TYPE_CHECKING:
    from .messages.events import Event


@dataclass(frozen=True)
class TodoPayload:
    """Extra fields that are added to ZorgNotes that are todos."""

    priority: TodoPriorityType = "C"
    status: TodoStatus = TodoStatus.OPEN


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
    notes: list[ZorgNote] = field(default_factory=lambda: [])
    events: list["Event"] = field(default_factory=lambda: [])


@dataclass(frozen=True)
class DescFilter:
    """Represents a description query filter (e.g. '"foo"' or '!"bar"')."""

    value: str
    case_sensitive: Optional[bool] = None
    op: DescOperator = DescOperator.CONTAINS


@dataclass(frozen=True)
class PropertyFilter:
    """Represents a single property filter (e.g. 'due<=0d' or '!recur')."""

    key: str
    value: str = ""
    op: PropertyOperator = PropertyOperator.EXISTS
    value_type: PropertyValueType = PropertyValueType.STRING


@dataclass(frozen=True)
class DateRange:
    """Represents a range of dates."""

    start: dt.date
    end: Optional[dt.date] = None


@dataclass
class AndZorgQuery:
    """Tag used to filter ZorgNotes."""

    areas: list[str] = field(default_factory=list)
    contexts: list[str] = field(default_factory=list)
    create_date_ranges: list[DateRange] = field(default_factory=list)
    desc_filters: list[DescFilter] = field(default_factory=list)
    done: Optional[bool] = None
    done_date_ranges: list[DateRange] = field(default_factory=list)
    property_filters: list[PropertyFilter] = field(default_factory=list)
    priorities: list[TodoPriorityType] = field(default_factory=list)
    projects: list[str] = field(default_factory=list)


@dataclass(frozen=True)
class OrZorgQuery:
    """A collection of `AndZorgQuery`s that have been ORed together."""

    and_queries: Iterable[AndZorgQuery]
