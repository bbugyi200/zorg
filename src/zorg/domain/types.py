"""Custom types used by zorg."""

import abc
import enum
from pathlib import Path
from typing import (
    Any,
    Generic,
    Literal,
    Mapping,
    Pattern,
    Protocol,
    Sequence,
    TypeVar,
)

from sqlalchemy.future import Engine


E = TypeVar("E")
T = TypeVar("T")


FileGroupMapType = Mapping[str, Sequence[str]]
TodoPriorityType = Literal[
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]
TemplatePatternMapType = Mapping[Pattern, Path]
VarMapType = Mapping[str, Any]
TodoStatusPrefixChar = Literal["o", "x", "~", "<", ">"]


class NoteStatus(enum.Enum):
    """Zorg note status."""

    BASIC = enum.auto()  # -
    OPEN_TODO = enum.auto()  # o
    CLOSED_TODO = enum.auto()  # x
    CANCELED_TODO = enum.auto()  # ~
    BLOCKED_TODO = enum.auto()  # <
    PARENT_TODO = enum.auto()  # >


class CreateEngineType(Protocol):
    """The type of a `db.create_engine()` callable."""

    def __call__(self, url: str, /, **kwargs: Any) -> Engine:
        """The function's call signature."""


class DescOperator(enum.Enum):
    """Used to determine the type of description constraint specified."""

    CONTAINS = enum.auto()
    NOT_CONTAINS = enum.auto()


class Select(enum.Enum):
    """A zorg query (S)ELECT."""

    AREAS = enum.auto()
    CONTEXTS = enum.auto()
    FILES = enum.auto()
    NOTES = enum.auto()
    PEOPLE = enum.auto()
    PROJECTS = enum.auto()


class PropertyOperator(enum.Enum):
    """Used to determine what kind of metatag constraint has been specified."""

    # exists / not exists
    EXISTS = enum.auto()
    NOT_EXISTS = enum.auto()

    # comparison operators
    EQ = enum.auto()
    NE = enum.auto()
    LT = enum.auto()
    LE = enum.auto()
    GT = enum.auto()
    GE = enum.auto()


class PropertyValueType(enum.Enum):
    """Specifies the data type of a PropertyFilter's value."""

    DATE = enum.auto()
    INTEGER = enum.auto()
    STRING = enum.auto()


class EntityConverter(Generic[E, T], abc.ABC):
    """Abstract interface for domain entity converters."""

    @abc.abstractmethod
    def to_entity(self, _: T) -> E:
        """Converts some non-domain object into a domain entity."""

    @abc.abstractmethod
    def from_entity(self, entity: E) -> T:
        """Converts some domain entity into something else."""
