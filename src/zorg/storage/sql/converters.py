"""Contains logic to convert domain models to/from SQL models."""

from pathlib import Path

from . import models as sql
from ...domain.models import ZorgFile, ZorgNote
from ...domain.types import EntityConverter


class ZorgFileConverter(EntityConverter[ZorgFile, sql.ZorgFile]):
    """Converts ZorgFile domain entities to/from ZorgFile sqlmodels."""

    def from_entity(self, entity: ZorgFile) -> sql.ZorgFile:
        """Model-to-SQL-model converter for a ZorgFile."""
        return sql.ZorgFile(
            path=str(entity.path),
            notes=[
                ZorgNoteConverter().from_entity(note) for note in entity.notes
            ],
        )

    def to_entity(self, sql_model: sql.ZorgFile) -> ZorgFile:
        """Model-to-SQL-model converter for a ZorgFile."""
        del sql_model
        return ZorgFile(Path("."))


class ZorgNoteConverter(EntityConverter[ZorgNote, sql.ZorgNote]):
    """Converts ZorgNote domain entities to/from ZorgNote sqlmodels."""

    def from_entity(self, entity: ZorgNote) -> sql.ZorgNote:
        """Model-to-SQL-model converter for a ZorgNote."""
        return sql.ZorgNote(body=entity.body)

    def to_entity(self, sql_model: sql.ZorgNote) -> ZorgNote:
        """Model-to-SQL-model converter for a ZorgNote."""
        del sql_model
        return ZorgNote("")
