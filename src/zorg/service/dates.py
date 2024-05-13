"""Utilities for managing Zorg dates live here."""

import datetime as dt
from typing import Final


_DATE_FMT: Final = "%Y%m%d"


def from_short_date(short_date: str) -> dt.date:
    """Creates a date from a short zorg date of the form YYMMDD."""
    return dt.datetime.strptime(f"20{short_date}", _DATE_FMT).date()


def to_short_date(date: dt.date) -> str:
    """Creates a short zorg date of the form YYMMDD from a date."""
    return date.strftime(_DATE_FMT)[2:]


def is_short_date(short_date: str) -> bool:
    """Returns True iff {short_date} is a valid short date."""
    return len(short_date) == 6 and all(ch.isdigit() for ch in short_date)


def is_zid(zid: str) -> bool:
    """Returns True iff {zid} is a valid ZID."""
    return len(zid) == 9 and is_short_date(zid[:6]) and zid[6] == "#"
