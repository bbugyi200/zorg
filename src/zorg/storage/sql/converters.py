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

    def from_entity(self, entity: ZorgFile) -> sql.ZorgFile:
        """Model-to-SQL-model converter for a ZorgFile."""
        return sql.ZorgFile(
            path=str(entity.path),
            notes=[
                self._note_converter.from_entity(note) for note in entity.notes
            ],
        )

    def to_entity(self, sql_model: sql.ZorgFile) -> ZorgFile:
        """Model-to-SQL-model converter for a ZorgFile."""
        del sql_model
        return ZorgFile(Path("."))


class ZorgNoteConverter(EntityConverter[ZorgNote, sql.ZorgNote]):
    """Converts ZorgNote domain entities to/from ZorgNote sqlmodels."""

    def __init__(self, session: Session) -> None:
        self._session = session
        self._tag_cache: dict[Any, dict[str, Any]] = defaultdict(lambda: {})

    def from_entity(self, entity: ZorgNote) -> sql.ZorgNote:
        """Model-to-SQL-model converter for a ZorgNote."""
        kwargs: dict[str, Any] = {
            "body": entity.body,
        }
        if entity.todo_payload:
            kwargs["todo_status"] = entity.todo_payload.status
            kwargs["todo_priority"] = entity.todo_payload.priority
        sql_zorg_note = sql.ZorgNote(**kwargs)
        for attr, tag_model in [
            ("areas", sql.Area),
            ("contexts", sql.Context),
            ("people", sql.Person),
            ("projects", sql.Project),
        ]:
            self_tag_list = getattr(entity, attr)
            model_tag_list = []
            for tag_name in self_tag_list:
                if tag_name not in self._tag_cache[tag_model]:
                    stmt = select(tag_model).where(tag_model.name == tag_name)
                    results = self._session.exec(stmt)
                    tag = results.first()
                    if tag is None:
                        tag = tag_model(name=tag_name)
                    self._tag_cache[tag_model][tag_name] = tag

                tag = self._tag_cache[tag_model][tag_name]
                model_tag_list.append(tag)
            setattr(sql_zorg_note, attr, model_tag_list)
        return sql_zorg_note

    def to_entity(self, sql_model: sql.ZorgNote) -> ZorgNote:
        """Model-to-SQL-model converter for a ZorgNote."""
        del sql_model
        return ZorgNote("")
