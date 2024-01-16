"""Tests the zorg project's CLI."""

from __future__ import annotations

from zorg.__main__ import main


def test_main() -> None:
    """Tests main() function."""
    assert main([""]) == 0
