"""Zorg's message bus lives here."""

from __future__ import annotations

from typing import Any, Callable, List

from logrus import Logger

from . import handlers
from ..domain import commands, events
from ..domain.types import Message
from ..storage.sql.session import ZorgSQLSession


logger = Logger(__name__)

COMMAND_HANDLERS: dict[
    type[commands.Command], Callable[[Any, ZorgSQLSession], None]
] = {
    commands.EditCommand: handlers.edit_zorg_files,
    commands.CheckKeepAliveFileCommand: handlers.check_keep_alive_file,
}
EVENT_HANDLERS: dict[
    type[events.Event], list[Callable[[Any, ZorgSQLSession], None]]
] = {}


def handle(messages: list[Message], session: ZorgSQLSession) -> None:
    """Entry point into Zorg's event messagebus loop."""
    queue = messages.copy()
    while queue:
        message = queue.pop(0)
        if isinstance(message, events.Event):
            handle_event(message, queue, session)
        elif isinstance(message, commands.Command):
            handle_command(message, queue, session)
        else:
            raise Exception(f"{message} was not an Event or Command")


def handle_event(
    event: events.Event,
    queue: List[Message],
    session: ZorgSQLSession,
) -> None:
    """Handles a single Zorg event."""
    for handler in EVENT_HANDLERS[type(event)]:
        try:
            logger.debug(
                "handling event with handler",
                zorg_event=str(event),
                handler=str(handler),
            )
            with session:
                handler(event, session)
                queue.extend(session.collect_new_messages())
        except Exception:
            logger.exception("Exception handling event", zorg_event=event)
            continue


def handle_command(
    command: commands.Command,
    queue: List[Message],
    session: ZorgSQLSession,
) -> None:
    """Handles a single Zorg command."""
    logger.debug("handling command", command=command)
    try:
        handler = COMMAND_HANDLERS[type(command)]
        with session:
            handler(command, session)
            queue.extend(session.collect_new_messages())
    except Exception:
        logger.exception("Exception handling command", command=command)
        raise
