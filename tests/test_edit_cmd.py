"""Tests the zorg project's 'edit' CLI command."""

from __future__ import annotations

from pathlib import Path

from syrupy.assertion import SnapshotAssertion as Snapshot

from . import common as c


def test_edit_day_logs(
    main: c.MainType, tmp_path: Path, snapshot: Snapshot
) -> None:
    """Test that we properly generate test day, habit, and done logs."""
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

    day_log = f"{c.YYYY}/{c.YYYY}{c.MM}{c.DD}.zo"
    habit_log = f"{c.YYYY}/{c.YYYY}{c.MM}{c.YEST_DD}_habit.zo"
    done_log = f"{c.YYYY}/{c.YYYY}{c.MM}{c.DD}_done.zo"
    re_date_group = "(?P<date>[0-9]{4}[01][0-9][0-3][0-9])"
    exit_code = main(
        "--dir",
        str(zettel_dir),
        "edit",
        day_log,
        habit_log,
        done_log,
        template_pattern_map={
            f"^{re_date_group}_habit$": "habit_log_tmpl.zo",
            f"^{re_date_group}_done$": "done_log_tmpl.zo",
            f"^{re_date_group}$": "day_log_tmpl.zo",
        },
        **kwargs,
    )

    day_log_path = zettel_dir / day_log
    habit_log_path = zettel_dir / habit_log
    done_log_path = zettel_dir / done_log

    assert exit_code == 0
    assert day_log_path.read_text() == snapshot
    assert habit_log_path.read_text() == snapshot
    assert done_log_path.read_text() == snapshot
