"""Contains the ZorgSQLSession class."""

from __future__ import annotations

from functools import partial
from pathlib import Path
from types import TracebackType
from typing import Iterator, Type

from logrus import Logger
from potoroo import UnitOfWork
from sqlmodel import Session

from ...domain.types import CreateEngineType, Message
from .engine import create_cached_engine
from .repo import ZorgSQLRepo


logger = Logger(__name__)


class ZorgSQLSession(UnitOfWork[ZorgSQLRepo]):
    """Unit-of-work pattern used to manage transactions on zorg's SQL DB."""

    def __init__(
        self,
        db_url: str,
        *,
        engine_factory: CreateEngineType = create_cached_engine,
        create_new_database: bool = False,
        verbose: int = 0,
    ) -> None:
        # echo SQL statements to console if -vvv or greater is specified on the
        # command-line
        engine_kwargs = {}
        if verbose > 2:
            engine_kwargs["echo"] = True

        _prep_sqlite_db(db_url, should_delete=create_new_database)
        self._engine_factory = partial(engine_factory, db_url, **engine_kwargs)
        self._messages: list[Message] = []

        self._session: Session
        self._repo: ZorgSQLRepo

    def __enter__(self) -> ZorgSQLSession:
        """Called before entering a ZorgSQLSession with-block."""
        self._session = Session(self._engine_factory())
        self._repo = ZorgSQLRepo(self._session)
        return self

    def __exit__(
        self,
        exc_type: Type[BaseException] | None,
        exc_value: BaseException | None,
        traceback: TracebackType | None,
    ) -> None:
        """Called before exiting a ZorgSQLSession with-block."""
        del exc_type
        del exc_value
        del traceback

        self.rollback()
        self._session.close()

    def commit(self) -> None:
        """Commit our changes."""
        self._session.commit()

    def rollback(self) -> None:
        """Revert any changes made while in this ZorgSQLSession's with-block."""
        self._session.rollback()

    @property
    def repo(self) -> ZorgSQLRepo:
        """Returns the GreatRepo object associated with this ZorgSQLSession."""
        return self._repo

    def send_message(self, message: Message) -> None:
        """Register a message to be handled by the message bus."""
        self._messages.append(message)

    def collect_new_messages(self) -> Iterator[Message]:
        """Collect new events/commands for our messagebus to process."""
        while self._messages:
            yield self._messages.pop(0)

        for zorg_file in self.repo.seen:
            while zorg_file.messages:
                yield zorg_file.messages.pop(0)


def _prep_sqlite_db(database_url: str, should_delete: bool = False) -> None:
    """Ensure sqlite DB file exists and delete if {should_delete} is True."""
    sqlite_prefix = "sqlite:///"
    if database_url.startswith(sqlite_prefix):
        db_path = Path(database_url[len(sqlite_prefix) :])
        db_path.parent.mkdir(exist_ok=True, parents=True)
        if db_path.exists() and should_delete:
            logger.info("Deleting existing zorg database.", db_path=db_path)
            db_path.unlink()
