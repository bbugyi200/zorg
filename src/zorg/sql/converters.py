"""Contains logic to convert domain models to/from SQL models."""

from pathlib import Path

from . import models as sql
from ..models import ZorgFile, ZorgNote


def file_to_sql_model(model: ZorgFile) -> sql.ZorgFile:
    """Model-to-SQL-model converter for a ZorgFile."""
    del model
    return sql.ZorgFile()


def sql_file_to_model(sql_model: sql.ZorgFile) -> ZorgFile:
    """Model-to-SQL-model converter for a ZorgFile."""
    del sql_model
    return ZorgFile(Path("."))


def note_to_sql_model(model: ZorgNote) -> sql.ZorgNote:
    """Model-to-SQL-model converter for a ZorgFile."""
    del model
    return sql.ZorgNote(desc="")


def sql_note_to_model(sql_model: sql.ZorgNote) -> ZorgNote:
    """Model-to-SQL-model converter for a ZorgFile."""
    del sql_model
    return ZorgNote("")
