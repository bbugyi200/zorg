"""Zorg's message bus lives here."""

from __future__ import annotations

from pathlib import Path
from typing import Any, Callable, Sequence

from logrus import Logger
from typist import PathLike, assert_never

from zorg.domain.messages import Message, commands, events
from zorg.service import handlers
from zorg.storage.sql import SQLSession

_LOGGER = Logger(__name__)

MessageHandler = Callable[[Any, SQLSession], None]
COMMAND_HANDLERS: dict[type[commands.Command], MessageHandler] = {
    commands.EditCommand: handlers.edit_files,
    commands.CreateDBCommand: handlers.create_database,
    commands.ReindexDBCommand: handlers.reindex_database,
}
EVENT_HANDLERS: dict[type[events.Event], list[MessageHandler]] = {
    events.EditorClosedEvent: [
        handlers.check_keep_alive_file,
        handlers.reindex_database_after_edit,
    ],
    events.ModifiedZorgNotesEvent: [handlers.update_note_modify_dates],
    events.NewZorgNotesEvent: [handlers.add_zids_to_notes_in_file],
}


def handle(
    zdir: PathLike,
    db_url: str,
    messages: Sequence[Message],
    *,
    verbose: int = 0,
    should_delete_existing_db: bool = False,
) -> None:
    """Entry point into Zorg's event messagebus loop."""
    zdir = Path(zdir)
    with SQLSession(
        zdir,
        db_url,
        should_delete_existing_db=should_delete_existing_db,
        verbose=verbose,
    ) as session:
        return _handle(messages, session)


def _handle(messages: Sequence[Message], session: SQLSession) -> None:
    queue = list(messages)
    while queue := sorted(
        queue, key=lambda x: isinstance(x, commands.Command)
    ):
        message = queue.pop(0)
        _handle_message(message, session)
        queue.extend(session.collect_new_messages())


def _handle_message(message: Message, session: SQLSession) -> None:
    with session:
        if isinstance(message, events.Event):
            _handle_event(message, session)
        elif isinstance(message, commands.Command):
            _handle_command(message, session)
        else:
            assert_never(message)


def _handle_event(
    event: events.Event,
    session: SQLSession,
) -> None:
    for handler in EVENT_HANDLERS[type(event)]:
        _LOGGER.debug(
            "handling event with handler",
            zorg_event=str(event),
            handler=str(handler),
        )
        try:
            handler(event, session)
        except Exception:
            _LOGGER.exception("Exception handling event", zorg_event=event)
            continue


def _handle_command(
    command: commands.Command,
    session: SQLSession,
) -> None:
    _LOGGER.debug("handling command", command=command)
    try:
        handler = COMMAND_HANDLERS[type(command)]
        handler(command, session)
    except Exception:
        _LOGGER.exception("Exception handling command", command=command)
        raise
