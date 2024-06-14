"""Clack config for zorg."""

from __future__ import annotations

import itertools as it
from pathlib import Path
from typing import Any, Final, Literal, Optional, Sequence

import clack
from logrus import Logger
from typist import literal_to_list

from .. import APP_NAME
from ..domain.types import FileGroupMapType, TemplatePatternMapType, VarMapType
from ..service import common


Command = Literal[
    "compile",
    "create",
    "edit",
    "init",
    "list",
    "open",
    "query",
    "reindex",
    "render",
]

_LOGGER = Logger(__name__)

_DEFAULT_ZETTEL_DIR: Final[Path] = Path.home() / "org"


def _get_default_database_url(zdir: Path) -> str:
    return f"sqlite:///{zdir}/.{APP_NAME}/{APP_NAME}.db"


class Config(clack.Config):
    """Shared clack configuration class."""

    command: Command

    # ----- ARGUMENTS
    zettel_dir: Path = _DEFAULT_ZETTEL_DIR

    # ----- CONFIG
    database_url: str = _get_default_database_url(_DEFAULT_ZETTEL_DIR)
    template_pattern_map: TemplatePatternMapType = {}


class CompileConfig(Config):
    """Clack config for the 'compile' command."""

    command: Literal["compile"]

    # ----- ARGUMENTS
    zo_path: Path


class DbCreateConfig(Config):
    """Clack config for the 'db create' command."""

    command: Literal["create"]


class DbReindexConfig(Config):
    """Clack config for the 'db reindex' command."""

    command: Literal["reindex"]

    # ----- ARGUMENTS
    paths: list[Path] = []


class EditConfig(Config):
    """Clack config for the 'edit' command."""

    command: Literal["edit"]

    # ----- ARGUMENTS
    zo_paths: list[Path]

    # ----- CONFIG
    file_group_map: FileGroupMapType = {}
    keep_alive_file: Path = Path("/tmp/zorg_keep_alive")
    vim_commands: list[str] = []


class OpenActionConfig(Config):
    """Clack config for the 'action open' command."""

    command: Literal["open"]

    # ----- ARGUMENTS
    zo_path: Path
    line_number: int
    option_idx: Optional[int] = None


class QueryConfig(Config):
    """Clack config for the 'query' command."""

    command: Literal["query"]

    # ----- ARGUMENTS
    query: str


class TemplateListConfig(Config):
    """Clack config for the 'template' command."""

    command: Literal["list"]


class TemplateRenderConfig(Config):
    """Clack config for the 'template' command."""

    command: Literal["render"]

    # ----- ARGUMENTS
    template: Path
    var_map: VarMapType


class TemplateInitConfig(Config):
    """Clack config for the 'template' command."""

    command: Literal["init"]

    # ----- ARGUMENTS
    new_path: Path
    should_overwrite_existing: bool = False
    template: Optional[Path] = None
    var_map: Optional[VarMapType] = None


