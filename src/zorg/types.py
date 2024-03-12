"""Custom types used by zorg."""

from pathlib import Path
from typing import Any, Literal, Mapping, Pattern, Sequence


FileGroupMapType = Mapping[str, Sequence[str]]
TemplatePatternMapType = Mapping[Pattern, Path]
VarMapType = Mapping[str, Any]
