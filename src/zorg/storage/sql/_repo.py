"""Contains the Repo class."""

# pylint: disable=unsubscriptable-object

from __future__ import annotations

from pathlib import Path
from typing import Optional, cast

from logrus import Logger
from sqlmodel import Session, and_, select
from sqlmodel.sql.expression import ColumnElement

from zorg.domain.messages.events import NewZorgNotesEvent
from zorg.domain.models import Note, Page, WhereOrFilter
from zorg.shared import common as c, dates as zdt

from . import _models as sql
from ._page_converters import NoteConverter, PageConverter
from ._query_converter import to_sql_select
from ._zid_manager import ZIDManager


_LOGGER = Logger(__name__)


class SQLRepo:
    """Repo that stores zorg notes in sqlite database."""

    def __init__(
        self, zdir: Path, session: Session, *, verbose: int = 0
    ) -> None:
        self._zdir = zdir
        self._session = session
        self._verbose = verbose

        self._page_converter = PageConverter(zdir, session)
        self._note_converter = NoteConverter(zdir, session)
        self._path_to_seen_page: dict[str, Page] = {}

        self.seen_pages: list[Page] = []

    def add_file(self, page: Page, /, *, key: str = None) -> None:
        """Adds a new file to the DB."""
        del key
        self._record_seen_page(page)
        _add_zids(self._zdir, page)
        sql_zorg_page = self._page_converter.from_entity(page)
        self._session.add(sql_zorg_page)

    def remove_file_by_name(self, filename: str) -> Optional[Page]:
        """Remove a zorg file from the repo by path."""
        stmt = select(sql.Page).where(sql.Page.path == filename)
        results = self._session.exec(stmt)
        sql_zorg_page = results.first()
        if sql_zorg_page:
            page = self._page_converter.to_entity(sql_zorg_page)
            _LOGGER.debug("Deleting Zorg Page", page=page)
            for sql_note in sql_zorg_page.notes:
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
            self._session.delete(sql_zorg_page)
            return page
        else:
            emsg = "Cannot delete zorg file since it does not exist."
            _LOGGER.debug(emsg, path=filename)
            return None

    def get_notes_by_query(self, query: Optional[WhereOrFilter]) -> list[Note]:
        """Get note(s) from DB by using a query."""
        select_of_note = to_sql_select(query, self._session)
        # If the user asked for really verbose output...
        if self._verbose > 1:
            # ... then we print the SELECT statement.
            print(select_of_note)

        notes: list[Note] = []
        for sql_note in self._session.exec(select_of_note):
            page = self._get_page(sql_note)
            note = c.get_only_item(
                [note for note in page.notes if note.zid == sql_note.zid]
            )
            notes.append(note)
        return notes

    def get_note_by_zid(self, zid: str) -> Optional[Note]:
        """Fetch a single note using its unique ZID."""
        stmt = select(sql.Note).where(sql.Note.zid == zid)
        results = self._session.exec(stmt)
        sql_note = results.first()
        if sql_note:
            return self._note_converter.to_entity(sql_note)
        else:
            _LOGGER.warning(
                "Unable to find a note with the given ZID", zid=zid
            )
            return None

    def get_notes_by_id(self, id_: str, *, id_key: str = "ID") -> list[Note]:
        """Fetch a list of notes using an id:: property."""
        stmt = (
            select(sql.Note)
            .join(
                sql.PropertyLink,
                cast(
                    ColumnElement, sql.Note.id == sql.PropertyLink.note_id
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
                and_(
                    sql.Property.name == id_key, sql.PropertyLink.value == id_
                )
            )
        )
        results = self._session.exec(stmt)
        return [
            self._note_converter.to_entity(sql_note)
            for sql_note in results.all()
        ]

    def _record_seen_page(self, page: Page) -> None:
        if page not in self.seen_pages:
            self.seen_pages.append(page)
        if str(page.path) not in self._path_to_seen_page:
            self._path_to_seen_page[str(page.path)] = page

    def _get_page(self, sql_note: sql.Note) -> Page:
        page_path = sql_note.page_path
        if page_path not in self._path_to_seen_page:
            self._record_seen_page(_get_page(sql_note, self._page_converter))
        return self._path_to_seen_page[page_path]


def _add_zids(zdir: Path, page: Page) -> None:
    new_notes = []
    zid_manager = ZIDManager(zdir)
    for note in page.notes:
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
        page.events.append(
            NewZorgNotesEvent(
                zdir, zorg_page_path=page.path, new_notes=new_notes
            )
        )


def _get_page(sql_note: sql.Note, page_converter: PageConverter) -> Page:
    sql_block = sql_note.block
    if sql_h1 := sql_block.h1:
        sql_page = sql_h1.page
    elif sql_h2 := sql_block.h2:
        sql_page = sql_h2.h1.page
    elif sql_h3 := sql_block.h3:
        sql_page = sql_h3.h2.h1.page
    elif sql_h4 := sql_block.h4:
        sql_page = sql_h4.h3.h2.h1.page
    else:
        raise RuntimeError(
            f"A block MUST be associated with an H1-H4 section | {sql_block}"
        )
    return page_converter.to_entity(sql_page)
