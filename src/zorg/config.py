"""Clack config for zorg."""

from __future__ import annotations

import argparse
import datetime as dt
import itertools as it
from pathlib import Path
import re
from typing import Any, Literal, Sequence

import clack


Command = Literal["edit", "new"]


class Config(clack.Config):
    """Shared clack configuration class."""

    command: Command

    zettel_dir: Path = Path.home() / "org"


class EditConfig(Config):
    """Clack config for the 'edit' command."""

    command: Literal["edit"]

    # ----- CONFIG
    vim_commands: list[str] = []

    # ----- ARGUMENTS
    day_log_template: Path = Path("day_log_tmpl.zo")
    habit_log_template: Path = Path("habit_log_tmpl.zo")
    done_log_template: Path = Path("done_log_tmpl.zo")
    edit_day_log: bool = True


class NewConfig(Config):
    """Clack config for the 'new' command."""

    command: Literal["new"]

    # ----- ARGUMENTS
    template: Path
    var_map: dict[str, Any]


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
    edit_parser = new_command(
        "edit",
        help=(
            "Generate new day logs from templates and open the main day log in"
            " your system's editor. This is the default subcommand."
        ),
    )
    edit_parser.add_argument(
        "-D",
        "--day-log-template",
        type=Path,
        help="Template used to generate day logs.",
    )
    edit_parser.add_argument(
        "-H",
        "--habit-log-template",
        type=Path,
        help="Template used to generate habit trackers.",
    )
    edit_parser.add_argument(
        "-X",
        "--done-log-template",
        type=Path,
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

    new_parser = new_command(
        "new", help="Render a new .zo file using a .zot template."
    )
    new_parser.add_argument(
        "template", type=Path, help="Path to the .zot template."
    )
    new_parser.add_argument(
        "variables",
        help="A list of comma-separated variable specs of the form key=value.",
    )

    args = parser.parse_args(argv[1:])
    kwargs = clack.filter_cli_args(args)

    _preprocess_template_name(kwargs, "day_log_template")
    _preprocess_template_name(kwargs, "habit_log_template")
    _preprocess_template_name(kwargs, "done_log_template")

    _convert_variables_to_var_map(kwargs)

    return kwargs


def _convert_variables_to_var_map(kwargs: dict[str, Any]) -> None:
    if "variables" in kwargs:
        var_map = {}
        for var_spec in kwargs["variables"].split(","):
            k, v = var_spec.split("=")
            var_map[k] = _var_map_value(v)
        if any(isinstance(v, dt.datetime) for v in var_map.values()):
            var_map["one_day"] = dt.timedelta(days=1)
        kwargs["var_map"] = var_map
        del kwargs["variables"]


def _var_map_value(value: str) -> Any:
    if re.match("^[0-9]{4}[01][0-9][0-3][0-9]$", value):
        return dt.datetime.strptime(value, "%Y%m%d")
    return value


def _preprocess_template_name(kwargs: dict[str, Any], key: str) -> None:
    if key in kwargs:
        kwargs[key] = kwargs[key] + "_tmpl.zo"
