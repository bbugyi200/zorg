"""Contains the Repo class."""

# pylint: disable=unsubscriptable-object

from __future__ import annotations

from pathlib import Path
from typing import Optional

from eris import ErisResult, Ok
from logrus import Logger
from sqlmodel import Session, select

from . import models as sql
from ...domain.messages.events import NewZorgNotesEvent
from ...domain.models import File, Note, WhereOrFilter
from ...service.zid_manager import ZIDManager
from .converters import ZorgFileConverter, ZorgNoteConverter, to_select_of_note


_LOGGER = Logger(__name__)


class SQLRepo:
    """Repo that stores zorg notes in sqlite database."""

    def __init__(
        self, zettel_dir: Path, session: Session, *, verbose: int = 0
    ) -> None:
        self._zettel_dir = zettel_dir
        self._session = session
        self._converter = ZorgFileConverter(zettel_dir, session)
        self._note_converter = ZorgNoteConverter(session)
        self._verbose = verbose

        self.seen: list[File] = []

    def add(self, zorg_file: File, /, *, key: str = None) -> ErisResult[str]:
        """Adds a new file to the DB.

        Returns a unique identifier that has been associated with this file.
        """
        del key
        self._seen_zorg_file(zorg_file)
        _add_zids(self._zettel_dir, zorg_file)
        sql_zorg_file = self._converter.from_entity(zorg_file)
        self._session.add(sql_zorg_file)
        return Ok(sql_zorg_file.path)

    def remove(
        self, zorg_file: File, /  # noqa: W504
    ) -> ErisResult[File | None]:
        """Remove a file from the DB."""
        sql_zorg_file = self._converter.from_entity(zorg_file)
        self._session.delete(sql_zorg_file)
        return Ok(zorg_file)

    # TODO(bugyi): Remove commits from this function!
    def remove_by_key(self, key: str) -> ErisResult[Optional[File]]:
        """Remove a zorg file from the repo by path."""
        path = key
        stmt = select(sql.ZorgFile).where(sql.ZorgFile.path == path)
        results = self._session.exec(stmt)
        sql_zorg_file = results.first()
        if sql_zorg_file:
            zorg_file = self._converter.to_entity(sql_model=sql_zorg_file)
            _LOGGER.debug("Deleting Zorg File", zorg_file=zorg_file)
            for sql_note in sql_zorg_file.notes:
                for prop_link in sql_note.property_links:
                    delete_prop = len(prop_link.prop.links) == 1
                    self._session.delete(prop_link)
                    if delete_prop:
                        self._session.delete(prop_link.prop)
                    self._session.commit()

                for note_tags in [
                    sql_note.areas,
                    sql_note.contexts,
                    sql_note.people,
                    sql_note.projects,
                ]:
                    for tag in note_tags:  # type: ignore[attr-defined]
                        if len(tag.notes) == 1:
                            self._session.delete(tag)
                            self._session.commit()

                self._session.delete(sql_note)
            self._session.delete(sql_zorg_file)
            return Ok(zorg_file)
        else:
            emsg = "Cannot delete zorg file since it does not exist."
            _LOGGER.debug(emsg, path=path)
            return Ok(None)

    def get(self, key: str) -> ErisResult[Optional[File]]:
        """Retrieve a file from the DB."""
        path = key
        stmt = select(sql.ZorgFile).where(sql.ZorgFile.path == path)
        results = self._session.exec(stmt)
        sql_zorg_file = results.first()
        if sql_zorg_file:
            zorg_file = self._converter.to_entity(sql_zorg_file)
            self._seen_zorg_file(zorg_file)
            return Ok(zorg_file)
        else:
            return Ok(None)

    def get_by_query(self, query: Optional[WhereOrFilter]) -> list[Note]:
        """Get file(s) from DB by using a query."""
        select_of_note = to_select_of_note(query, self._session)
        # If the user asked for really verbose output...
        if self._verbose > 1:
            # ... then we print the SELECT statement.
            print(select_of_note)

        result: list[Note] = []
        for sql_note in self._session.exec(select_of_note):
            result.append(self._note_converter.to_entity(sql_note))
        return result

    def all(self) -> ErisResult[list[File]]:
        """Returns all zorg notes contained in the underlying SQL database."""
        stmt = select(sql.ZorgFile)
        result: list[File] = []
        for sql_zorg_file in self._session.exec(stmt).all():
            zorg_file = self._converter.to_entity(sql_zorg_file)
            self._seen_zorg_file(zorg_file)
        return Ok(result)

    def _seen_zorg_file(self, zorg_file: File) -> None:
        # TODO(bugyi): Do I need to deduplicate self.seen?
        self.seen.append(zorg_file)


def _add_zids(zdir: Path, zorg_file: File) -> None:
    new_notes = []
    zid_manager = ZIDManager(zdir)
    for note in zorg_file.notes:
        if note.zid is None:
            _LOGGER.debug("Found new zorg note", zorg_note=note)
            zid = zid_manager.get_next(note.create_date)
            note.zid = zid
            new_notes.append(note)
    if new_notes:
        zorg_file.events.append(
            NewZorgNotesEvent(
                zdir, zorg_file_path=zorg_file.path, new_notes=new_notes
            )
        )
