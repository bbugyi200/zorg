"""Contains utilities for working with saved queries."""

from pathlib import Path
import re
from typing import Final, Optional

from logrus import Logger
from typist import PathLike

from zorg.shared import common as c


_LOGGER: Final = Logger(__name__)


def expand_saved_queries(zdir: PathLike, qstring: str) -> Optional[str]:
    """Recursively expands all saved queries in {query}."""
    zdir = Path(zdir)
    new_qstring = qstring
    for qname in _get_saved_query_names(qstring):
        sub_where_filter = _get_saved_where_filter(zdir, qname)
        if sub_where_filter is None:
            _LOGGER.error(
                "Failed to get saved WHERE filter from query name",
                query_name=qname,
            )
            return None
        new_qstring = new_qstring.replace(f"{{{qname}}}", sub_where_filter)
    _LOGGER.debug(
        "All saved query references have been expanded",
        original_query=qstring,
        expanded_query=new_qstring,
    )
    return new_qstring


def _get_saved_query_names(qstring: str) -> set[str]:
    """
    Extracts all saved query names from the given query string.

    Arguments:
    ----------
    qstring: The input string containing saved queries.

    Return:
    -------
    A set of saved query names.
    """
    # Regex to match the pattern of saved queries in the form {FOOBAR}
    pattern = r"\{(.*?)\}"
    # Find all matches in the query string
    matches = re.findall(pattern, qstring)
    return set(matches)


def _get_saved_where_filter(zdir: PathLike, query_name: str) -> Optional[str]:
    """Attempt to fetch a saved where filter string.

    Returns a where filter string taken from the {zdir}/query/{query_name}.zoq
    file, if it exists. Otherwise, returns None.
    """
    zdir = Path(zdir)
    zoq_path = c.prepend_zdir(zdir, f"query/{query_name}.zoq")
    if not zoq_path.exists():
        _LOGGER.error("Zorg query file does NOT exist", zoq_path=str(zoq_path))
        return None

    qstring = zoq_path.read_text().split("\n")[0][2:]
    in_where_filter = False
    where_words = []
    for word in qstring.split(" "):
        if word == "W":
            in_where_filter = True
            continue
        if word == "O":
            in_where_filter = False
            continue
        if word == "G":
            in_where_filter = False
            continue
        if in_where_filter:
            where_words.append(word)

    where_filter = " ".join(where_words)
    for sub_query_name in _get_saved_query_names(where_filter):
        sub_where_filter = _get_saved_where_filter(zdir, sub_query_name)
        if sub_where_filter is None:
            _LOGGER.error(
                "Failed to get saved WHERE filter from subquery name",
                query_name=query_name,
                sub_query_name=sub_query_name,
            )
            return None
        where_filter = where_filter.replace(
            f"{{{sub_query_name}}}", sub_where_filter
        )
    return where_filter
