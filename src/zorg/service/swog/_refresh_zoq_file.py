"""Contains utilities for refreshing *.zoq files."""

import datetime as dt
from functools import partial
import itertools as it
from pathlib import Path

from typist import PathLike

from zorg.storage.sql import SQLSession

from ._executor import execute_with_session


def refresh_zoq_file(
    zdir: PathLike, db_url: str, zoq_path: Path, *, verbose: int = 0
) -> None:
    """Refresh the query execution results contained in {zoq_path}."""
    zdir = Path(zdir)
    with SQLSession(zdir, db_url, verbose=verbose) as session:
        refresh_zoq_file_with_session(session, zoq_path)


def refresh_zoq_file_with_session(session: SQLSession, zoq_path: Path) -> None:
    """Refresh the query execution results contained in a provided *.zoq file.

    Arguments:
    ----------
    session: A zorg SQL session that MUST be instantiated (e.g. using `with
        session`) by the caller.
    zoq_path: The path of an existing *.zoq file we are going to refresh.
    """
    assert (
        zoq_path.exists()
    ), "PRECONDITION: Provided *.zoq path (i.e. zoq_path argument) MUST exist."
    zoq_lines = zoq_path.read_text().split("\n")
    qstring = zoq_lines[0].strip()[2:]
    query_results = execute_with_session(session, qstring)
    date_spec = dt.datetime.now().strftime("%Y-%m-%d AT %H:%M:%S")
    stats_line_start = "# SAVED QUERY GENERATED ON"
    old_header_lines = it.takewhile(
        partial(_is_zoq_header_line, stats_line_start), zoq_lines
    )
    old_header = "\n".join(old_header_lines)
    stats_line = f"{stats_line_start} {date_spec}."
    maybe_hash_line = "" if old_header.endswith("#") else "#\n"
    zoq_contents = (
        f"{old_header}\n{maybe_hash_line}{stats_line}\n\n{query_results}"
    )
    with zoq_path.open("w") as f:
        f.write(zoq_contents)


def _is_zoq_header_line(end_marker: str, line: str) -> bool:
    return line.startswith("#") and not line.startswith(end_marker)
