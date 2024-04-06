"""Tests for the zorg project's 'action' CLI command."""

from __future__ import annotations

from pathlib import Path

from _pytest.capture import CaptureFixture
from pytest import mark

from . import common as c


params = mark.parametrize


@params(
    "lineno,expected",
    [(3, "foo.zo"), (5, "bar.sh"), (6, "baz.zo"), (7, "buz.zo")],
)
def test_action_open(
    main: c.MainType,
    capsys: CaptureFixture,
    zettel_dir: Path,
    lineno: int,
    expected: str,
) -> None:
    """Test that the OPEN_LINK action is WAI."""
    zpath_to_links = zettel_dir / "links.zo"
    exit_code = main(
        "--dir",
        str(zettel_dir),
        "action",
        "open",
        str(zpath_to_links),
        str(lineno),
    )

    assert exit_code == 0
    capture = capsys.readouterr()
    assert capture.out == f"EDIT {zettel_dir}/{expected}\n"
