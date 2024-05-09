"""Tests for the zorg project's 'action' CLI command."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from _pytest.capture import CaptureFixture
from pytest import fixture, mark, param
from syrupy.assertion import SnapshotAssertion as Snapshot

from . import common as c


params = mark.parametrize


@params(
    "lineno,zo_name",
    [(7, "foo.zo"), (9, "bar.sh"), (10, "baz.zo")],
)
def test_action_open__good(
    open_action_main: c.MainType,
    capsys: CaptureFixture,
    zettel_dir: Path,
    lineno: int,
    zo_name: str,
) -> None:
    """Test the 'action open' command's simple happy path."""
    open_action_main(str(lineno))

    capture = capsys.readouterr()
    assert capture.err == ""
    assert capture.out == f"EDIT {zettel_dir}/{zo_name}\n"


@params("lineno", [param(12, id="line_with_no_links")])
def test_action_open__bad(
    open_action_main: c.MainType,
    capsys: CaptureFixture,
    snapshot: Snapshot,
    lineno: int,
) -> None:
    """Test the 'action open' command's sad path."""
    open_action_main(str(lineno))

    capture = capsys.readouterr()
    assert capture.err == ""
    assert capture.out == snapshot


@params(
    "lineno,zo_name",
    [param(5, "order_by_file.zoq", id="order_by_file_query")],
)
def test_action_open__query(
    open_action_main: c.MainType,
    capsys: CaptureFixture,
    snapshot: Snapshot,
    db_zettel_dir: Path,
    lineno: int,
    zo_name: str,
) -> None:
    """Test the 'action open' command with a SWOG query."""
    open_action_main(str(lineno), zdir=db_zettel_dir)

    capture = capsys.readouterr()
    query_zo_path = db_zettel_dir / zo_name
    assert capture.err == ""
    assert capture.out == f"EDIT {query_zo_path}\n"
    assert query_zo_path.read_text() == snapshot


@params("lineno,zo_name,link_prop", [param(11, "buz.zo", "fuzz")])
def testActionOpen_withProperty_sendsSearchMsg(
    open_action_main: c.MainType,
    capsys: CaptureFixture,
    db_zettel_dir: Path,
    lineno: int,
    zo_name: str,
    link_prop: str,
) -> None:
    """Test the 'action open' command's SEARCH message.

    This message should be sent back to vim when zorg is asked to open a link
    with a '::' separator. For example, a link of the form [[foo::bar]] should
    trigger the 'SEARCH bar' message.
    """
    open_action_main(str(lineno), zdir=db_zettel_dir)

    capture = capsys.readouterr()
    zo_path = db_zettel_dir / zo_name
    assert capture.err == ""
    assert capture.out.strip().split("\n") == [
        f"EDIT {zo_path}",
        f"SEARCH id::{link_prop}",
    ]


@fixture(name="open_action_main")
def open_action_main_fixture(main: c.MainType, zettel_dir: Path) -> c.MainType:
    """Wrapper for main() fixture that is tailered to 'action open' tests."""

    def open_action_main(*args: str, zdir: Path = None, **kwargs: Any) -> int:
        zdir = zdir or zettel_dir
        exit_code = main(
            "--log=null",
            "--dir",
            str(zdir),
            "action",
            "open",
            str(zdir / "links.zo"),
            *args,
            **kwargs,
        )
        assert exit_code == 0
        return exit_code

    return open_action_main
