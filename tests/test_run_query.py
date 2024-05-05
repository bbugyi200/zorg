"""Tests for the zorg project's 'query' CLI command."""

from __future__ import annotations

from pathlib import Path

from _pytest.capture import CaptureFixture
from pytest import fixture, mark
from syrupy.assertion import SnapshotAssertion as Snapshot

from . import common as c


params = mark.parametrize


@fixture(scope="module")
def db_zettel_dir(main: c.MainType, module_zettel_dir: Path) -> Path:
    """Returns zettel dir containing pre-initialized database.."""
    assert main("--dir", str(module_zettel_dir), "db", "create") == 0
    return module_zettel_dir


@params("query", ["o", "o [#a]", "o [#bc]", "W - +zorg G file"])
def test_query(
    main: c.MainType,
    capsys: CaptureFixture,
    snapshot: Snapshot,
    db_zettel_dir: Path,
    query: str,
) -> None:
    """Tests that zorg queries produce expected output."""
    exit_code = main("--dir", str(db_zettel_dir), "query", query)
    capture = capsys.readouterr()

    assert exit_code == 0
    assert capture.out == snapshot
