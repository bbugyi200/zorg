"""Contains service logic used to compile zorg queries."""

from typing import cast

from logrus import Logger

from ...domain.models import Query, WhereAndFilter, WhereOrFilter
from ...domain.types import NoteType, SelectType, TodoPriorityType
from ...grammar.zorg_query.ZorgQueryListener import ZorgQueryListener
from ...grammar.zorg_query.ZorgQueryParser import ZorgQueryParser


_LOGGER = Logger(__name__)


class ZorgQueryCompiler(ZorgQueryListener):
    """Listener that compiles zorg queries."""

    def __init__(self, zorg_query: Query) -> None:
        self.zorg_query = zorg_query

        self._and_filters: list[WhereAndFilter] = []

    def enterSelect(
        self, ctx: ZorgQueryParser.SelectContext
    ) -> None:  # noqa: D102
        select_body = cast(
            ZorgQueryParser.Select_bodyContext, ctx.select_body()
        )
        select: SelectType
        if select_body.AT_SIGN():
            select = SelectType.CONTEXTS
        elif select_body.HASH():
            select = SelectType.AREAS
        elif select_body.PERCENT():
            select = SelectType.PEOPLE
        elif select_body.PLUS():
            select = SelectType.PROJECTS
        elif select_body.getText() == "file":
            select = SelectType.FILES
        elif select_body.getText() == "note":
            select = SelectType.NOTES
        else:
            emsg = "Unrecognized select body"
            _LOGGER.error(emsg, select_body=select_body.getText())
            raise RuntimeError(emsg)

        self.zorg_query.select = select

    def enterAnd_filter(
        self, ctx: ZorgQueryParser.And_filterContext
    ) -> None:  # noqa: D102
        where_atoms = cast(
            list[ZorgQueryParser.Where_atomContext], ctx.where_atom()
        )
        allowed_note_statuses: set[NoteType] = set()
        priorities: set[TodoPriorityType] = set()
        for where_atom in where_atoms:
            if where_atom.note_status():
                note_status = cast(
                    ZorgQueryParser.Note_statusContext,
                    where_atom.note_status(),
                )
                note_status_chars = cast(
                    list[ZorgQueryParser.Note_status_charContext],
                    note_status.note_status_char(),
                )
                _add_note_statuses(note_status_chars, allowed_note_statuses)
            elif where_atom.priority_range():
                priority_range = cast(
                    ZorgQueryParser.Priority_rangeContext,
                    where_atom.priority_range(),
                )
                _add_priorities(priority_range, priorities)

        self._and_filters.append(
            WhereAndFilter(
                allowed_note_statuses=allowed_note_statuses,
                priorities=priorities,
            )
        )

    def exitWhere(
        self, ctx: ZorgQueryParser.WhereContext
    ) -> None:  # noqa: D102
        del ctx
        where = WhereOrFilter(self._and_filters)
        self.zorg_query.where = where


def _add_note_statuses(
    note_status_chars: list[ZorgQueryParser.Note_status_charContext],
    allowed_note_statuses: set[NoteType],
) -> None:
    for note_status_char in note_status_chars:
        if note_status_char.DASH():
            allowed_note_statuses.add(NoteType.BASIC)
        elif note_status_char.LOWER_O():
            allowed_note_statuses.add(NoteType.OPEN_TODO)
        elif note_status_char.LOWER_X():
            allowed_note_statuses.add(NoteType.CLOSED_TODO)
        elif note_status_char.TILDE():
            allowed_note_statuses.add(NoteType.CANCELED_TODO)
        elif note_status_char.LANGLE():
            allowed_note_statuses.add(NoteType.BLOCKED_TODO)
        elif note_status_char.RANGLE():
            allowed_note_statuses.add(NoteType.PARENT_TODO)
        else:
            emsg = "Unrecognized note status character"
            _LOGGER.error(emsg, note_status_char=note_status_char.getText())
            raise RuntimeError(emsg)


def _add_priorities(
    priority_range: ZorgQueryParser.Priority_rangeContext,
    priorities: set[TodoPriorityType],
) -> None:
    for ID in priority_range.ID():
        pletter: str = ID.getText().upper()
        assert (
            len(pletter) == 1 and pletter.isalpha()
        ), f"Invalid priority: {pletter}"
        priorities.add(cast(TodoPriorityType, pletter))
