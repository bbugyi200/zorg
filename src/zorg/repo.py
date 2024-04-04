"""Contains the Repo class."""

from __future__ import annotations

from typing import TypeVar

from eris import ErisResult, Ok
from logrus import Logger
from potoroo import TaggedRepo
from sqlmodel import Session

from .models import OrZorgQuery, ZorgNote


logger = Logger(__name__)

T = TypeVar("T")


class ZorgSQLRepo(TaggedRepo[str, ZorgNote, OrZorgQuery]):
    """Repo that stores zorg notes in sqlite database."""

    def __init__(
        self,
        session: Session,
    ) -> None:
        self.session = session

    def add(self, note: ZorgNote, /, *, key: str = None) -> ErisResult[str]:
        """Adds a new note to the DB.

        Returns a unique identifier that has been associated with this note.
        """
        del note, key
        return Ok("")

    def remove(self, note: ZorgNote, /) -> ErisResult[ZorgNote | None]:
        """Remove a note from the DB."""
        del note
        return Ok(None)

    def get(self, key: str) -> ErisResult[ZorgNote | None]:
        """Retrieve a note from the DB."""
        del key
        return Ok(None)

    def get_by_tag(self, tag: OrZorgQuery) -> ErisResult[list[ZorgNote]]:
        """Get note(s) from DB by using a tag."""
        del tag
        return Ok([])

    def all(self) -> ErisResult[list[ZorgNote]]:
        """Returns all zorg notes contained in the underlying SQL database."""
        return Ok([])
