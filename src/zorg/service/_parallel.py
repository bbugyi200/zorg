"""Parallel processing utilities for zorg file operations."""

from __future__ import annotations

from concurrent.futures import ProcessPoolExecutor, as_completed
import hashlib
import multiprocessing as mp
from pathlib import Path
from typing import Callable, Optional

from logrus import Logger

from zorg.domain.models import Page
from zorg.service.compiler import walk_zorg_page

_LOGGER = Logger(__name__)


def process_zo_files_parallel(
    zdir: Path,
    zo_paths: list[Path],
    *,
    max_workers: Optional[int] = None,
    verbose: bool = False,
) -> list[Page]:
    """Process multiple *.zo files in parallel.

    Args:
    ----
        zdir: The zettel directory root.
        zo_paths: List of paths to *.zo files to process.
        max_workers: Maximum number of worker processes. Defaults to CPU count.
        verbose: Whether to enable verbose logging.

    Returns:
    -------
        List of parsed Page objects.

    """
    if max_workers is None:
        max_workers = mp.cpu_count()

    # For small numbers of files, parallel processing overhead isn't worth it
    if len(zo_paths) < 4 or max_workers == 1:
        _LOGGER.debug(
            "Processing files serially (too few files or single worker)",
            num_files=len(zo_paths),
            max_workers=max_workers,
        )
        return [
            walk_zorg_page(zdir, zo_path, verbose=verbose)
            for zo_path in zo_paths
        ]

    _LOGGER.debug(
        "Processing files in parallel",
        num_files=len(zo_paths),
        max_workers=max_workers,
    )

    pages = []
    with ProcessPoolExecutor(max_workers=max_workers) as executor:
        # Submit all tasks
        future_to_path = {
            executor.submit(
                _process_single_file, zdir, zo_path, verbose
            ): zo_path
            for zo_path in zo_paths
        }

        # Collect results as they complete
        for future in as_completed(future_to_path):
            zo_path = future_to_path[future]
            try:
                page = future.result()
                pages.append(page)
            except Exception as exc:
                _LOGGER.error(
                    "Failed to process zorg file",
                    zo_path=str(zo_path),
                    error=str(exc),
                )
                raise

    return pages


def hash_files_parallel(
    paths: list[Path],
    *,
    max_workers: Optional[int] = None,
    chunk_size: int = 8192,
) -> dict[str, str]:
    """Compute SHA256 hashes for multiple files in parallel.

    Args:
    ----
        paths: List of file paths to hash.
        max_workers: Maximum number of worker processes. Defaults to CPU count.
        chunk_size: Size of chunks to read when hashing files.

    Returns:
    -------
        Dictionary mapping file path strings to their hash values.

    """
    if max_workers is None:
        max_workers = mp.cpu_count()

    # For small numbers of files, parallel processing overhead isn't worth it
    if len(paths) < 4 or max_workers == 1:
        return {
            str(path): _hash_file(path, chunk_size=chunk_size)
            for path in paths
        }

    file_to_hash: dict[str, str] = {}
    with ProcessPoolExecutor(max_workers=max_workers) as executor:
        future_to_path = {
            executor.submit(_hash_file, path, chunk_size): path
            for path in paths
        }

        for future in as_completed(future_to_path):
            path = future_to_path[future]
            try:
                hash_value = future.result()
                file_to_hash[str(path)] = hash_value
            except Exception as exc:
                _LOGGER.error(
                    "Failed to hash file", path=str(path), error=str(exc)
                )
                raise

    return file_to_hash


def _process_single_file(
    zdir: Path, zo_path: Path, verbose: bool = False
) -> Page:
    """Process a single *.zo file (used by worker processes).

    Args:
    ----
        zdir: The zettel directory root.
        zo_path: Path to the *.zo file to process.
        verbose: Whether to enable verbose logging.

    Returns:
    -------
        Parsed Page object.

    """
    return walk_zorg_page(zdir, zo_path, verbose=verbose)


def _hash_file(filepath: Path, chunk_size: int = 8192) -> str:
    """Hash a file using SHA256 algorithm.

    Args:
    ----
        filepath: Path to the file to be hashed.
        chunk_size: Size of chunks to read the file. Default is 8192 bytes.

    Returns:
    -------
        A SHA256 hash of the file's contents.

    """
    hasher = hashlib.sha256()
    with filepath.open("rb") as file:
        while chunk := file.read(chunk_size):
            hasher.update(chunk)
    return hasher.hexdigest()
