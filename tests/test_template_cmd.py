"""Tests for the zorg project's 'template' CLI command."""

from __future__ import annotations

from pathlib import Path

from _pytest.capture import CaptureFixture
from syrupy.assertion import SnapshotAssertion as Snapshot

from . import common as c


def test_template_render_day_log(
    main: c.MainType,
    capsys: CaptureFixture,
    tmp_path: Path,
    snapshot: Snapshot,
) -> None:
    """Test that the 'day_log_tmpl.zo' template renders as expected."""
    zettel_dir = tmp_path / "org"
    zot_basename = "day_log_tmpl.zo"
    template_path: Path = zettel_dir / zot_basename
    template_path.parent.mkdir(parents=True, exist_ok=True)
    test_data_template_path = Path(__file__).parent / Path(
        f"data/{zot_basename}"
    )
    template_path.write_text(test_data_template_path.read_text())

    argv = [
        "--dir",
        str(zettel_dir),
        "template",
        "render",
        zot_basename,
        "date=19910304",
    ]
    exit_code = main(*argv)

    assert exit_code == 0
    capture = capsys.readouterr()
    assert capture.out == snapshot


def test_template_render_hello(
    main: c.MainType,
    capsys: CaptureFixture,
    tmp_path: Path,
) -> None:
    """Test that the 'hello_tmpl.zo' template renders as expected."""
    zettel_dir = tmp_path / "org"
    zot_basename = "hello_tmpl.zo"
    template_path: Path = zettel_dir / zot_basename
    template_path.parent.mkdir(parents=True, exist_ok=True)
    test_data_template_path = Path(__file__).parent / Path(
        f"data/{zot_basename}"
    )
    template_path.write_text(test_data_template_path.read_text())

    argv = [
        "--dir",
        str(zettel_dir),
        "template",
        "render",
        zot_basename,
        "first_name=John",
        "last_name=Smith",
    ]
    assert main(*argv) == 0

    capture = capsys.readouterr()
    assert capture.out == "Hello John Smith\n"
