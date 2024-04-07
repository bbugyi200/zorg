"""Zorg commands."""

from dataclasses import dataclass
from pathlib import Path

from .types import Message


@dataclass(frozen=True)
class Command(Message):
    """A zorg command."""


@dataclass(frozen=True)
class EditCommand(Command):
    """Command to open one or more zorg files using an editor."""

    zettel_dir: Path
    paths: list[Path]
    keep_alive_file: Path
    vim_commands: list[str]


@dataclass(frozen=True)
class CheckKeepAliveFileCommand(EditCommand):
    """Command to check for the existance of a 'keep alive' file.

    If the file exists, we run the {EditCommand} using either the most recently
    edited zorg files, if the keep alive file is empty, or a list of zorg files
    specified by the contents of the keep alive file.
    """
