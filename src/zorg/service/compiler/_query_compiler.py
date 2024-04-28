"""Contains service logic used to compile zorg queries."""

from typing import cast

from logrus import Logger

from ...domain.models import ZorgQuery
from ...domain.types import Select
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
        del ctx
