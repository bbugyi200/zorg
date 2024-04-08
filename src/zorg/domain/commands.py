"""Zorg commands."""

from dataclasses import dataclass
from pathlib import Path

from .types import Message


@dataclass(frozen=True)
class Command(Message):
    """A zorg command."""

    zettel_dir: Path


@dataclass(frozen=True)
class EditCommand(Command):
    """Command to open one or more zorg files using an editor."""

    paths: list[Path]
    keep_alive_file: Path
    vim_commands: list[str]


@dataclass(frozen=True)
class CreateDBCommand(Command):
    """Command to (re)create zorg's database from scratch."""
