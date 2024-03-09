"""Custom types used by zorg."""

from typing import Literal, Mapping, Sequence


Action = Literal["OPEN_LINK"]
FileGroupMapType = Mapping[str, Sequence[str]]
