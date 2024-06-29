"""Tests for the zorg project's 'note' CLI command."""

from __future__ import annotations

from pathlib import Path

from _pytest.capture import CaptureFixture
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


@params(
    "where_query,mutate",
    [
        param("'240408#0X '", "x +foobar", id="done_foobar_note"),
        param(
            "#thoughts",
            "0o [[deep_work]] +brainstorm @THINKING",
            id="high_priority_thoughts",
        ),
    ],
)
def test_note_mutate(
    main: c.MainType,
    db_zettel_dir: Path,
    snapshot: Snapshot,
    capsys: CaptureFixture,
    where_query: str,
    mutate: str,
) -> None:
    """Tests the 'note mutate' command."""
    exit_code = main(
        "--dir", str(db_zettel_dir), "note", "mutate", where_query, mutate
    )
    capture = capsys.readouterr()

    assert exit_code == 0
    assert capture.out == snapshot
