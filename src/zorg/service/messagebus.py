"""Zorg's message bus lives here."""

from __future__ import annotations

from typing import Any, Callable, MutableSequence, Sequence

from logrus import Logger
from typist import assert_never

from . import handlers
from ..domain.messages import Message, commands, events
from ..storage.sql.session import SQLSession


logger = Logger(__name__)

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
    events.NewZorgNotesEvent: [handlers.add_zids_to_notes_in_file],
    events.DBModifiedEvent: [handlers.increment_zid_counters],
}


def handle(messages: Sequence[Message], session: SQLSession) -> None:
    """Entry point into Zorg's event messagebus loop."""
    queue = list(messages)
    while queue:
        message = queue.pop(0)
        _handle_message(message, queue, session)


def _handle_message(
    message: Message, queue: MutableSequence[Message], session: SQLSession
) -> None:
    with session:
        if isinstance(message, events.Event):
            _handle_event(message, queue, session)
        elif isinstance(message, commands.Command):
            _handle_command(message, queue, session)
        else:
            assert_never(message)


def _handle_event(
    event: events.Event,
    queue: MutableSequence[Message],
    session: SQLSession,
) -> None:
    for handler in EVENT_HANDLERS[type(event)]:
        try:
            logger.debug(
                "handling event with handler",
                zorg_event=str(event),
                handler=str(handler),
            )
            handler(event, session)
            queue.extend(session.collect_new_messages())
        except Exception:
            logger.exception("Exception handling event", zorg_event=event)
            continue


def _handle_command(
    command: commands.Command,
    queue: MutableSequence[Message],
    session: SQLSession,
) -> None:
    logger.debug("handling command", command=command)
    try:
        handler = COMMAND_HANDLERS[type(command)]
        handler(command, session)
        queue.extend(session.collect_new_messages())
    except Exception:
        logger.exception("Exception handling command", command=command)
        raise
