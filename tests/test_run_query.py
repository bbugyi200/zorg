"""Tests for the zorg project's 'query' CLI command."""

from __future__ import annotations

from pathlib import Path

from _pytest.capture import CaptureFixture
from pytest import fixture, mark, param
from syrupy.assertion import SnapshotAssertion as Snapshot

from . import common as c


params = mark.parametrize


@params(
    "query",
    [
        param("o", id="open_todos"),
        param("o [#a]", id="high_priority"),
        param("o [#bc]", id="mid_and_low_priority"),
        param("W - +zorg G file", id="zorg_notes"),
        param(
            "S note W (o or x or ~ or < or > or -) O priority date G file",
            id="grouped_and_ordered",
        ),
        param(
            "S note W (o or x or ~ or < or > or -) G type # +",
            id="group_by_type_area_project",
        ),
        param("(o or x or ~ or < or > or -) G @", id="group_by_context"),
        param("(o or x or ~ or < or > or -) G %", id="group_by_people"),
    ],
)
def test_query(
    main: c.MainType,
    capsys: CaptureFixture,
    snapshot: Snapshot,
    db_zettel_dir: Path,
    query: str,
) -> None:
    """Tests that zorg queries produce expected output."""
    exit_code = main("--log=null", "--dir", str(db_zettel_dir), "query", query)
    capture = capsys.readouterr()

    assert exit_code == 0
    assert capture.err == ""
    assert capture.out == snapshot
