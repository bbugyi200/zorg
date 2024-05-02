"""Contains the ZorgQuery Domain entity."""

from dataclasses import dataclass, field
import datetime as dt
from typing import Iterable, Optional

from ..types import (
    DescOperator,
    NoteStatus,
    PropertyOperator,
    PropertyValueType,
    Select,
    TodoPriorityType,
)


@dataclass(frozen=True)
class DescFilter:
    """Represents a description query filter (e.g. '"foo"' or '!"bar"')."""

    value: str
    case_sensitive: Optional[bool] = None
    op: DescOperator = DescOperator.CONTAINS


@dataclass(frozen=True)
class PropertyFilter:
    """Represents a single property filter (e.g. 'due:<=0d' or '!recur:*')."""

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
class WhereAndFilter:
    """Tag used to filter ZorgNotes."""

    allowed_note_statuses: set[NoteStatus] = field(default_factory=set)
    areas: list[str] = field(default_factory=list)
    contexts: list[str] = field(default_factory=list)
    create_date_ranges: list[DateRange] = field(default_factory=list)
    desc_filters: list[DescFilter] = field(default_factory=list)
    modify_date_ranges: list[DateRange] = field(default_factory=list)
    or_filters: list["WhereOrFilter"] = field(default_factory=list)
    people: list[str] = field(default_factory=list)
    property_filters: list[PropertyFilter] = field(default_factory=list)
    priorities: list[TodoPriorityType] = field(default_factory=list)
    projects: list[str] = field(default_factory=list)

    def __repr__(self) -> str:
        """String representation that only shows fields if they are set."""
        dict_repr = ", ".join(
            f"{k}={v!r}"
            for k, v in filter(
                lambda item: bool(item[1]), self.__dict__.items()
            )
        )

        return f"{self.__class__.__name__}({dict_repr})"


@dataclass(frozen=True)
class WhereOrFilter:
    """A collection of `WhereAndFilter`s that have been ORed together."""

    and_filters: Iterable[WhereAndFilter]


@dataclass
class ZorgQuery:
    """A zorg query that uses SWOG syntax.

    (S)ELECT
    (W)HERE
    (O)RDER BY
    (G)ROUP BY
    """

    select: Select = field(default=Select.NOTES)
    where: Optional[WhereOrFilter] = None
