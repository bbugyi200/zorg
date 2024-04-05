"""Tests the zorg project's clack config parser."""

from pathlib import Path
from typing import Any, Sequence, cast

from clack import clack_envvars_set
from clack.types import ClackConfig

from zorg.app.config import EditConfig, TemplateRenderConfig, clack_parser


def test_defaultToEdit_whenNoCommandIsGiven() -> None:
    """Default to 'edit' when no subcommand is explicitly specified.

    When no subcommand is provided, default to using the 'edit' command with
    the default file group (i.e. @default).
    """
    kwargs = wrapped_clack_parser([""])
    assert kwargs == {"command": "edit", "zo_paths": [Path("@default")]}


def test_defaultToEdit_whenFileGroupNameIsFirstArg() -> None:
    """Default to 'edit' when a file group name is the first arg.

    When a file group name (e.g. @foo) is the first positional arg (e.g.
    non-option) and no subcommand was provided, default to using the 'edit'
    command.
    """
    kwargs = wrapped_clack_parser(["", "@foo"])
    assert kwargs == {"command": "edit", "zo_paths": [Path("@foo")]}


def wrapped_clack_parser(argv: Sequence[str]) -> dict[str, Any]:
    """Thin wrapper around clack_parser()."""
    with clack_envvars_set(
        "zorg",
        cast(list[type[ClackConfig]], [EditConfig, TemplateRenderConfig]),
    ):
        return clack_parser(argv)
