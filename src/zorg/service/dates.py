"""Utilities for managing Zorg dates live here."""

import datetime as dt
from typing import Final, Union

from dateutil.relativedelta import relativedelta


_SHORT_DATE_FMT: Final = "%Y%m%d"
_LONG_DATE_FMT: Final = "%Y-%m-%d"


def from_date_spec(spec: str) -> dt.date:
    """Converts some date string spec to an actual date."""
    if is_short_date_spec(spec):
        return from_short_date_spec(spec)
    elif is_long_date_spec(spec):
        return _from_long_date_spec(spec)
    elif _is_relative_date_spec(spec):
        return _from_relative_date_spec(spec)
    else:
        raise RuntimeError(f"Unrecognize date format: {spec}")


def from_short_date_spec(short_date: str) -> dt.date:
    """Creates a date from a short zorg date of the form YYMMDD."""
    return dt.datetime.strptime(f"20{short_date}", _SHORT_DATE_FMT).date()


def is_date_spec(spec: str) -> bool:
    """Returns True iff {spec} is a valid zorg date."""
    return (
        is_short_date_spec(spec)
        or is_long_date_spec(spec)
        or _is_relative_date_spec(spec)
    )


def is_short_date_spec(short_date: str) -> bool:
    """Returns True iff {short_date} is a valid short date."""
    return len(short_date) == 6 and all(ch.isdigit() for ch in short_date)


def is_long_date_spec(long_date: str) -> bool:
    """Returns True iff {long_date} is a valid long date."""
    return (
        len(long_date) == 10
        and {long_date[4], long_date[7]} == {"-"}
        and all(ch.isdigit() for ch in long_date.replace("-", ""))
    )


def is_zid(zid: str) -> bool:
    """Returns True iff {zid} is a valid ZID."""
    return len(zid) == 9 and is_short_date_spec(zid[:6]) and zid[6] == "#"


def to_short_date_spec(date: dt.date) -> str:
    """Creates a short zorg date of the form YYMMDD from a date."""
    return date.strftime(_SHORT_DATE_FMT)[2:]


def _is_relative_date_spec(spec: str) -> bool:
    """Returns True iff spec appears to be a relative date (e.g. 1d).

    Examples:
        >>> _is_relative_date_spec("0d")
        True

        >>> _is_relative_date_spec("5y")
        True

        >>> _is_relative_date_spec("-10d")
        True

        >>> _is_relative_date_spec("240620")
        False
    """
    if spec.startswith("-"):
        spec = spec[1:]

    return (
        len(spec) > 1
        and spec[:-1].isdigit()
        and spec[-1].lower() in ["d", "m", "y"]
    )


def _from_long_date_spec(long_date: str) -> dt.date:
    """Creates a date from a long zorg date of the form YYYY-MM-DD."""
    return dt.datetime.strptime(long_date, _LONG_DATE_FMT).date()


def _from_relative_date_spec(
    spec: str, *, start_date: dt.date = None, past: bool = False
) -> dt.date:
    """Converts `spec` to a timedelta and adds it to `date`.

    Args:
        spec: A timedelta specification string (e.g. '1d', '2m', '3y').
        start_date: The return value is a function of this argument and the
          timedelta constructed from `spec`. Defaults to today's date.
        past: If set, we use a relative date from the past instead of the
          future (e.g. '1d' will yield yesterday's date instead of today's).

    Examples:
        # Imports
        >>> import datetime as dt

        # Helper Functions
        >>> to_date = lambda x: dt.datetime.strptime(x, "%Y-%m-%d")
        >>> from_date = lambda x: x.strftime("%Y-%m-%d")
        >>> frds = lambda x, y: from_date(
        ...   _from_relative_date_spec(x, start_date=to_date(y))
        ... )
        >>> past_frds = lambda x, y: from_date(
        ...   _from_relative_date_spec(x, start_date=to_date(y), past=True)
        ... )

        # Default start date.
        >>> D = "2000-01-31"

        # Tests
        >>> frds("7d", D)
        '2000-02-07'

        >>> frds("7D", D)
        '2000-02-07'

        >>> frds("1m", D)
        '2000-02-29'

        >>> frds("1m", "2001-01-31")
        '2001-02-28'

        >>> frds("2M", D)
        '2000-03-31'

        >>> frds("3m", D)
        '2000-04-30'

        >>> frds("20y", D)
        '2020-01-31'

        >>> past_frds("1d", D)
        '2000-01-30'

        >>> frds("-1d", D)
        '2000-01-30'
    """
    spec = spec.lower()
    if start_date is None:
        start_date = dt.date.today()

    if spec.startswith("-"):
        past = True
        spec = spec[1:]

    delta: Union[dt.timedelta, relativedelta]
    ch = spec[-1]
    N = int(spec[:-1])

    if ch == "d":
        delta = dt.timedelta(days=N)
    elif ch == "m":
        delta = relativedelta(months=N)
    else:
        assert ch == "y"
        delta = relativedelta(years=N)

    if past:
        return start_date - delta
    else:
        return start_date + delta
