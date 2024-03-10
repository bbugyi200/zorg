"""Tests the zorg project's 'edit' CLI command."""

from __future__ import annotations

from pathlib import Path
from typing import Any
from unittest.mock import Mock, call

from syrupy.assertion import SnapshotAssertion as Snapshot

from . import common as c


def test_edit_day_logs(
    main: c.MainType, vim_proc_mock: Mock, tmp_path: Path, snapshot: Snapshot
) -> None:
    """Test that we properly generate test day, habit, and done logs."""
    zettel_dir = tmp_path / "org"
    kwargs: dict[str, Any] = {"vim_commands": ["source {zdir}/vimrc"]}
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
        template_path.write_bytes(test_data_template_path.read_bytes())
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
            f"^{re_date_group}_habit.zo$": "habit_log_tmpl.zo",
            f"^{re_date_group}_done.zo$": "done_log_tmpl.zo",
            f"^{re_date_group}.zo$": "day_log_tmpl.zo",
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
    vim_proc_mock.assert_called_once_with(
        [
            "vim",
            str(day_log_path),
            str(habit_log_path),
            str(done_log_path),
            "-c",
            f"source {zettel_dir}/vimrc",
        ],
        stdout=None,
        stderr=None,
        timeout=None,
    )


def test_whenEmptyKeepAliveFileExists_shouldRestartVim(
    main: c.MainType, vim_proc_mock: Mock, tmp_path: Path
) -> None:
    """Test that we can use the keep alive file to have zorg re-run vim."""
    zettel_dir = tmp_path / "org"

    keep_alive_file = tmp_path / "zorg_keep_alive"
    keep_alive_file.touch()
    exit_code = main(
        "--dir",
        str(zettel_dir),
        "edit",
        "foobar.zo",
        keep_alive_file=keep_alive_file,
    )

    assert exit_code == 0
    vim_proc_mock.assert_called_with(
        ["vim", str(zettel_dir / "foobar.zo")],
        stdout=None,
        stderr=None,
        timeout=None,
    )
    assert vim_proc_mock.call_count == 2
    assert not keep_alive_file.exists()


def test_whenKeepAliveFileContainsPaths_useThosePathsOnRestart(
    main: c.MainType, vim_proc_mock: Mock, tmp_path: Path
) -> None:
    """Test that we can use the keep alive file to change our vim file args."""
    zettel_dir = tmp_path / "org"

    keep_alive_file = tmp_path / "zorg_keep_alive"
    keep_alive_file.write_text("baz.zo buz.zo")
    exit_code = main(
        "--dir",
        str(zettel_dir),
        "edit",
        "foobar.zo",
        keep_alive_file=keep_alive_file,
    )

    assert exit_code == 0
    vim_proc_mock.assert_has_calls([
        call(
            ["vim", str(zettel_dir / "foobar.zo")],
            stdout=None,
            stderr=None,
            timeout=None,
        ),
        call().unwrap(),
        call(
            ["vim", str(zettel_dir / "baz.zo"), str(zettel_dir / "buz.zo")],
            stdout=None,
            stderr=None,
            timeout=None,
        ),
        call().unwrap(),
    ])
    assert vim_proc_mock.call_count == 2
    assert not keep_alive_file.exists()
