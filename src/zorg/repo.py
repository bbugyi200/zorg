"""Contains the Repo class."""

from __future__ import annotations

from eris import ErisResult, Ok
from logrus import Logger
from potoroo import TaggedRepo
from sqlmodel import Session, select

from . import model_converter, models, sql_models


logger = Logger(__name__)


class ZorgSQLRepo(TaggedRepo[str, models.ZorgNote, models.OrZorgQuery]):
    """Repo that stores zorg notes in sqlite database."""

    def __init__(
        self,
        session: Session,
    ) -> None:
        self._session = session

    def add(
        self, note: models.ZorgNote, /, *, key: str = None
    ) -> ErisResult[str]:
        """Adds a new note to the DB.

        Returns a unique identifier that has been associated with this note.
        """
        del key
        self._session.add(note)
        # TODO(bugyi): Add ID generation logic here, which should add an event to the message bus.
        assert note.ident is not None
        return Ok(str(note.ident))

    def remove(
        self, note: models.ZorgNote, /  # noqa: W504
    ) -> ErisResult[models.ZorgNote | None]:
        """Remove a note from the DB."""
        self._session.delete(note)
        return Ok(note)

    def get(self, key: str) -> ErisResult[models.ZorgNote | None]:
        """Retrieve a note from the DB."""
        stmt = select(sql_models.ZorgNote).where(
            sql_models.ZorgNote.id == int(key)
        )
        results = self._session.exec(stmt)
        sql_note = results.first()
        if sql_note:
            return Ok(model_converter.sql_note_to_model(sql_note))
        else:
            return Ok(None)

    def get_by_tag(
        self, tag: models.OrZorgQuery
    ) -> ErisResult[list[models.ZorgNote]]:
        """Get note(s) from DB by using a tag."""
        del tag
        return Ok([])

    def all(self) -> ErisResult[list[models.ZorgNote]]:
        """Returns all zorg notes contained in the underlying SQL database."""
        stmt = select(sql_models.ZorgNote)
        return Ok([
            model_converter.sql_note_to_model(sql_note)
            for sql_note in self._session.exec(stmt).all()
        ])
