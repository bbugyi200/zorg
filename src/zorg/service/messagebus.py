"""Zorg's message bus lives here."""

from __future__ import annotations

from typing import Any, Callable, List

from logrus import Logger

from . import handlers
from ..domain.messages import Message, commands, events
from ..storage.sql.session import SQLSession


logger = Logger(__name__)

COMMAND_HANDLERS: dict[
    type[commands.Command], Callable[[Any, SQLSession], None]
] = {
    commands.EditCommand: handlers.edit_files,
    commands.CreateDBCommand: handlers.create_database,
}
EVENT_HANDLERS: dict[
    type[events.Event], list[Callable[[Any, SQLSession], None]]
] = {events.EditorClosedEvent: [handlers.check_keep_alive_file]}


def handle(messages: list[Message], session: SQLSession) -> None:
    """Entry point into Zorg's event messagebus loop."""
    queue = messages.copy()
    while queue:
        message = queue.pop(0)
        with session:
            if isinstance(message, events.Event):
                handle_event(message, queue, session)
            elif isinstance(message, commands.Command):
                handle_command(message, queue, session)
            else:
                raise Exception(f"{message} was not an Event or Command")


def handle_event(
    event: events.Event,
    queue: List[Message],
    session: SQLSession,
) -> None:
    """Handles a single Zorg event."""
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


def handle_command(
    command: commands.Command,
    queue: List[Message],
    session: SQLSession,
) -> None:
    """Handles a single Zorg command."""
    logger.debug("handling command", command=command)
    try:
        handler = COMMAND_HANDLERS[type(command)]
        handler(command, session)
        queue.extend(session.collect_new_messages())
    except Exception:
        logger.exception("Exception handling command", command=command)
        raise
