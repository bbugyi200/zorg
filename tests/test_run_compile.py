"""Tests for the zorg project's 'compile' CLI command."""

from __future__ import annotations

from pathlib import Path

from _pytest.capture import CaptureFixture
from pytest import mark, param
from syrupy.assertion import SnapshotAssertion as Snapshot

from . import common as c


params = mark.parametrize


def _get_all_zo_paths() -> list[Path]:
    root_dir = Path(__file__).parent.parent
    return sorted(root_dir.rglob("*.zo"))


@params(
    "zo_path",
    [param(zo_path, id=zo_path.stem) for zo_path in _get_all_zo_paths()],
)
def test_compile(
    main: c.MainType,
    capsys: CaptureFixture,
    tmp_path: Path,
    snapshot: Snapshot,
    zo_path: Path,
) -> None:
    """Test that the all *.zo test data files compile as expected."""
    zettel_dir = tmp_path / "org"

    argv = [
        "--dir",
        str(zettel_dir),
        "compile",
        str(zo_path),
    ]
    exit_code = main(*argv)
    capture = capsys.readouterr()

    assert exit_code == 0
    assert capture.err == ""
    assert capture.out == snapshot
