"""Clack config for zorg."""

from __future__ import annotations

import itertools as it
from pathlib import Path
from typing import Any, Literal, Sequence

import clack


Command = Literal["edit"]


class Config(clack.Config):
    """Shared clack configuration class."""

    command: Command

    zettel_dir: Path = Path.home() / "org"


class EditConfig(Config):
    """Clack config for the 'edit' command."""

    command: Literal["edit"]

    day_log_template: str = "day_log_tmpl.zo"
    habit_log_template: str = "habit_log_tmpl.zo"
    done_log_template: str = "done_log_tmpl.zo"
    vim_commands: list[str]


def clack_parser(argv: Sequence[str]) -> dict[str, Any]:
    """Parser we pass to the `main_factory()` `parser` kwarg."""
    # HACK: Make 'tui' the default sub-command.
    if not list(it.dropwhile(lambda x: x.startswith("-"), argv[1:])):
        argv = list(argv) + ["edit"]

    parser = clack.Parser(description="The zettel note manager of the future.")
    parser.add_argument(
        "-d",
        "--dir",
        dest="zettel_dir",
        type=Path,
        help="The directory where all of your notes are stored.",
    )

    new_command = clack.new_command_factory(parser)
    edit_parser = new_command("edit", help="Open day log in editor.")
    edit_parser.add_argument(
        "-D",
        "--day-log-template",
        help="Template used to generate day logs.",
    )
    edit_parser.add_argument(
        "-H",
        "--habit-log-template",
        help="Template used to generate habit trackers.",
    )
    edit_parser.add_argument(
        "-X",
        "--done-log-template",
        help="Template used to generate files for done todos.",
    )

    args = parser.parse_args(argv[1:])
    kwargs = clack.filter_cli_args(args)

    _preprocess_template_name(kwargs, "day_log_template")
    _preprocess_template_name(kwargs, "habit_log_template")
    _preprocess_template_name(kwargs, "done_log_template")

    return kwargs


def _preprocess_template_name(kwargs: dict[str, Any], key: str) -> None:
    if key in kwargs:
        kwargs[key] = kwargs[key] + "_tmpl.zo"