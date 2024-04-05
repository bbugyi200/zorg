"""Tests the zorg project's 'db' CLI command."""

from __future__ import annotations

from pathlib import Path

from syrupy.assertion import SnapshotAssertion as Snapshot

from . import common as c


def test_run_db_create(
    main: c.MainType, tmp_path: Path, snapshot: Snapshot
) -> None:
    """Confirm the 'zorg db create' command can create a SQLite DB file."""
    zettel_dir = tmp_path / "org"
    exit_code = main(
        "--dir",
        str(zettel_dir),
        "db",
        "create"
    )
    assert exit_code == 0
