"""Test utils used by multiple modules."""

from __future__ import annotations

from typing import Any, Final, Protocol


# datetime info used by freezegun (and tests)
hh: Final = "12"
mm: Final = "00"
hhmm: Final = f"{hh}{mm}"

YYYY: Final = "2000"
MM: Final = "01"
DD: Final = "03"
YEST_DD: Final = "02"
TODAY: Final = f"{YYYY}-{MM}-{DD}"


class MainType(Protocol):
    """Type returned by main() fixture."""

    def __call__(self, *args: str, **kwargs: Any) -> int:
        """The signature of the main() function."""
