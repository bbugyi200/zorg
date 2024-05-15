"""Utilities for managing Zorg dates live here."""

import datetime as dt
from typing import Final


_SHORT_DATE_FMT: Final = "%Y%m%d"
_LONG_DATE_FMT: Final = "%Y-%m-%d"


def from_short_date(short_date: str) -> dt.date:
    """Creates a date from a short zorg date of the form YYMMDD."""
    return dt.datetime.strptime(f"20{short_date}", _SHORT_DATE_FMT).date()


def from_long_date(long_date: str) -> dt.date:
    """Creates a date from a long zorg date of the form YYYY-MM-DD."""
    return dt.datetime.strptime(long_date, _LONG_DATE_FMT).date()


def to_date(date_spec: str) -> dt.date:
    """Converts some date string spec to an actual date."""
    if is_short_date(date_spec):
        return from_short_date(date_spec)
    elif is_long_date(date_spec):
        return from_long_date(date_spec)
    else:
        raise RuntimeError(f"Unrecognize date format: {date_spec}")


def to_short_date(date: dt.date) -> str:
    """Creates a short zorg date of the form YYMMDD from a date."""
    return date.strftime(_SHORT_DATE_FMT)[2:]


def is_short_date(short_date: str) -> bool:
    """Returns True iff {short_date} is a valid short date."""
    return len(short_date) == 6 and all(ch.isdigit() for ch in short_date)


def is_long_date(long_date: str) -> bool:
    """Returns True iff {long_date} is a valid long date."""
    return (
        len(long_date) == 10
        and {long_date[4], long_date[7]} == {"-"}
        and all(ch.isdigit() for ch in long_date.replace("-", ""))
    )


def is_date(date_spec: str) -> bool:
    """Returns True iff {date_spec} is a valid zorg date."""
    return is_short_date(date_spec) or is_long_date(date_spec)


def is_zid(zid: str) -> bool:
    """Returns True iff {zid} is a valid ZID."""
    return len(zid) == 9 and is_short_date(zid[:6]) and zid[6] == "#"
