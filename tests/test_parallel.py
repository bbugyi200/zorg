"""Tests for the parallel processing module."""

from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING

from pytest import fixture

from zorg.service._parallel import (
    hash_files_parallel,
    process_zo_files_parallel,
)

if TYPE_CHECKING:
    from . import common as test_c


@fixture
def sample_zo_files(local_zettel_dir: Path) -> list[Path]:
    """Returns a list of sample *.zo files for testing."""
    return sorted(local_zettel_dir.rglob("*.zo"))


def test_process_zo_files_parallel__basic(
    local_zettel_dir: Path, sample_zo_files: list[Path]
) -> None:
    """Test that parallel processing produces valid Page objects."""
    pages = process_zo_files_parallel(
        local_zettel_dir, sample_zo_files, max_workers=2
    )

    assert len(pages) == len(sample_zo_files)
    assert all(page.path.exists() for page in pages)
    assert all(isinstance(page.notes, list) for page in pages)


def test_process_zo_files_parallel__single_worker(
    local_zettel_dir: Path, sample_zo_files: list[Path]
) -> None:
    """Test that single worker mode works (falls back to serial)."""
    pages = process_zo_files_parallel(
        local_zettel_dir, sample_zo_files, max_workers=1
    )

    assert len(pages) == len(sample_zo_files)
    assert all(page.path.exists() for page in pages)


def test_process_zo_files_parallel__empty_list(
    local_zettel_dir: Path,
) -> None:
    """Test that processing an empty list returns an empty list."""
    pages = process_zo_files_parallel(local_zettel_dir, [])
    assert pages == []


def test_hash_files_parallel__basic(sample_zo_files: list[Path]) -> None:
    """Test that parallel hashing produces valid hashes."""
    file_to_hash = hash_files_parallel(sample_zo_files, max_workers=2)

    assert len(file_to_hash) == len(sample_zo_files)
    # Check that all hashes are valid SHA256 hashes (64 hex characters)
    for path in sample_zo_files:
        hash_value = file_to_hash[str(path)]
        assert len(hash_value) == 64
        assert all(c in "0123456789abcdef" for c in hash_value)


def test_hash_files_parallel__single_worker(
    sample_zo_files: list[Path],
) -> None:
    """Test that single worker mode works (falls back to serial)."""
    file_to_hash = hash_files_parallel(sample_zo_files, max_workers=1)

    assert len(file_to_hash) == len(sample_zo_files)
    for path in sample_zo_files:
        assert str(path) in file_to_hash


def test_hash_files_parallel__empty_list() -> None:
    """Test that hashing an empty list returns an empty dict."""
    file_to_hash = hash_files_parallel([])
    assert file_to_hash == {}


def test_hash_files_parallel__consistency(
    sample_zo_files: list[Path],
) -> None:
    """Test that parallel and serial hashing produce the same results."""
    if not sample_zo_files:
        return  # Skip if no files available

    # Hash with multiple workers
    parallel_hashes = hash_files_parallel(sample_zo_files, max_workers=2)

    # Hash with single worker (serial)
    serial_hashes = hash_files_parallel(sample_zo_files, max_workers=1)

    # Results should be identical
    assert parallel_hashes == serial_hashes


def test_process_zo_files_parallel__consistency(
    local_zettel_dir: Path, sample_zo_files: list[Path]
) -> None:
    """Test that parallel and serial processing produce consistent results."""
    if not sample_zo_files:
        return  # Skip if no files available

    # Process with multiple workers
    parallel_pages = process_zo_files_parallel(
        local_zettel_dir, sample_zo_files, max_workers=2
    )

    # Process with single worker (serial)
    serial_pages = process_zo_files_parallel(
        local_zettel_dir, sample_zo_files, max_workers=1
    )

    # Results should have same number of pages
    assert len(parallel_pages) == len(serial_pages)

    # Sort both lists by path for comparison
    parallel_pages.sort(key=lambda p: str(p.path))
    serial_pages.sort(key=lambda p: str(p.path))

    # Check that each page has the same basic properties
    for p_page, s_page in zip(parallel_pages, serial_pages):
        assert p_page.path == s_page.path
        assert len(p_page.notes) == len(s_page.notes)
        assert p_page.has_errors == s_page.has_errors
