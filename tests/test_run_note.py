"""Tests for the zorg project's 'note' CLI command."""

from __future__ import annotations

from pathlib import Path
from typing import Optional

from _pytest.capture import CaptureFixture
from pytest import mark, param
from syrupy.assertion import SnapshotAssertion as Snapshot

from . import common as c


params = mark.parametrize


@params(
    "zid,src_name,dest_name,mutate",
    [
        param("240510#02", "basic.zo", "property.zo", None, id="basic"),
        param(
            "240510#0Q", "property.zo", "tags_and_ids.zo", None, id="multiline"
        ),
        param(
            "301231#X1",
            "tags_and_ids.zo",
            "priority.zo",
            "0o",
            id="inherited_tags",
        ),
    ],
)
def test_note_move(
    main: c.MainType,
    db_zettel_dir: Path,
    snapshot: Snapshot,
    zid: str,
    src_name: str,
    dest_name: str,
    mutate: Optional[str],
) -> None:
    """Tests the 'note move' command."""
    main_args = ["--dir", str(db_zettel_dir), "note", "move", zid, dest_name]
    if mutate is not None:
        main_args.append(mutate)
    exit_code = main(*main_args)

    src_path = db_zettel_dir / src_name
    dest_path = db_zettel_dir / dest_name
    assert exit_code == 0
    assert snapshot == src_path.read_text()
    assert snapshot == dest_path.read_text()
