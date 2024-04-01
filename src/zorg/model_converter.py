"""Contains logic to convert domain models to/from SQL models."""

from . import models, sql_models


def file_to_sql_model(model: models.ZorgFile) -> sql_models.ZorgFile:
    """Model-to-SQL-model converter for a ZorgFile."""


def sql_file_to_model(sql_model: sql_models.ZorgFile) -> models.ZorgFile:
    """Model-to-SQL-model converter for a ZorgFile."""


def todo_to_sql_model(model: models.ZorgTodo) -> sql_models.ZorgNote:
    """Model-to-SQL-model converter for a ZorgFile."""


def sql_note_to_todo_model(sql_model: sql_models.ZorgNote) -> models.ZorgTodo:
    """Model-to-SQL-model converter for a ZorgFile."""


def note_to_sql_model(model: models.ZorgNote) -> sql_models.ZorgNote:
    """Model-to-SQL-model converter for a ZorgFile."""


def sql_note_to_note_model(sql_model: sql_models.ZorgNote) -> models.ZorgNote:
    """Model-to-SQL-model converter for a ZorgFile."""
