"""Zorg's file unit-of-work implementation (FileSession) lives here."""

from potoroo import UnitOfWork

from .repo import FileRepo


class FileSession(UnitOfWork[FileRepo]):
    """Unit-of-work impl that enables atomic transactions for zorg files."""
