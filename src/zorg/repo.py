"""Contains the Repo class."""

from __future__ import annotations

from typing import TypeVar

from eris import ErisResult, Ok
from logrus import Logger
from potoroo import TaggedRepo

from . import db
from .models import OrZorgQuery, ZorgNote
from .types import CreateEngineType


logger = Logger(__name__)

T = TypeVar("T")


class ZorgSQLRepo(TaggedRepo[str, ZorgNote, OrZorgQuery]):
    """Repo that stores Todos in sqlite database."""

    def __init__(
        self,
        url: str,
        *,
        engine_factory: CreateEngineType = db.create_cached_engine,
        verbose: int = 0,
    ) -> None:
        # echo SQL statements to console if -vvv or greater is specified on the
        # command-line
        engine_kwargs = {}
        if verbose > 2:
            engine_kwargs["echo"] = True

        self.url = url
        self.engine = engine_factory(url, **engine_kwargs)

    def add(self, note: ZorgNote, /, *, key: str = None) -> ErisResult[str]:
        """Adds a new Todo to the DB.

        Returns a unique identifier that has been associated with this Todo.
        """
        del note, key
        return Ok("")

    def get(self, key: str) -> ErisResult[ZorgNote | None]:
        """Retrieve a Todo from the DB."""
        del key
        return Ok(None)

    def remove(self, key: str) -> ErisResult[ZorgNote | None]:
        """Remove a Todo from the DB."""
        del key
        return Ok(None)

    def get_by_tag(self, tag: OrZorgQuery) -> ErisResult[list[ZorgNote]]:
        """Get Todo(s) from DB by using a tag."""
        del tag
        return Ok([])

    def remove_by_tag(self, tag: OrZorgQuery) -> ErisResult[list[ZorgNote]]:
        """Removes Todo(s) from DB by using a tag."""
        del tag
        return Ok([])

    def all(self) -> ErisResult[list[ZorgNote]]:
        """Returns all Todos contained in the underlying SQL database."""
        return Ok([])
