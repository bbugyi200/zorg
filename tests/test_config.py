"""Tests the zorg project's clack config parser."""

from pathlib import Path

from clack import clack_envvars_set

from zorg.config import EditConfig, NewConfig, clack_parser


all_config_types = [EditConfig, NewConfig]


def test_defaultToEdit_whenNoCommandIsGiven():
    """Default to 'edit' when no subcommand is explicitly specified.

    When no subcommand is provided, default to using the 'edit' command with
    the default file group (i.e. @default).
    """
    with clack_envvars_set("zorg", all_config_types):
        kwargs = clack_parser([""])
    assert kwargs == {"command": "edit", "zo_paths": [Path("@default")]}


def test_defaultToEdit_whenFileGroupNameIsFirstArg():
    """Default to 'edit' when a file group name is the first arg.

    When a file group name (e.g. @foo) is the first positional arg (e.g.
    non-option) and no subcommand was provided, default to using the 'edit'
    command.
    """
    with clack_envvars_set("zorg", all_config_types):
        kwargs = clack_parser(["", "@foo"])
    assert kwargs == {"command": "edit", "zo_paths": [Path("@foo")]}
