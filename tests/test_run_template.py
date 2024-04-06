"""Tests for the zorg project's 'template' CLI command."""

from __future__ import annotations

from pathlib import Path

from _pytest.capture import CaptureFixture
from syrupy.assertion import SnapshotAssertion as Snapshot

from . import common as c


def test_template_render_day_log(
    main: c.MainType,
    capsys: CaptureFixture,
    zettel_dir: Path,
    snapshot: Snapshot,
) -> None:
    """Test that the 'day_log.zot' template renders as expected."""
    argv = [
        "--dir",
        str(zettel_dir),
        "template",
        "render",
        "day_log.zot",
        "date=19910304",
    ]
    exit_code = main(*argv)

    assert exit_code == 0
    capture = capsys.readouterr()
    assert capture.out == snapshot


def test_template_render_hello(
    main: c.MainType, capsys: CaptureFixture, zettel_dir: Path
) -> None:
    """Test that the 'hello.zot' template renders as expected."""
    argv = [
        "--dir",
        str(zettel_dir),
        "template",
        "render",
        "hello.zot",
        "first_name=John",
        "last_name=Smith",
    ]
    exit_code = main(*argv)

    assert exit_code == 0
    capture = capsys.readouterr()
    assert capture.out == "Hello John Smith\n"
