"""Zorg ID generation and persistence logic lives here."""

import datetime as dt
import json
from pathlib import Path
from typing import Final, Optional, cast

from .. import APP_NAME


_UNSUPPORTED_ZID_CHARS: Final[tuple[str, ...]] = (
    "I",
    "O",
    "Q",
    "S",
    "g",
    "i",
    "j",
    "l",
    "p",
    "q",
    "y",
)


class ZIDManager:
    """Responsible for knowing what the next zorg ID is based on the date."""

    def __init__(self, zettel_dir: Path) -> None:
        zorg_data_dir = zettel_dir / f".{APP_NAME}"
        zorg_data_dir.mkdir(exist_ok=True)
        self._next_ids_path = zorg_data_dir / "next_ids.json"
        self._mutable_next_id_map: Optional[dict[str, str]] = None

    def get_next(self, date: dt.date) -> str:
        """Returns the next zorg ID based on {date}."""
        date_part = date.strftime("%Y%m%d")[2:]
        next_id_map = self._next_id_map
        id_part = next_id_map.get(date_part, "00")
        # pylint: disable=unsupported-assignment-operation
        next_id_map[date_part] = _get_next_id(id_part)
        self._write_to_disk(next_id_map)
        return f"{date_part}#{id_part}"

    def _write_to_disk(self, next_id_map: dict[str, str]) -> None:
        """Writes the next ID map back to disk."""
        with self._next_ids_path.open("w") as f:
            json.dump(dict(next_id_map), f, indent=4)

    @property
    def _next_id_map(self) -> dict[str, str]:
        if self._next_ids_path.exists() and self._mutable_next_id_map is None:
            return cast(
                dict[str, str], json.loads(self._next_ids_path.read_text())
            )
        else:
            return {}


def _get_next_id(last_id: str) -> str:
    next_ch: Optional[str] = None
    idx = -1
    while next_ch is None and abs(idx) <= len(last_id):
        ch = last_id[idx]
        if ch == "9":
            next_ch = "A"
        elif ch == "Z":
            next_ch = "a"
        elif ch == "z":
            next_ch = None
            idx -= 1
        else:
            next_ch = chr(ord(ch) + 1)
            while next_ch in _UNSUPPORTED_ZID_CHARS:
                next_ch = chr(ord(next_ch) + 1)

    if next_ch is None and len(last_id) == 2:
        # Special case that allows for 3-digit ID part if necessary. This
        # allows for enough available IDs if you run 'db create' on a large
        # zettel org with a lot of notes that need ZIDs.
        return "000"
    elif next_ch is None:
        raise RuntimeError(
            f"Ran out of zorg IDs to allocate! | last_id={last_id}"
        )

    next_id = last_id[:idx] + next_ch
    while len(next_id) < len(last_id):
        next_id = f"{next_id}0"
    return next_id
