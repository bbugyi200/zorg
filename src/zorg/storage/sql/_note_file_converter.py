"""Convert domain Pages/Notes to/from SQL ZorgFile/ZorgNote models."""

from collections import defaultdict
from pathlib import Path
from typing import Any, cast

from sqlmodel import Session, select

from zorg.domain.models import (
    Note,
    Page,
    TodoPayload,
)
from zorg.domain.types import (
    EntityConverter,
    TodoPriorityType,
)
from zorg.shared import common

from . import _models as sql


class ZorgFileConverter(EntityConverter[Page, sql.ZorgFile]):
    """Converts Page domain entities to/from ZorgFile sqlmodels."""

    def __init__(self, zdir: Path, session: Session) -> None:
        self._zdir = zdir
        self._note_converter = ZorgNoteConverter(zdir, session)
        self._all_sql_notes: list[sql.ZorgNote] = []

    def from_entity(self, entity: Page) -> sql.ZorgFile:
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

    def to_entity(self, sql_model: sql.ZorgFile) -> Page:
        """Model-to-SQL-model converter for a Page."""
        return Page(
            Path(common.strip_zdir(self._zdir, sql_model.path)),
            has_errors=sql_model.has_errors,
            notes=[
                self._note_converter.to_entity(sql_note)
                for sql_note in sql_model.notes
            ],
        )


class ZorgNoteConverter(EntityConverter[Note, sql.ZorgNote]):
    """Converts Note domain entities to/from ZorgNote sqlmodels."""

    def __init__(self, zdir: Path, session: Session) -> None:
        self._zdir = zdir
        self._session = session

        self._tag_cache: dict[Any, dict[str, Any]] = defaultdict(lambda: {})
        self._property_cache: dict[str, sql.Property] = {}

    def from_entity(self, entity: Note) -> sql.ZorgNote:
        """Model-to-SQL-model converter for a ZorgNote."""
        # HACK: Needed to prevent errors of the form:
        #   SAWarning: Object of type <ZorgNote> not in session...
        with self._session.no_autoflush as session:
            return self._from_entity_with_session(
                entity, cast(Session, session)
            )

    def _from_entity_with_session(
        self, entity: Note, session: Session
    ) -> sql.ZorgNote:
        kwargs: dict[str, Any] = {
            "body": entity.body,
            "create_date": entity.create_date,
            "modify_date": entity.modify_date,
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
            ("links", sql.Link),
        ]:
            entity_tag_list = getattr(entity, attr)
            sql_tag_list = []
            tag_cache = self._tag_cache[tag_model]
            for tag_name in entity_tag_list:
                if tag_name not in tag_cache:
                    stmt = select(tag_model).where(tag_model.name == tag_name)
                    results = session.exec(stmt)
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
                results = session.exec(stmt)
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
            results = session.exec(stmt)
            prop_link = results.first()

            if prop_link is None:
                prop_link = sql.PropertyLink(
                    prop=prop, todo=sql_zorg_note, value=v
                )

            property_links.append(prop_link)

        sql_zorg_note.property_links = property_links

        # Convert 'zorg_file' field.
        if entity.file_path is not None:
            stripped_file_path = common.strip_zdir(
                self._zdir, entity.file_path
            )
            stmt = select(sql.ZorgFile).where(
                sql.ZorgFile.path == stripped_file_path
            )
            results = session.exec(stmt)
            sql_zorg_note.zorg_file = results.first()

        sql_zorg_note.line_no = entity.line_no
        return sql_zorg_note

    def to_entity(self, sql_model: sql.ZorgNote) -> Note:
        """Model-to-SQL-model converter for a Note."""
        todo_payload = (
            TodoPayload(
                status=sql_model.todo_status,
                priority=cast(TodoPriorityType, sql_model.todo_priority),
            )
            if sql_model.todo_priority is not None
            and sql_model.todo_status is not None
            else None
        )
        properties: dict[str, str] = {}
        for prop_link in sql_model.property_links:
            properties[prop_link.prop.name] = prop_link.value

        return Note(
            sql_model.body,
            areas=list(area.name for area in sql_model.areas),
            contexts=list(context.name for context in sql_model.contexts),
            create_date=sql_model.create_date,
            file_path=Path(sql_model.zorg_file.path),
            line_no=sql_model.line_no,
            links=[link.name for link in sql_model.links],
            modify_date=sql_model.modify_date,
            people=list(person.name for person in sql_model.people),
            projects=list(project.name for project in sql_model.projects),
            properties=properties,
            todo_payload=todo_payload,
            zid=sql_model.zid,
        )
