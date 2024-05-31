"""Contains the Repo class."""

# pylint: disable=unsubscriptable-object

from __future__ import annotations

from pathlib import Path
from typing import Optional, cast

from logrus import Logger
from sqlmodel import Session, and_, select
from sqlmodel.sql.expression import ColumnElement

from . import models as sql
from ...domain.messages.events import NewZorgNotesEvent
from ...domain.models import File, Note, WhereOrFilter
from ...service import dates as zdt
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
        self._note_converter = ZorgNoteConverter(zettel_dir, session)
        self._verbose = verbose

        self.seen: list[File] = []

    def add_file(self, zorg_file: File, /, *, key: str = None) -> None:
        """Adds a new file to the DB."""
        del key
        self._seen_zorg_file(zorg_file)
        _add_zids(self._zettel_dir, zorg_file)
        sql_zorg_file = self._converter.from_entity(zorg_file)
        self._session.add(sql_zorg_file)

    def remove_file_by_name(self, filename: str) -> Optional[File]:
        """Remove a zorg file from the repo by path."""
        stmt = select(sql.ZorgFile).where(sql.ZorgFile.path == filename)
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
            return zorg_file
        else:
            emsg = "Cannot delete zorg file since it does not exist."
            _LOGGER.debug(emsg, path=filename)
            return None

    def get_notes_by_query(self, query: Optional[WhereOrFilter]) -> list[Note]:
        """Get note(s) from DB by using a query."""
        select_of_note = to_select_of_note(query, self._session)
        # If the user asked for really verbose output...
        if self._verbose > 1:
            # ... then we print the SELECT statement.
            print(select_of_note)

        result: list[Note] = []
        for sql_note in self._session.exec(select_of_note):
            result.append(self._note_converter.to_entity(sql_note))
        return result

    def get_note_by_zid(self, zid: str) -> Optional[Note]:
        """Fetch a single note using its unique ZID."""
        stmt = select(sql.ZorgNote).where(sql.ZorgNote.zid == zid)
        results = self._session.exec(stmt)
        sql_note = results.first()
        if sql_note:
            return self._note_converter.to_entity(sql_note)
        else:
            _LOGGER.warning(
                "Unable to find a note with the given ZID", zid=zid
            )
            return None

    def get_notes_by_id(self, id_: str) -> list[Note]:
        """Fetch a list of notes using an id:: property."""
        stmt = (
            select(sql.ZorgNote)
            .join(
                sql.PropertyLink,
                cast(
                    ColumnElement, sql.ZorgNote.id == sql.PropertyLink.note_id
                ),
            )
            .join(
                sql.Property,
                cast(
                    ColumnElement,
                    sql.PropertyLink.prop_id == sql.Property.id,
                ),
            )
            .where(
                and_(sql.Property.name == "id", sql.PropertyLink.value == id_)
            )
        )
        results = self._session.exec(stmt)
        return [
            self._note_converter.to_entity(sql_note)
            for sql_note in results.all()
        ]

    def _seen_zorg_file(self, zorg_file: File) -> None:
        self.seen.append(zorg_file)


def _add_zids(zdir: Path, zorg_file: File) -> None:
    new_notes = []
    zid_manager = ZIDManager(zdir)
    for note in zorg_file.notes:
        if note.zid is None:
            _LOGGER.debug("Found new zorg note", zorg_note=note)
            zid = zid_manager.get_next(note.create_date)
            note.zid = zid
            old_body = note.body.lstrip()
            if zdt.is_long_date_spec(old_body.split(" ")[0]):
                old_body = " ".join(old_body.split(" ")[1:])
            note.body = f"{zid} {old_body}"
            new_notes.append(note)
    if new_notes:
        zorg_file.events.append(
            NewZorgNotesEvent(
                zdir, zorg_file_path=zorg_file.path, new_notes=new_notes
            )
        )
