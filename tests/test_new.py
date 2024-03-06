"""Tests for the zorg project's 'new' CLI command."""

from __future__ import annotations

from pathlib import Path

from _pytest.capture import CaptureFixture
from syrupy.assertion import SnapshotAssertion as Snapshot

from . import common as c


def test_new(
    main: c.MainType,
    capsys: CaptureFixture,
    tmp_path: Path,
    snapshot: Snapshot,
) -> None:
    """Test the 'new' subcommand."""
    zettel_dir = tmp_path / "org"
    template_path: Path = zettel_dir / "day_log_tmpl.zo"
    template_path.parent.mkdir(parents=True, exist_ok=True)
    test_data_template_path = Path(__file__).parent / Path(
        "data/day_log_tmpl.zo"
    )
    template_path.write_text(test_data_template_path.read_text())

    argv = [
        "--dir",
        str(zettel_dir),
        "new",
        "day_log_tmpl.zo",
        "date=19910304",
    ]
    assert main(*argv) == 0

    capture = capsys.readouterr()
    assert capture.out == snapshot
