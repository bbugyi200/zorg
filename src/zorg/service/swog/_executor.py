"""Logic for executing zorg queries lives in this module."""

import time

from logrus import Logger

from ...domain.types import NoteType, SelectType
from ...storage.sql.session import SQLSession
from ..compiler import build_zorg_query


_LOGGER = Logger(__name__)


def execute(session: SQLSession, query_string: str) -> str:
    """Execute a zorg query and then render it as a .zo file.

    In other words, a Zorg query comes in and a Zorg file comes out.

    Arguments:
    ----------
    session: A zorg SQL session that MUST be instantiated (e.g. using `with
        session`) by the caller.
    query_string: A zorg query that MUST conform to the syntax defined by the
        [[src/zorg/grammar/zorg_query/ZorgQuery.g4]] grammar.

    Return:
    -------
    A string that MUST conform to the syntax defined by the
    [[src/zorg/grammar/zorg_file/ZorgFile.g4]] grammar's "body" parser rule.
    """
    query = build_zorg_query(query_string)
    # (W)HERE
    start_time = time.time()
    filtered_notes = session.repo.get_by_query(query.where)
    query_runtime = time.time() - start_time
    _LOGGER.info(
        "Query complete",
        num_of_notes=len(filtered_notes),
        seconds=f"{query_runtime:.3f}",
    )

    # (G)ROUP BY

    # (O)RDER BY

    # (S)ELECT
    result = ""
    if query.select is SelectType.NOTE:
        for note in filtered_notes:
            note_type = (
                note.todo_payload.status
                if note.todo_payload
                else NoteType.BASIC
            )
            char = note_type.to_prefix_char()
            priority = (
                f" [#{note.todo_payload.priority}]"
                if note.todo_payload
                else ""
            )
            result += f"{char}{priority} {note.body.strip()}\n"

    return result