"""Contains service logic used to compile zorg queries."""

from ...grammar.zorg_query.ZorgQueryListener import ZorgQueryListener
from ...grammar.zorg_query.ZorgQueryParser import ZorgQueryParser


class ZorgQueryCompiler(ZorgQueryListener):
    """Listener that compiles zorg queries."""

    def enterSelect(
        self, ctx: ZorgQueryParser.SelectContext
    ) -> None:  # noqa: D102
        print(ctx.getText())
