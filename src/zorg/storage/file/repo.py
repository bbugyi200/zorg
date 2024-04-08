"""Zorg's file repository (FileRepo) lives here."""

from potoroo import Repo

from ...domain.models import ZorgNote


class FileRepo(Repo[str, ZorgNote]):
    """Repository for zorg (*.zo) files."""
