"""Custom types used by zorg."""

import abc
import enum
from pathlib import Path
from typing import (
    TYPE_CHECKING,
    Any,
    Callable,
    Generic,
    Literal,
    Mapping,
    Optional,
    Pattern,
    Protocol,
    Sequence,
    TypeVar,
)

from sqlalchemy.future import Engine
from typist import Comparable, assert_never


if TYPE_CHECKING:
    from .models import Note, TodoPayload


E = TypeVar("E")
T = TypeVar("T")


KeyFunc = Callable[["Note"], Comparable]
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


class NoteType(enum.Enum):
    """Zorg note status."""

    BASIC = enum.auto()  # -
    OPEN_TODO = enum.auto()  # o
    CLOSED_TODO = enum.auto()  # x
    CANCELED_TODO = enum.auto()  # ~
    BLOCKED_TODO = enum.auto()  # <
    PARENT_TODO = enum.auto()  # >

    def to_header_label(self) -> str:
        """Converts to a header label that can be used by GROUP BY."""
        if self is NoteType.BASIC:
            return "Notes"
        elif self is NoteType.OPEN_TODO:
            return "Open Todos"
        elif self is NoteType.CLOSED_TODO:
            return "Done Todos"
        elif self is NoteType.CANCELED_TODO:
            return "Canceled Todos"
        elif self is NoteType.BLOCKED_TODO:
            return "Blocked Todos"
        elif self is NoteType.PARENT_TODO:
            return "Parent Todos"
        else:
            assert_never(self)

    def to_prefix_char(self) -> str:  # pyright: reportGeneralTypeIssues=false
        """Converts a note's type to its corresponding prefix character."""
        if self is NoteType.BASIC:
            return "-"
        elif self is NoteType.OPEN_TODO:
            return "o"
        elif self is NoteType.CLOSED_TODO:
            return "x"
        elif self is NoteType.CANCELED_TODO:
            return "~"
        elif self is NoteType.BLOCKED_TODO:
            return "<"
        elif self is NoteType.PARENT_TODO:
            return ">"
        else:
            assert_never(self)


class Color(enum.Enum):
    """Represents colors that Zorg uses."""

    BLACK = enum.auto()
    GREEN = enum.auto()
    WHITE = enum.auto()
    YELLOW = enum.auto()

    def to_rich_spec(self) -> str:
        """Converts a Color to a string spec that rich understands."""
        if self is Color.BLACK:
            return "black"
        elif self is Color.GREEN:
            return "#1A7E23"
        elif self is Color.WHITE:
            return "#FFFFFF"
        elif self is Color.YELLOW:
            return "#FFFEB8"
        else:
            assert_never(self)


class CreateEngineType(Protocol):
    """The type of a `db.create_engine()` callable."""

    def __call__(self, url: str, /, **kwargs: Any) -> Engine:
        """The function's call signature."""


class DescOperator(enum.Enum):
    """Used to determine the type of description constraint specified."""

    CONTAINS = enum.auto()
    NOT_CONTAINS = enum.auto()


class GroupByType(enum.Enum):
    """Represents a single GROUP BY field for zorg queries."""

    AREA = enum.auto()
    CONTEXT = enum.auto()
    FILE = enum.auto()
    NOTE_TYPE = enum.auto()
    PERSON = enum.auto()
    PROJECT = enum.auto()

    @property
    def keyfunc(self) -> KeyFunc:
        """Returns a callable that can be used to group/sort notes."""
        if self is GroupByType.AREA:
            return _tag_keyfunc_factory("areas", "#")
        elif self is GroupByType.CONTEXT:
            return _tag_keyfunc_factory("contexts", "@")
        elif self is GroupByType.FILE:
            return lambda note: _to_comparable_file(note.file_path)
        elif self is GroupByType.NOTE_TYPE:
            return lambda note: _to_comparable_note_type(note.todo_payload)
        elif self is GroupByType.PERSON:
            return _tag_keyfunc_factory("people", "%")
        elif self is GroupByType.PROJECT:
            return _tag_keyfunc_factory("projects", "+")
        else:
            assert_never(self)


class OrderByType(enum.Enum):
    """Represents a single ORDER BY field for zorg queries."""

    DATE = enum.auto()
    NOTE_TYPE = enum.auto()
    PRIORITY = enum.auto()


class SelectType(enum.Enum):
    """A zorg query (S)ELECT."""

    AREA = enum.auto()
    CONTEXT = enum.auto()
    FILE = enum.auto()
    NOTE = enum.auto()
    PERSON = enum.auto()
    PROJECT = enum.auto()


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


def _to_comparable_note_type(todo_payload: Optional["TodoPayload"]) -> str:
    if todo_payload is None:
        return NoteType.BASIC.to_header_label()
    else:
        return todo_payload.status.to_header_label()


def _to_comparable_file(file_path: Optional[Path]) -> str:
    assert file_path is not None
    link_name = str(file_path).replace(".zo", "")
    return f"[[{link_name}]]"


def _tag_keyfunc_factory(attr: str, tag_symbol: str) -> KeyFunc:
    def _keyfunc(note: "Note") -> str:
        return " ".join(
            f"{tag_symbol}{tag}" for tag in sorted(getattr(note, attr))
        )

    return _keyfunc
