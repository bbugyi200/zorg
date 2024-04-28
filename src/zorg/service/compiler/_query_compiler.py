"""Contains service logic used to compile zorg queries."""

from ...domain.models import ZorgQuery
from ...grammar.zorg_query.ZorgQueryListener import ZorgQueryListener
from ...grammar.zorg_query.ZorgQueryParser import ZorgQueryParser


class ZorgQueryCompiler(ZorgQueryListener):
    """Listener that compiles zorg queries."""

    def __init__(self, zorg_query: ZorgQuery) -> None:
        self.zorg_query = zorg_query

    def enterSelect(
        self, ctx: ZorgQueryParser.SelectContext
    ) -> None:  # noqa: D102
        print(ctx.getText())
