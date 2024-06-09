"""Tests the zorg project's 'edit' CLI command."""

from __future__ import annotations

from pathlib import Path
from typing import Any
from unittest.mock import Mock

from syrupy.assertion import SnapshotAssertion as Snapshot

from . import common as c


def test_edit_day_logs(
    main: c.MainType, vim_proc_mock: Mock, zettel_dir: Path, snapshot: Snapshot
) -> None:
    """Test that we properly generate test day, habit, and done logs."""
    day_log = f"{c.YYYY}/{c.YYYY}{c.MM}{c.DD}.zo"
    habit_log = f"{c.YYYY}/{c.YYYY}{c.MM}{c.YEST_DD}_habit.zo"
    done_log = f"{c.YYYY}/{c.YYYY}{c.MM}{c.DD}_done.zo"
    re_date_group = "(?P<date>[0-9]{4}[01][0-9][0-3][0-9])"
    kwargs: dict[str, Any] = {
        "vim_commands": ["echo hi", "source {zdir}/vimrc"]
    }
    exit_code = main(
        "--dir",
        str(zettel_dir),
        "edit",
        day_log,
        habit_log,
        done_log,
        template_pattern_map={
            f"^{c.YYYY}/{re_date_group}_habit.zo$": "habit_log.zot",
            f"^{c.YYYY}/{re_date_group}_done.zo$": "done_log.zot",
            f"^{c.YYYY}/{re_date_group}.zo$": "day_log.zot",
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
            "echo hi",
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
    main: c.MainType, vim_proc_mock: Mock, tmp_path: Path, snapshot: Snapshot
) -> None:
    """Test that we can use the keep alive file to change our vim file args."""
    zettel_dir = tmp_path / "org"

    keep_alive_file = tmp_path / "zorg_keep_alive"
    keep_alive_file.write_text("baz.zo buz.zo buz.zo")
    exit_code = main(
        "--dir",
        str(zettel_dir),
        "edit",
        "foobar.zo",
        keep_alive_file=keep_alive_file,
    )

    assert exit_code == 0
    assert [
        [cmd_part.replace(str(tmp_path), "<TMP>") for cmd_part in call.args[0]]
        for call in vim_proc_mock.mock_calls
        if call.args
    ] == snapshot
    assert vim_proc_mock.call_count == 2
    assert not keep_alive_file.exists()