def clack_parser(argv: Sequence[str]) -> dict[str, Any]:
    """Parser we pass to the `main_factory()` `parser` kwarg."""
    # HACK: These make the command-line arguments more conveniant:
    #
    # * Make 'edit' the default sub-command.
    # * Make 'render' the default sub-sub-command for the 'template'
    #   sub-command.
    argv_before_opts = [argv[0]] + list(
        it.takewhile(lambda x: x.startswith("-"), argv[1:])
    )
    argv_after_opts = list(it.dropwhile(lambda x: x.startswith("-"), argv[1:]))
    if not argv_after_opts:
        _LOGGER.debug(
            "Inferring 'edit' command since no subcommand was specified."
        )
        argv = list(argv) + ["edit"]
    elif argv_after_opts[0].startswith("@"):
        argv = argv_before_opts + ["edit"] + argv_after_opts
        _LOGGER.debug(
            "Inferring 'edit' command since we found a file group name.",
            file_group_name=argv_after_opts[0],
            new_args=argv[1:],
        )
    elif (
        argv_after_opts[0] == "template"
        and len(argv_after_opts) > 1
        and argv_after_opts[1] not in literal_to_list(Command)
    ):
        argv = (
            argv_before_opts
            + [argv_after_opts[0], "render"]
            + argv_after_opts[1:]
        )
    elif argv_after_opts[0] == "template" and len(argv_after_opts) == 1:
        argv = argv_before_opts + [argv_after_opts[0], "render", ""]

    parser = clack.Parser(description="The zettel note manager of the future.")
    # --- Global Options
    parser.add_argument(
        "-d",
        "--dir",
        dest="zettel_dir",
        type=Path,
        help="The directory where all of your notes are stored.",
    )

    new_command = clack.new_command_factory(parser)

    # --- 'action' command
    action_parser = new_command(
        "action",
        help="Used to interface with vim via an action protocol.",
    )
    # --- 'action open' command
    new_action_command = clack.new_command_factory(action_parser)
    action_open_parser = new_action_command(
        "open",
        help=(
            "Open a zettel link if one exists on the provided zorg file line."
        ),
    )
    action_open_parser.add_argument(
        "zo_path",
        type=Path,
        help="The file that your editor currently has open.",
    )
    action_open_parser.add_argument(
        "line_number",
        type=int,
        help=(
            "The line number that your editor cursor is currently located on."
        ),
    )
    action_open_parser.add_argument(
        "option_idx",
        nargs="?",
        help=(
            "Used on a second 'action open' run to indicate which option was"
            " selected."
        ),
    )

    # --- 'compile' command
    compile_parser = new_command(
        "compile", help="Compiles zorg (*.zo) files into zorc (*.zoc) files."
    )
    compile_parser.add_argument(
        "zo_path", help="Path to the zorg file you want to compile."
    )

    # --- 'db' command
    db_parser = new_command(
        "db", help="Commands for managing Zorg's SQL database."
    )
    new_db_command = clack.new_command_factory(db_parser)
    # --- 'db create' command
    new_db_command(
        "create",
        help="Create zorg's backend database from scratch.",
    )
    # --- 'db reindex' command
    db_reindex_parser = new_db_command(
        "reindex",
        help="Reindex any changed files by adding them to the database.",
    )
    db_reindex_parser.add_argument(
        "paths",
        type=Path,
        nargs="*",
        help=(
            "Reindex these specific paths. If this argument is not provided,"
            " we use a hashing approach to check which files have changed."
        ),
    )

    # --- 'edit' command
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

    # --- 'query' command
    query_parser = new_command(
        "query", help="Run a zorg query against your zettel directory."
    )
    query_parser.add_argument("query", help="The zorg query we will run.")

    # --- 'template' command
    template_parser = new_command(
        "template", help="Commands for managing .zot templates."
    )
    new_template_command = clack.new_command_factory(template_parser)
    # --- 'template init' command
    template_init_parser = new_template_command(
        "init", help="Initialize a new file using a zorg template."
    )
    template_init_parser.add_argument(
        "new_path",
        type=Path,
        help="Path to the new file you would like to create.",
    )
    template_init_parser.add_argument(
        "-f",
        "--force",
        dest="should_overwrite_existing",
        action="store_true",
        help="Overwrite target file if the file already exists.",
    )
    template_init_parser.add_argument(
        "-t",
        "--template",
        type=Path,
        nargs=1,
        help=(
            "Optional path to the .zot template. If a template is not"
            " provided, we will infer what template to use based off of the"
            " new file's name."
        ),
    )
    template_init_parser.add_argument(
        "variables",
        nargs="*",
        help="A list of variable specs of the form of key=value.",
    )
    # --- 'template list' command
    new_template_command("list", help="List all zorg template files.")
    # --- 'template render' command
    template_render_parser = new_template_command(
        "render", help="Render a new .zo file using a .zot template."
    )
    template_render_parser.add_argument(
        "template", type=Path, help="Path to the .zot template."
    )
    template_render_parser.add_argument(
        "variables",
        nargs="*",
        help="A list of variable specs of the form of key=value.",
    )

    args = parser.parse_args(argv[1:])
    kwargs = clack.filter_cli_args(args)

    _convert_variables_to_var_map(kwargs)
    _process_zo_paths(kwargs)
    _process_query(kwargs)
    _fix_database_url(kwargs)

    return kwargs


def _fix_database_url(kwargs: dict[str, Any]) -> None:
    if "database_url" not in kwargs and (zdir := kwargs.get("zettel_dir")):
        kwargs["database_url"] = _get_default_database_url(zdir)


def _process_query(kwargs: dict[str, Any]) -> None:
    if kwargs["command"] != "query":
        return

    if not kwargs["query"].startswith(("S ", "W ")):
        query = kwargs["query"]
        kwargs["query"] = f"W {query}"

    if not kwargs["query"].startswith("S ") and " G " not in kwargs["query"]:
        query = kwargs["query"]
        kwargs["query"] = f"{query} G file"


def _process_zo_paths(kwargs: dict[str, Any]) -> None:
    if kwargs["command"] == "edit" and "zo_paths" not in kwargs:
        _LOGGER.debug(
            "The 'edit' command was invoked, but no file paths were specified."
            " Auto-adding the @default file group paths.",
            kwargs=kwargs,
        )
        kwargs["zo_paths"] = [Path("@default")]


def _convert_variables_to_var_map(kwargs: dict[str, Any]) -> None:
    if "variables" in kwargs:
        var_map = {}
        for var_spec in kwargs["variables"]:
            k, v = var_spec.split("=")
            var_map[k] = v
        var_map = common.process_var_map(var_map)
        kwargs["var_map"] = var_map
        del kwargs["variables"]
    elif kwargs["command"] == "render":
        kwargs["var_map"] = {}
