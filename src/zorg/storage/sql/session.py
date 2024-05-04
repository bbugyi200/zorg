"""Contains the SQLSession class."""

from __future__ import annotations

from functools import partial
from pathlib import Path
from types import TracebackType
from typing import Iterator, Type

from logrus import Logger
from sqlmodel import Session

from ...domain.messages import Message
from ...domain.types import CreateEngineType
from .engine import create_cached_engine
from .repo import SQLRepo


_LOGGER = Logger(__name__)


class SQLSession:
    """Unit-of-work pattern used to manage transactions on zorg's SQL DB.

    TODO: Document __init__() params here.
    """

    def __init__(
        self,
        zettel_dir: Path,
        db_url: str,
        *,
        engine_factory: CreateEngineType = create_cached_engine,
        should_delete_existing_db: bool = False,
        verbose: int = 0,
    ) -> None:
        # echo SQL statements to console if -vvv or greater is specified on the
        # command-line
        engine_kwargs = {}
        if verbose > 2:
            engine_kwargs["echo"] = True

        _prep_sqlite_db(db_url, should_delete=should_delete_existing_db)
        self._engine_factory = partial(engine_factory, db_url, **engine_kwargs)
        self._zettel_dir = zettel_dir
        self._messages: list[Message] = []
        self._last_messages: list[Message] = []
        self._verbose = verbose

        self._session: Session
        self._repo: SQLRepo

    def __enter__(self) -> SQLSession:
        """Called before entering a SQLSession with-block."""
        self._session = Session(self._engine_factory())
        self._repo = SQLRepo(
            self._zettel_dir, self._session, verbose=self._verbose
        )
        return self

    def __exit__(
        self,
        exc_type: Type[BaseException] | None,
        exc_value: BaseException | None,
        traceback: TracebackType | None,
    ) -> None:
        """Called before exiting a SQLSession with-block."""
        del exc_type
        del exc_value
        del traceback

        self.rollback()
        self._session.close()

    def commit(self) -> None:
        """Commit our changes."""
        self._session.commit()

    def rollback(self) -> None:
        """Revert any changes made while in this SQLSession's with-block."""
        self._session.rollback()

    @property
    def repo(self) -> SQLRepo:
        """Returns the GreatRepo object associated with this SQLSession."""
        return self._repo

    def add_message(self, message: Message) -> None:
        """Register a message to be handled by the message bus first.

        These messages will be processed BEFORE any messages attached to domain
        entities (e.g. zorg files).
        """
        self._messages.append(message)

    def add_last_message(self, message: Message) -> None:
        """Register a message to be handled by the message bus last.

        These messages will be processed AFTER any messages attached to domain
        entities (e.g. zorg files).
        """
        self._last_messages.append(message)

    def collect_new_messages(self) -> Iterator[Message]:
        """Collect new events/commands for our messagebus to process."""
        while self._messages or any(file.events for file in self.repo.seen):
            while self._messages:
                yield self._messages.pop(0)

            for zorg_file in self.repo.seen:
                while zorg_file.events:
                    yield zorg_file.events.pop(0)

        while self._last_messages:
            yield self._last_messages.pop(0)


def _prep_sqlite_db(database_url: str, should_delete: bool = False) -> None:
    """Ensure sqlite DB file exists and delete if {should_delete} is True."""
    sqlite_prefix = "sqlite:///"
    if database_url.startswith(sqlite_prefix):
        db_path = Path(database_url[len(sqlite_prefix) :])
        db_path.parent.mkdir(exist_ok=True, parents=True)
        if db_path.exists() and should_delete:
            _LOGGER.info("Deleting existing zorg database.", db_path=db_path)
            db_path.unlink()
