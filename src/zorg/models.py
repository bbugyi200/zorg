"""This file contains Zorg's domain model classes."""

from dataclasses import dataclass, field
import datetime as dt
from pathlib import Path
from typing import Iterable, Optional

from .types import (
    DescOperator,
    MetatagOperator,
    MetatagValueType,
    TodoPriorityType,
    TodoStatus,
)


@dataclass(frozen=True)
class DateRange:
    """Represents a range of dates."""

    start: dt.date
    end: Optional[dt.date] = None


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


@dataclass(frozen=True)
class DescFilter:
    """Represents a description query filter (e.g. '"foo"' or '!"bar"')."""

    value: str
    case_sensitive: Optional[bool] = None
    op: DescOperator = DescOperator.CONTAINS


@dataclass(frozen=True)
class MetatagFilter:
    """Represents a single metatag filter (e.g. 'due<=0d' or '!recur')."""

    key: str
    value: str = ""
    op: MetatagOperator = MetatagOperator.EXISTS
    value_type: MetatagValueType = MetatagValueType.STRING


@dataclass
class AndZorgQuery:
    """Tag used to filter ZorgNotes."""

    contexts: list[str] = field(default_factory=list)
    create_date_ranges: list[DateRange] = field(default_factory=list)
    desc_filters: list[DescFilter] = field(default_factory=list)
    done_date_ranges: list[DateRange] = field(default_factory=list)
    done: Optional[bool] = None
    epics: list[str] = field(default_factory=list)
    metatag_filters: list[MetatagFilter] = field(default_factory=list)
    priorities: list[TodoPriorityType] = field(default_factory=list)
    projects: list[str] = field(default_factory=list)


@dataclass(frozen=True)
class OrZorgQuery:
    """A collection of `AndZorgQuery`s that have been ORed together."""

    and_queries: Iterable[AndZorgQuery]
