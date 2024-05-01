"""Contains service logic used to compile zorg queries."""

from typing import cast

from logrus import Logger

from ...domain.models import WhereAndFilter, WhereOrFilter, ZorgQuery
from ...domain.types import NoteStatus, Select
from ...grammar.zorg_query.ZorgQueryListener import ZorgQueryListener
from ...grammar.zorg_query.ZorgQueryParser import ZorgQueryParser


_LOGGER = Logger(__name__)


class ZorgQueryCompiler(ZorgQueryListener):
    """Listener that compiles zorg queries."""

    def __init__(self, zorg_query: ZorgQuery) -> None:
        self.zorg_query = zorg_query

    def enterSelect(
        self, ctx: ZorgQueryParser.SelectContext
    ) -> None:  # noqa: D102
        select_body = cast(
            ZorgQueryParser.Select_bodyContext, ctx.select_body()
        )
        select: Select
        if select_body.AT_SIGN():
            select = Select.CONTEXTS
        elif select_body.HASH():
            select = Select.AREAS
        elif select_body.PERCENT():
            select = Select.PEOPLE
        elif select_body.PLUS():
            select = Select.PROJECTS
        elif select_body.getText() == "file":
            select = Select.FILES
        elif select_body.getText() == "note":
            select = Select.NOTES
        else:
            emsg = "Unrecognized select body"
            _LOGGER.error(emsg, select_body=select_body.getText())
            raise RuntimeError(emsg)

        self.zorg_query.select = select

    def enterWhere(
        self, ctx: ZorgQueryParser.WhereContext
    ) -> None:  # noqa: D102
        note_status = cast(
            ZorgQueryParser.Note_statusContext, ctx.where_body().note_status()
        )
        note_status_chars = cast(
            list[ZorgQueryParser.Note_status_charContext],
            note_status.note_status_char(),
        )
        allowed_note_statuses: set[NoteStatus] = set()
        where: WhereOrFilter
        for note_status_char in note_status_chars:
            if note_status_char.DASH():
                allowed_note_statuses.add(NoteStatus.BASIC)
            elif note_status_char.LOWER_O():
                allowed_note_statuses.add(NoteStatus.OPEN_TODO)
            elif note_status_char.LOWER_X():
                allowed_note_statuses.add(NoteStatus.CLOSED_TODO)
            elif note_status_char.TILDE():
                allowed_note_statuses.add(NoteStatus.CANCELED_TODO)
            elif note_status_char.LANGLE():
                allowed_note_statuses.add(NoteStatus.BLOCKED_TODO)
            elif note_status_char.RANGLE():
                allowed_note_statuses.add(NoteStatus.PARENT_TODO)
            else:
                emsg = "Unrecognized note status character"
                _LOGGER.error(
                    emsg, note_status_char=note_status_char.getText()
                )
                raise RuntimeError(emsg)
        where = WhereOrFilter(
            [WhereAndFilter(allowed_note_statuses=allowed_note_statuses)]
        )
        self.zorg_query.where = where
