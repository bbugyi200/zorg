"""Contains the init_zoq_file() function."""

import datetime as dt
from functools import partial
import itertools as it
from pathlib import Path

from ...storage.sql.session import SQLSession
from ._executor import execute


def init_zoq_file(
    session: SQLSession, query_string: str, zoq_path: Path
) -> None:
    """Initialize the provided *.zoq file.

    Arguments:
    ----------
    session: A zorg SQL session that MUST be instantiated (e.g. using `with
        session`) by the caller.
    query_string: A SWOG query string. We will execute this query and use the
        results to populate the provided *.zoq file.
    zoq_path: The path of the *.zoq file we are going to initialize.
    """
    query_results = execute(session, query_string)
    date_spec = dt.datetime.now().strftime("%Y-%m-%d at %H:%M:%S")
    stats_line_start = "# Saved query generated on"
    zoq_lines = zoq_path.read_text().split("\n")
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
