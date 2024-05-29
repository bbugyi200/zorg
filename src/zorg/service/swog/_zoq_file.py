"""Contains utilities for working with *.zoq files."""

import datetime as dt
from functools import partial
import itertools as it
from pathlib import Path

from ...storage.sql.session import SQLSession
from ._executor import execute


def refresh_zoq_file(session: SQLSession, zoq_path: Path) -> None:
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
    query_string = zoq_lines[0].strip()[2:]
    query_results = execute(session, query_string)
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
