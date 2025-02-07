"""Custom types used by zorg."""

# pyright: reportGeneralTypeIssues=false

import abc
from dataclasses import dataclass
import datetime as dt
import enum
from pathlib import Path
from typing import (
    TYPE_CHECKING,
    Any,
    Callable,
    Final,
    Generic,
    Literal,
    Mapping,
    Optional,
    Pattern,
    Protocol,
    Sequence,
    TypeVar,
    Union,
)

from sqlalchemy.future import Engine
from typist import assert_never

if TYPE_CHECKING:
    from zorg.domain.models import Note, Section, TodoPayload


E = TypeVar("E")
T = TypeVar("T")

KeyFunc = Callable[["Note"], str]
FileGroupMapType = Mapping[str, Sequence[str]]
FuncName = Literal["count"]
SelectType = Union[
    "SelectAggregation", "SelectStaticType", "SelectPropertyValues"
]
TagName = Literal["areas", "contexts", "links", "people", "projects"]
MetadataType = Literal[TagName, "properties"]
TodoPriorityType = Literal[
    "P0", "P1", "P2", "P3", "P4", "P5", "P6", "P7", "P8", "P9"
]
TemplatePatternMapType = Mapping[Pattern, Path]
VarMapType = Mapping[str, Any]

# Prefix characters that specifies the type of a Zorg note.
DoneTodoTypeChar = Literal["x", "~"]
TodoTypeChar = Literal[DoneTodoTypeChar, "o", "<", ">"]
NoteTypeChar = Literal[TodoTypeChar, "-"]

_SECTION_SEP: Final = "|"


def cast_tag_name(name: TagName) -> TagName:
    """Typing helper for working with TagNames."""
    return name


class NoteType(enum.Enum):
    """Zorg note status."""

    BASIC = "-"
    OPEN_TODO = "o"
    CLOSED_TODO = "x"
    CANCELED_TODO = "~"
    BLOCKED_TODO = "<"
    PARENT_TODO = ">"

    def to_header_label(self) -> str:
        """Converts to a header label that can be used by GROUP BY."""
        open_todos_label: Final = "1 | OPEN TODOS"
        if self is NoteType.BASIC:
            return "4 | NOTES"
        elif self is NoteType.OPEN_TODO:
            return open_todos_label
        elif self is NoteType.CLOSED_TODO:
            return "2 | DONE TODOS"
        elif self is NoteType.CANCELED_TODO:
            return "3 | CANCELED TODOS"
        elif self is NoteType.BLOCKED_TODO:
            return open_todos_label
        elif self is NoteType.PARENT_TODO:
            return open_todos_label
        else:
            assert_never(self)


class Color(enum.Enum):
    """Represents colors that Zorg uses."""

    BLACK = "black"
    GREEN = "#1A7E23"
    WHITE = "#FFFFFF"
    YELLOW = "#FFFEB8"


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
    PRIORITY = enum.auto()
    PROJECT = enum.auto()
    SECTION = enum.auto()

    @property
    def keyfunc(self) -> KeyFunc:
        """Returns a callable that can be used to group notes."""
        if self is GroupByType.AREA:
            return _to_comparable_tag_factory("areas", "#")
        elif self is GroupByType.CONTEXT:
            return _to_comparable_tag_factory("contexts", "@")
        elif self is GroupByType.FILE:
            return lambda note: _to_comparable_file(note.file_path)
        elif self is GroupByType.NOTE_TYPE:
            return lambda note: _to_comparable_note_type(note.todo_payload)
        elif self is GroupByType.PERSON:
            return _to_comparable_tag_factory("people", "%")
        elif self is GroupByType.PROJECT:
            return _to_comparable_tag_factory("projects", "+")
        elif self is GroupByType.PRIORITY:
            return lambda note: _to_comparable_priority(note.todo_payload)
        elif self is GroupByType.SECTION:
            return _to_comparable_section_from_note
        else:
            assert_never(self)


