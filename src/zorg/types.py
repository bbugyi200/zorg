"""Custom types used by zorg."""

import enum
from pathlib import Path
from typing import Any, Literal, Mapping, Pattern, Sequence


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
