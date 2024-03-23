"""Tests for the zorg project's 'compile' CLI command."""

from __future__ import annotations

from pathlib import Path
from typing import Iterator

from _pytest.capture import CaptureFixture
from pytest import mark
from syrupy.assertion import SnapshotAssertion as Snapshot
from typist import PathLike

from . import common as c


params = mark.parametrize


def _get_all_zo_stems(src_dir: PathLike = None) -> list[str]:
    return list(
        stem
        for stem in _get_zo_stem_iter(src_dir)
        if not stem.endswith("_tmpl")
    )


def _get_zo_stem_iter(src_dir: PathLike = None) -> Iterator[str]:
    if src_dir is None:
        src_dir = Path(__file__).parent / "data"
    else:
        src_dir = Path(src_dir)
    for zo_path in src_dir.glob("*.zo"):
        yield zo_path.stem


@params("zo_path", _get_all_zo_stems())
def test_compile(
    main: c.MainType,
    capsys: CaptureFixture,
    tmp_path: Path,
    snapshot: Snapshot,
    zo_path: PathLike,
) -> None:
    """Test that the all *.zo test data files compile as expected."""
    zettel_dir = tmp_path / "org"
    zo_with_ext = str(zo_path).replace(".zo", "") + ".zo"
    zo_path = Path(__file__).parent / f"data/{zo_with_ext}"

    argv = [
        "--dir",
        str(zettel_dir),
        "compile",
        str(zo_path),
    ]
    exit_code = main(*argv)

    assert exit_code == 0
    capture = capsys.readouterr()
    assert capture.out == snapshot
