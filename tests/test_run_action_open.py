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
    tmp_path: Path,
    lineno: int,
    expected: str,
) -> None:
    """Test that the OPEN_LINK action is WAI."""
    zettel_dir = tmp_path / "org"
    zettel_dir.mkdir(parents=True, exist_ok=True)
    path_to_links = Path(__file__).parent / Path("data/links.zo")
    zpath_to_links = zettel_dir / "links.zo"
    zpath_to_links.write_bytes(path_to_links.read_bytes())

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
