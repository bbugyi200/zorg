"""Clack config for zorg."""

from __future__ import annotations

import argparse
import itertools as it
from pathlib import Path
from typing import Any, Literal, Pattern, Sequence

import clack
from logrus import Logger

from . import common


Command = Literal["edit", "new"]

logger = Logger(__name__)


class Config(clack.Config):
    """Shared clack configuration class."""

    command: Command

    template_pattern_map: dict[Pattern, Path]
    zettel_dir: Path = Path.home() / "org"


class EditConfig(Config):
    """Clack config for the 'edit' command."""

    command: Literal["edit"]

    # ----- CONFIG
    file_group_map: dict[str, list[str]] = {}
    keep_alive_file: Path = Path("/tmp/zorg_keep_alive")
    vim_commands: list[str] = []

    # ----- ARGUMENTS
    zo_paths: list[Path]
    # TODO(bugyi): Rename to dry_run
    edit_day_log: bool = True


class NewConfig(Config):
    """Clack config for the 'new' command."""

    command: Literal["new"]

    # ----- ARGUMENTS
    template: Path
    var_map: dict[str, Any]


def clack_parser(argv: Sequence[str]) -> dict[str, Any]:
    """Parser we pass to the `main_factory()` `parser` kwarg."""
    # HACK: Make 'edit' the default sub-command.
    argv_after_opts = list(it.dropwhile(lambda x: x.startswith("-"), argv[1:]))
    if not argv_after_opts:
        logger.debug(
            "Inferring 'edit' command since no subcommand was specified."
        )
        argv = list(argv) + ["edit"]
    elif argv_after_opts[0].startswith("@"):
        argv_opts = list(it.takewhile(lambda x: x.startswith("-"), argv[1:]))
        argv = [argv[0]] + argv_opts + ["edit"] + argv_after_opts
        logger.debug(
            "Inferring 'edit' command since we found a file group name.",
            file_group_name=argv_after_opts[0],
            new_args=argv[1:],
        )

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
        "zo_paths",
        type=Path,
        nargs="*",
        help="The .zo files we want to open in an editor.",
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

    _convert_variables_to_var_map(kwargs)
    _process_zo_paths(kwargs)

    return kwargs


def _process_zo_paths(kwargs: dict[str, Any]) -> None:
    if kwargs["command"] == "edit" and "zo_paths" not in kwargs:
        logger.debug(
            "The 'edit' command was invoked, but no file paths were specified."
            " Auto-adding the @default file group paths.",
            kwargs=kwargs,
        )
        kwargs["zo_paths"] = ["@default"]


def _convert_variables_to_var_map(kwargs: dict[str, Any]) -> None:
    if "variables" in kwargs:
        var_map = {}
        for var_spec in kwargs["variables"].split(","):
            k, v = var_spec.split("=")
            var_map[k] = v
        var_map = common.process_var_map(var_map)
        kwargs["var_map"] = var_map
        del kwargs["variables"]
