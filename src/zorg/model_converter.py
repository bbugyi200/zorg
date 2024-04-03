"""Contains logic to convert domain models to/from SQL models."""

from pathlib import Path

from . import models, sql_models


def file_to_sql_model(model: models.ZorgFile) -> sql_models.ZorgFile:
    """Model-to-SQL-model converter for a ZorgFile."""
    del model
    return sql_models.ZorgFile()


def sql_file_to_model(sql_model: sql_models.ZorgFile) -> models.ZorgFile:
    """Model-to-SQL-model converter for a ZorgFile."""
    del sql_model
    return models.ZorgFile(Path("."))


def note_to_sql_model(model: models.ZorgNote) -> sql_models.ZorgNote:
    """Model-to-SQL-model converter for a ZorgFile."""
    del model
    return sql_models.ZorgNote(desc="")


def sql_note_to_model(sql_model: sql_models.ZorgNote) -> models.ZorgNote:
    """Model-to-SQL-model converter for a ZorgFile."""
    del sql_model
    return models.ZorgNote("")
