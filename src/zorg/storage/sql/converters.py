"""Contains logic to convert domain models to/from SQL models."""

from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Callable, Optional

import metaman
from sqlmodel import Session, or_, select
from sqlmodel.sql.expression import ColumnElement, SelectOfScalar

from . import models as sql
from ...domain.models import WhereAndFilter, WhereOrFilter, ZorgFile, ZorgNote
from ...domain.types import EntityConverter, NoteStatus
from ...service import common


_SONConverterParser = Callable[["_SONConverter"], ColumnElement]
# the @_son_converter_parser decorator should be used to mark a _SONConverter
# parser method
_SON_CONVERTER_PARSERS: list[_SONConverterParser] = []
_son_converter_parser = metaman.register_function_factory(
    _SON_CONVERTER_PARSERS
)


def to_select_of_note(
    or_filter: Optional[WhereOrFilter],
) -> SelectOfScalar[sql.ZorgNote]:
    """Converts a WhereOrFilter to a SQL SELECT that will fetch ZorgNotes."""
    if or_filter is None or not or_filter.and_filters:
        return select(sql.ZorgNote)

    return select(sql.ZorgNote).where(
        or_(*[
            _SONConverter(and_filter).to_note_clause()
            for and_filter in or_filter.and_filters
        ])
    )


@dataclass(frozen=True)
class _SONConverter:
    """Converts a WhereAndFilter to a ColumnElement."""

    and_filter: WhereAndFilter

    def to_note_clause(self) -> ColumnElement:
        """Constructs a SQL statement from the provided WhereAndFilter."""
        where = or_(*[parse(self) for parse in _SON_CONVERTER_PARSERS])
        return where

    @_son_converter_parser
    def note_status(self) -> ColumnElement:
        """Converter for done status (e.g. '-' or 'ox~<>')."""
        return or_(*[
            sql.ZorgNote.todo_status == _to_todo_status(note_status)
            for note_status in self.and_filter.allowed_note_statuses
        ])


def _to_todo_status(note_status: NoteStatus) -> Optional[NoteStatus]:
    if note_status is NoteStatus.BASIC:
        return None
    else:
        return note_status


class ZorgFileConverter(EntityConverter[ZorgFile, sql.ZorgFile]):
    """Converts ZorgFile domain entities to/from ZorgFile sqlmodels."""

    def __init__(self, zdir: Path, session: Session) -> None:
        self._zdir = zdir
        self._note_converter = ZorgNoteConverter(session)
        self._all_sql_notes: list[sql.ZorgNote] = []

    def from_entity(self, entity: ZorgFile) -> sql.ZorgFile:
        """Model-to-SQL-model converter for a ZorgFile."""
        sql_notes = []
        for note in entity.notes:
            sql_note = self._note_converter.from_entity(note)
            self._all_sql_notes.append(sql_note)
            sql_notes.append(sql_note)
        return sql.ZorgFile(
            path=common.strip_zdir(self._zdir, entity.path),
            notes=sql_notes,
            has_errors=entity.has_errors,
        )

    def to_entity(self, sql_model: sql.ZorgFile) -> ZorgFile:
        """Model-to-SQL-model converter for a ZorgFile."""
        return ZorgFile(
            Path(common.strip_zdir(self._zdir, sql_model.path)),
            has_errors=sql_model.has_errors,
            notes=[
                self._note_converter.to_entity(sql_note)
                for sql_note in sql_model.notes
            ],
        )


class ZorgNoteConverter(EntityConverter[ZorgNote, sql.ZorgNote]):
    """Converts ZorgNote domain entities to/from ZorgNote sqlmodels."""

    def __init__(self, session: Session) -> None:
        self._session = session
        self._tag_cache: dict[Any, dict[str, Any]] = defaultdict(lambda: {})
        self._property_cache: dict[str, sql.Property] = {}

    def from_entity(self, entity: ZorgNote) -> sql.ZorgNote:
        """Model-to-SQL-model converter for a ZorgNote."""
        kwargs: dict[str, Any] = {
            "body": entity.body,
            "create_date": entity.create_date,
            "zid": entity.zid,
        }
        if entity.todo_payload:
            kwargs["todo_status"] = entity.todo_payload.status
            kwargs["todo_priority"] = entity.todo_payload.priority
        sql_zorg_note = sql.ZorgNote(**kwargs)

        stmt: Any
        for attr, tag_model in [
            ("areas", sql.Area),
            ("contexts", sql.Context),
            ("people", sql.Person),
            ("projects", sql.Project),
        ]:
            entity_tag_list = getattr(entity, attr)
            sql_tag_list = []
            tag_cache = self._tag_cache[tag_model]
            for tag_name in entity_tag_list:
                if tag_name not in tag_cache:
                    stmt = select(tag_model).where(tag_model.name == tag_name)
                    results = self._session.exec(stmt)
                    tag = results.first()
                    if tag is None:
                        tag = tag_model(name=tag_name)
                    tag_cache[tag_name] = tag

                tag = tag_cache[tag_name]
                sql_tag_list.append(tag)
            setattr(sql_zorg_note, attr, sql_tag_list)

        property_links = []
        for k, v in entity.properties.items():
            if k not in self._property_cache:
                stmt = select(sql.Property).where(sql.Property.name == k)
                results = self._session.exec(stmt)
                prop = results.first()
                if prop is None:
                    prop = sql.Property(name=k)
                self._property_cache[k] = prop

            prop = self._property_cache[k]
            stmt = (
                select(sql.PropertyLink)
                .where(sql.PropertyLink.note_id == sql_zorg_note.id)
                .where(sql.PropertyLink.prop_id == prop.id)
            )
            results = self._session.exec(stmt)
            prop_link = results.first()

            if prop_link is None:
                prop_link = sql.PropertyLink(
                    prop=prop, todo=sql_zorg_note, value=v
                )

            property_links.append(prop_link)

        sql_zorg_note.property_links = property_links
        return sql_zorg_note

    def to_entity(self, sql_model: sql.ZorgNote) -> ZorgNote:
        """Model-to-SQL-model converter for a ZorgNote."""
        return ZorgNote(
            sql_model.body,
            areas=list(area.name for area in sql_model.areas),
            contexts=list(context.name for context in sql_model.contexts),
            people=list(person.name for person in sql_model.people),
            projects=list(project.name for project in sql_model.projects),
        )
