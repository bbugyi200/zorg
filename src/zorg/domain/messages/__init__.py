"""zorg.domain.messages

Messages used to register events that happened / commands that should be
performed live in this package.
"""

from typing import Union

from . import commands, events


Message = Union[commands.Command, events.Event]

__all__ = ["Message", "commands", "events"]
