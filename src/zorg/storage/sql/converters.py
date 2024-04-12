"""Contains logic to convert domain models to/from SQL models."""

from collections import defaultdict
from pathlib import Path
from typing import Any

from sqlmodel import Session, select

from . import models as sql
from ...domain.models import ZorgFile, ZorgNote
from ...domain.types import EntityConverter


class ZorgFileConverter(EntityConverter[ZorgFile, sql.ZorgFile]):
    """Converts ZorgFile domain entities to/from ZorgFile sqlmodels."""

    def __init__(self, session: Session) -> None:
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
            path=str(entity.path),
            notes=sql_notes,
            has_errors=entity.has_errors,
        )

    def to_entity(self, sql_model: sql.ZorgFile) -> ZorgFile:
        """Model-to-SQL-model converter for a ZorgFile."""
        return ZorgFile(
            Path(sql_model.path),
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
