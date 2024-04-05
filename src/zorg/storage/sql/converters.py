"""Contains logic to convert domain models to/from SQL models."""

from pathlib import Path

from . import models as sql
from ...domain.models import ZorgFile, ZorgNote
from ...domain.types import DomainConverter


class ZorgFileConverter(DomainConverter[ZorgFile, sql.ZorgFile]):
    """Converts ZorgFile domain entities to/from ZorgFile sqlmodels."""

    def from_domain(self, entity: ZorgFile) -> sql.ZorgFile:
        """Model-to-SQL-model converter for a ZorgFile."""
        del entity
        return sql.ZorgFile()

    def to_domain(self, sql_model: sql.ZorgFile) -> ZorgFile:
        """Model-to-SQL-model converter for a ZorgFile."""
        del sql_model
        return ZorgFile(Path("."))


class ZorgNoteConverter(DomainConverter[ZorgNote, sql.ZorgNote]):
    """Converts ZorgNote domain entities to/from ZorgNote sqlmodels."""

    def from_domain(self, entity: ZorgNote) -> sql.ZorgNote:
        """Model-to-SQL-model converter for a ZorgNote."""
        del entity
        return sql.ZorgNote(desc="")

    def to_domain(self, sql_model: sql.ZorgNote) -> ZorgNote:
        """Model-to-SQL-model converter for a ZorgNote."""
        del sql_model
        return ZorgNote("")
