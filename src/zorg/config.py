"""Clack config for zorg."""

from __future__ import annotations

import argparse
import itertools as it
from pathlib import Path
from typing import Any, Literal, Sequence

import clack


Command = Literal["day"]


class Config(clack.Config):
    """Shared clack configuration class."""

    command: Command

    zettel_dir: Path = Path.home() / "org"


class DayConfig(Config):
    """Clack config for the 'day' command."""

    command: Literal["day"]

    # ----- CONFIG
    vim_commands: list[str] = []

    # ----- ARGUMENTS
    day_log_template: str = "day_log_tmpl.zo"
    habit_log_template: str = "habit_log_tmpl.zo"
    done_log_template: str = "done_log_tmpl.zo"
    edit_day_log: bool = True


def clack_parser(argv: Sequence[str]) -> dict[str, Any]:
    """Parser we pass to the `main_factory()` `parser` kwarg."""
    # HACK: Make 'tui' the default sub-command.
    if not list(it.dropwhile(lambda x: x.startswith("-"), argv[1:])):
        argv = list(argv) + ["day"]

    parser = clack.Parser(description="The zettel note manager of the future.")
    parser.add_argument(
        "-d",
        "--dir",
        dest="zettel_dir",
        type=Path,
        help="The directory where all of your notes are stored.",
    )

    new_command = clack.new_command_factory(parser)
    edit_parser = new_command(
        "day",
        help=(
            "Generate new day logs from templates and open the main day log in"
            " your system's editor. This is the default subcommand."
        ),
    )
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
    edit_parser.add_argument(
        "--edit-day-log",
        action=argparse.BooleanOptionalAction,
        help=(
            "Should we open the main day log for editing? It is useful to"
            " disable editing when testing day log generation from templates."
        ),
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
