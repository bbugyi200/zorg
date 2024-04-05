"""Tests that flex file group logic."""

from pathlib import Path

from zorg.service.file_groups import expand_file_group_paths

from . import common as c


def test_expand_file_group_paths() -> None:
    """Tests that file group path expansion is WAI."""
    paths = expand_file_group_paths(
        ["@foo", Path("buz.zo")],
        file_group_map={
            "foo": ["{days[0].year}/{yyyymmdd[0]}.zo", "@bar"],
            "bar": ["bar.zo"],
        },
    )
    assert paths == [
        Path(p)
        for p in (
            f"{c.YYYY}/{c.YYYY}{c.MM}{c.DD}.zo",
            "bar.zo",
            "buz.zo",
        )
    ]
