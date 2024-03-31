"""Custom types used by zorg."""

import enum
from pathlib import Path
from typing import Any, Literal, Mapping, Pattern, Protocol, Sequence

from sqlalchemy.future import Engine


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


class TodoStatus(enum.Enum):
    """Status of a Zorg todo."""

    OPEN = enum.auto()
    CLOSED = enum.auto()
    CANCELED = enum.auto()


class CreateEngineType(Protocol):
    """The type of a `db.create_engine()` callable."""

    def __call__(self, url: str, /, **kwargs: Any) -> Engine:
        """The function's call signature."""


class DescOperator(enum.Enum):
    """Used to determine the type of description constraint specified."""

    CONTAINS = enum.auto()
    NOT_CONTAINS = enum.auto()


class MetatagOperator(enum.Enum):
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


class MetatagValueType(enum.Enum):
    """Specifies the data type of a MetatagFilter's value."""

    DATE = enum.auto()
    INTEGER = enum.auto()
    STRING = enum.auto()
