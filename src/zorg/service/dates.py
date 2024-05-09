"""Utilities for managing Zorg dates live here."""

import datetime as dt


def from_short_date(short_date: str) -> dt.date:
    """Creates a date from a short zorg date of the form YYMMDD."""
    return dt.datetime.strptime(f"20{short_date}", "%Y%m%d").date()
