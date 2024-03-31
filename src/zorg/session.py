"""Contains the ZorgSession class."""

from __future__ import annotations

from types import TracebackType
from typing import Type

from logrus import Logger
from potoroo import UnitOfWork

from .repo import ZorgSQLRepo


logger = Logger(__name__)


class ZorgSession(UnitOfWork[ZorgSQLRepo]):
    """Each time todos are opened in an editor, a new session is created."""

    def __init__(
        self,
        db_url: str,
        *,
        verbose: int = 0,
    ) -> None:
        self._repo = ZorgSQLRepo(db_url, verbose=verbose)

    def __enter__(self) -> ZorgSession:
        """Called before entering a ZorgSession with-block."""
        return self

    def __exit__(
        self,
        exc_type: Type[BaseException] | None,
        exc_value: BaseException | None,
        traceback: TracebackType | None,
    ) -> None:
        """Called before exiting a ZorgSession with-block."""
        del exc_type
        del exc_value
        del traceback

    def commit(self) -> None:
        """Commit our changes."""
        return

    def rollback(self) -> None:
        """Revert any changes made while in this ZorgSession's with-block."""

    @property
    def repo(self) -> ZorgSQLRepo:
        """Returns the GreatRepo object associated with this ZorgSession."""
        return self._repo
