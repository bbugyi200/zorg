"""Contains the Query domain entity."""

from dataclasses import dataclass, field
import datetime as dt
from typing import Iterable, Optional

from ..types import (
    DescOperator,
    GroupByType,
    NoteType,
    OrderByType,
    PropertyOperator,
    PropertyValueType,
    SelectType,
    TodoPriorityType,
)


@dataclass(frozen=True)
class DescFilter:
    """Represents a description query filter (e.g. '"foo"' or '!"bar"')."""

    value: str
    case_sensitive: Optional[bool] = None
    op: DescOperator = DescOperator.CONTAINS


@dataclass(frozen=True)
class FileFilter:
    """Represents a single file filter (e.g. 'f=foobar' or 'f=*baz*')."""

    path_glob: str
    negated: bool = False


@dataclass(frozen=True)
class LinkFilter:
    """Represents a single link filter (e.g. '[[foobar]]' or '![[bazbuz]]')."""

    link: str
    negated: bool = False


@dataclass(frozen=True)
class PropertyFilter:
    """Represents a single property filter (e.g. 'due:<=0d' or '!recur:*')."""

    key: str
    value: str = ""
    op: PropertyOperator = PropertyOperator.EXISTS
    value_type: PropertyValueType = PropertyValueType.STRING
    negated: bool = False


@dataclass(frozen=True)
class DateRange:
    """Represents a range of dates."""

    start: dt.date
    end: Optional[dt.date] = None


@dataclass
class WhereAndFilter:
    """Tag used to filter ZorgNotes."""

    allowed_note_types: set[NoteType] = field(default_factory=set)
    areas: set[str] = field(default_factory=set)
    contexts: set[str] = field(default_factory=set)
    create_date_ranges: set[DateRange] = field(default_factory=set)
    desc_filters: set[DescFilter] = field(default_factory=set)
    file_filters: set[FileFilter] = field(default_factory=set)
    link_filters: set[LinkFilter] = field(default_factory=set)
    modify_date_ranges: set[DateRange] = field(default_factory=set)
    or_filters: list["WhereOrFilter"] = field(default_factory=list)
    people: set[str] = field(default_factory=set)
    property_filters: set[PropertyFilter] = field(default_factory=set)
    priorities: set[TodoPriorityType] = field(default_factory=set)
    projects: set[str] = field(default_factory=set)

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
class Query:
    """A zorg query that uses SWOG syntax.

    (S)ELECT
    (W)HERE
    (O)RDER BY
    (G)ROUP BY
    """

    select: SelectType = field(default=SelectType.NOTE)
    where: Optional[WhereOrFilter] = None
    order_by: tuple[OrderByType, ...] = (
        OrderByType.NOTE_TYPE,
        OrderByType.PRIORITY,
        OrderByType.MODIFY_DATE,
        OrderByType.CREATE_DATE,
    )
    group_by: tuple[GroupByType, ...] = tuple()
