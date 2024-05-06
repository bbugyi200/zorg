"""Tests for the zorg project's 'action' CLI command."""

from __future__ import annotations

from pathlib import Path

from _pytest.capture import CaptureFixture
from pytest import fixture, mark
from syrupy.assertion import SnapshotAssertion as Snapshot

from . import common as c


params = mark.parametrize


@params(
    "lineno,expected",
    [(3, "foo.zo"), (5, "bar.sh"), (6, "baz.zo"), (7, "buz.zo")],
)
def test_action_open__good(
    open_action_main: c.MainType,
    capsys: CaptureFixture,
    zettel_dir: Path,
    lineno: int,
    expected: str,
) -> None:
    """Test that the OPEN_LINK action is WAI."""
    open_action_main(str(lineno))

    capture = capsys.readouterr()
    assert capture.err == ""
    assert capture.out == f"EDIT {zettel_dir}/{expected}\n"


@params("lineno", [8])
def test_action_open__bad(
    open_action_main: c.MainType,
    capsys: CaptureFixture,
    snapshot: Snapshot,
    lineno: int,
) -> None:
    """Test that the OPEN_LINK action is WAI."""
    open_action_main(str(lineno))

    capture = capsys.readouterr()
    assert capture.err == ""
    assert capture.out == snapshot


@fixture(name="open_action_main")
def open_action_main_fixture(main: c.MainType, zettel_dir: Path) -> c.MainType:
    """Wrapper for main() fixture that is tailered to 'action open' tests."""
    zpath_to_links = zettel_dir / "links.zo"

    def open_action_main(*args, **kwargs) -> int:
        exit_code = main(
            "--log=null",
            "--dir",
            str(zettel_dir),
            "action",
            "open",
            str(zpath_to_links),
            *args,
            **kwargs,
        )
        assert exit_code == 0
        return exit_code

    return open_action_main
