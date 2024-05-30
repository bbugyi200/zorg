"""Tests for the zorg project's 'query' CLI command."""

from __future__ import annotations

from pathlib import Path

from _pytest.capture import CaptureFixture
from pytest import mark, param
from syrupy.assertion import SnapshotAssertion as Snapshot

from . import common as c


params = mark.parametrize


@params(
    "query",
    [
        param("o", id="open_todos"),
        param("o P0", id="high_priority"),
        param("o P1-2", id="mid_and_low_priority"),
        param("W - +zorg G file", id="zorg_notes"),
        param(
            "S note W (o | x | ~ | < | > | -) O priority create modify G file",
            id="grouped_and_ordered",
        ),
        param(
            "S note W (o | x | ~ | < | > | -) G type # +",
            id="group_by_type_area_project",
        ),
        param("(o | x | ~ | < | > | -) G @", id="group_by_context"),
        param("(o | x | ~ | < | > | -) G %", id="group_by_people"),
        param("^240408 $240509", id="filter_by_create_and_modify"),
        param("due:2024-03-13", id="filter_by_property_eq"),
        param("p:>5", id="filter_by_property_gt"),
        param("'foo'", id="desc_filter__foo"),
        param("c's' c'u' c'p' G file", id="desc_filter__s_u_p"),
        param("S +", id="select_projects"),
        param("S file W o", id="select_files_with_todos"),
        param("f=basic G file", id="file_filter_basic"),
        param("f=*s G file", id="file_filter__ends_with_s"),
        param("f=p* G file", id="file_filter__starts_with_p"),
        param("f=*p* G file", id="file_filter__has_a_p"),
        param(
            "!f=*scrambled* !'e' G file",
            id="not_scrambled_file_AND_no_e_in_desc",
        ),
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
