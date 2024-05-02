"""Zorg commands."""

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Command:
    """A zorg command."""

    zettel_dir: Path


@dataclass(frozen=True)
class EditCommand(Command):
    """Command to open one or more zorg files using an editor."""

    paths: list[Path]
    keep_alive_file: Path
    vim_commands: list[str]
    verbose: int = 0


@dataclass(frozen=True)
class CreateDBCommand(Command):
    """Command to (re)create zorg's database from scratch."""


@dataclass(frozen=True)
class ReindexDBCommand(Command):
    """Command to reindex an existing zorg database."""

    paths: list[Path]
    verbose: bool = False
