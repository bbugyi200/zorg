"""Tests for the zorg project's 'note' CLI command."""

from __future__ import annotations

from pathlib import Path

from pytest import mark, param
from syrupy.assertion import SnapshotAssertion as Snapshot

from . import common as c


params = mark.parametrize


@params(
    "zid,src_name,dest_name",
    [
        param("240510#02", "basic.zo", "property.zo", id="basic"),
        param("240510#0Q", "property.zo", "tags_and_ids.zo", id="multiline"),
    ],
)
def test_note_move(
    main: c.MainType,
    db_zettel_dir: Path,
    snapshot: Snapshot,
    zid: str,
    src_name: str,
    dest_name: str,
) -> None:
    """Tests the 'note move' command."""
    exit_code = main(
        "--dir", str(db_zettel_dir), "note", "move", zid, dest_name
    )

    src_path = db_zettel_dir / src_name
    dest_path = db_zettel_dir / dest_name
    assert exit_code == 0
    assert snapshot == src_path.read_text()
    assert snapshot == dest_path.read_text()
