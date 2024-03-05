"""Tests the zorg project's 'edit' CLI command."""

from __future__ import annotations

from pathlib import Path

from syrupy.assertion import SnapshotAssertion as Snapshot

from . import common as c


def test_edit(main: c.MainType, tmp_path: Path, snapshot: Snapshot) -> None:
    """Test the 'edit' subcommand."""
    zettel_dir = tmp_path / "org"
    kwargs = {}
    for key, stem in [
        ("day_log_template", "day_log_tmpl"),
        ("habit_log_template", "habit_log_tmpl"),
        ("done_log_template", "done_log_tmpl"),
    ]:
        template_path: Path = zettel_dir / f"{stem}.zo"
        template_path.parent.mkdir(parents=True, exist_ok=True)
        test_data_template_path = Path(__file__).parent / Path(
            f"data/{stem}.zo"
        )
        template_path.write_text(test_data_template_path.read_text())
        kwargs[key] = template_path.name

    assert main("--dir", str(zettel_dir), "edit", **kwargs) == 0

    day_log_path = zettel_dir / c.YYYY / (c.YYYY + c.MM + c.DD + ".zo")
    habit_log_path = (
        zettel_dir / c.YYYY / (c.YYYY + c.MM + c.YEST_DD + "_habit.zo")
    )
    done_log_path = zettel_dir / c.YYYY / (c.YYYY + c.MM + c.DD + "_done.zo")

    assert day_log_path.read_text() == snapshot
    assert habit_log_path.read_text() == snapshot
    assert done_log_path.read_text() == snapshot
