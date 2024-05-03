"""Contains the Repo class."""

# pylint: disable=unsubscriptable-object

from __future__ import annotations

from pathlib import Path
from typing import Optional

from eris import ErisResult, Err, Ok
from logrus import Logger
from sqlmodel import Session, select

from . import models as sql
from ...domain.messages.events import NewZorgNotesEvent
from ...domain.models import WhereOrFilter, ZorgFile, ZorgNote
from ...service.zid_manager import ZIDManager
from .converters import ZorgFileConverter, ZorgNoteConverter, to_select_of_note


logger = Logger(__name__)


class SQLRepo:
    """Repo that stores zorg notes in sqlite database."""

    def __init__(
        self,
        zettel_dir: Path,
        session: Session,
    ) -> None:
        self._zettel_dir = zettel_dir
        self._session = session
        self._converter = ZorgFileConverter(zettel_dir, session)
        self._note_converter = ZorgNoteConverter(session)

        self.seen: list[ZorgFile] = []

    def add(
        self, zorg_file: ZorgFile, /, *, key: str = None
    ) -> ErisResult[str]:
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
        self, zorg_file: ZorgFile, /  # noqa: W504
    ) -> ErisResult[ZorgFile | None]:
        """Remove a file from the DB."""
        sql_zorg_file = self._converter.from_entity(zorg_file)
        self._session.delete(sql_zorg_file)
        return Ok(zorg_file)

    # TODO(bugyi): Remove commits from this function!
    def remove_by_key(self, key: str) -> ErisResult[Optional[ZorgFile]]:
        """Remove a zorg file from the repo by path."""
        path = key
        stmt = select(sql.ZorgFile).where(sql.ZorgFile.path == path)
        results = self._session.exec(stmt)
        sql_zorg_file = results.first()
        if sql_zorg_file:
            zorg_file = self._converter.to_entity(sql_model=sql_zorg_file)
            logger.info(
                "Deleting Zorg File",
                sql_zorg_file=sql_zorg_file,
                zorg_file=zorg_file,
            )
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
            emsg = "Failed to delete Zorg File"
            logger.warning(emsg, path=path)
            return Err(emsg)

    def get(self, key: str) -> ErisResult[Optional[ZorgFile]]:
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

    def get_by_query(
        self, query: Optional[WhereOrFilter]
    ) -> ErisResult[list[ZorgNote]]:
        """Get file(s) from DB by using a query."""
        select_of_note = to_select_of_note(query)
        result: list[ZorgNote] = []
        for sql_note in self._session.exec(select_of_note):
            result.append(self._note_converter.to_entity(sql_note))
        return Ok(result)

    def all(self) -> ErisResult[list[ZorgFile]]:
        """Returns all zorg notes contained in the underlying SQL database."""
        stmt = select(sql.ZorgFile)
        result: list[ZorgFile] = []
        for sql_zorg_file in self._session.exec(stmt).all():
            zorg_file = self._converter.to_entity(sql_zorg_file)
            self._seen_zorg_file(zorg_file)
        return Ok(result)

    def _seen_zorg_file(self, zorg_file: ZorgFile) -> None:
        # TODO(bugyi): Do I need to deduplicate self.seen?
        self.seen.append(zorg_file)


def _add_zids(zdir: Path, zorg_file: ZorgFile) -> None:
    new_notes = []
    zid_manager = ZIDManager(zdir)
    for note in zorg_file.notes:
        if note.zid is None:
            logger.debug("Found new zorg note", zorg_note=note)
            zid = zid_manager.get_next(note.create_date)
            note.zid = zid
            new_notes.append(note)
    if new_notes:
        zorg_file.events.append(
            NewZorgNotesEvent(
                zorg_file_path=zorg_file.path, new_notes=new_notes
            )
        )