class OrderByType(enum.Enum):
    """Represents a single ORDER BY field for zorg queries."""

    ALPHA = enum.auto()
    CREATE_DATE = enum.auto()
    MODIFY_DATE = enum.auto()
    NONE = enum.auto()
    NOTE_TYPE = enum.auto()
    PRIORITY = enum.auto()

    @property
    def keyfunc(self) -> KeyFunc:
        """Returns a callable that can be used sort notes."""
        if self is OrderByType.ALPHA:
            return lambda note: note.to_string()
        elif self is OrderByType.CREATE_DATE:
            return lambda note: _to_comparable_date(note.create_date)
        elif self is OrderByType.MODIFY_DATE:
            return lambda note: _to_comparable_date(note.modify_date)
        elif self is OrderByType.NOTE_TYPE:
            return lambda note: _to_comparable_note_type(note.todo_payload)
        elif self is OrderByType.PRIORITY:
            return lambda note: _to_comparable_priority(note.todo_payload)
        elif self is OrderByType.NONE:
            return lambda note: f"{str(note.file_path)}::{note.line_no}"
        else:
            assert_never(self)


class SelectStaticType(enum.Enum):
    """A zorg query (S)ELECT."""

    # Select file paths.
    FILE = enum.auto()

    # Select a note.
    NOTE = enum.auto()

    # Select tags.
    AREA = enum.auto()
    CONTEXT = enum.auto()
    PERSON = enum.auto()
    PROJECT = enum.auto()

    # Select property keys.
    PROPERTY = enum.auto()

    # Select links.
    LINKS = enum.auto()


@dataclass(frozen=True)
class SelectPropertyValues:
    """(S)ELECT property values (e.g. via prop:foo selector)"""

    key: str


@dataclass(frozen=True)
class SelectAggregation:
    """(S)ELECT aggregation function call [e.g. count(note)]"""

    func_name: FuncName
    select_type: SelectType

    def aggregate(self, values: list[str]) -> int:
        """Aggregates a list of values (e.g. notes, property values)."""
        if self.func_name == "count":
            return len(values)
        else:
            assert_never(self)


class PropertyOperator(enum.Enum):
    """Used to determine what kind of property constraint has been specified."""

    EXISTS = enum.auto()
    EQ = enum.auto()
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
    def from_entity(self, _: E) -> T:
        """Converts some domain entity into something else."""


def _to_comparable_note_type(todo_payload: Optional["TodoPayload"]) -> str:
    if todo_payload is None:
        return NoteType.BASIC.to_header_label()
    else:
        return todo_payload.status.to_header_label()


def _to_comparable_priority(todo_payload: Optional["TodoPayload"]) -> str:
    if todo_payload is None:
        return ""
    else:
        return todo_payload.priority


def _to_comparable_file(file_path: Optional[Path]) -> str:
    assert file_path is not None
    link_name = str(file_path).replace(".zo", "")
    return f"[[{link_name}]]"


def _to_comparable_date(date: dt.date) -> str:
    return date.strftime("%Y%m%d")


def _to_comparable_tag_factory(attr: str, tag_symbol: str) -> KeyFunc:
    def _keyfunc(note: "Note") -> str:
        return " | ".join(
            f"{tag_symbol}{tag}" for tag in sorted(getattr(note, attr))
        )

    return _keyfunc


def _to_comparable_section_from_note(note: "Note") -> str:
    assert note.block is not None
    assert note.block.section is not None
    return _to_comparable_section_from_section(note.block.section)


def _to_comparable_section_from_section(section: "Section") -> str:
    from zorg.domain.models import H1, H2, H3, H4

    result = ""
    if isinstance(section, H1):
        h1 = section
    else:
        if isinstance(section, H2):
            h2 = section
        else:
            if isinstance(section, H3):
                h3 = section
            else:
                assert isinstance(section, H4)
                result = section.title
                assert section.h3 is not None
                h3 = section.h3
            assert h3.h2 is not None
            h2 = h3.h2
            result = _prepend_to_header(result, h3.title)
        assert h2.h1 is not None
        h1 = h2.h1
        result = _prepend_to_header(result, h2.title)
    if h1.title:
        result = _prepend_to_header(result, h1.title)
    return result


def _prepend_to_header(header: str, value: str) -> str:
    header = header if header == "" else f" {_SECTION_SEP} {header}"
    return f"{value}{header}"
