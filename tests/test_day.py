"""Tests the zorg project's 'day' CLI command."""

from __future__ import annotations

from . import common as c


def test_day_basic(main: c.MainType) -> None:
    """Basic test of the 'day' subcommand.

    Tests that zorg exits successfully (e.g. does not throw any exceptions).
    """
    assert main("day") == 0
