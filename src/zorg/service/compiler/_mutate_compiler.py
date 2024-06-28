"""Contains service logic used to compile mutate commands."""

from ...grammar.zorg_mutate.ZorgMutateListener import ZorgMutateListener
from ...grammar.zorg_mutate.ZorgMutateParser import ZorgMutateParser


class ZorgMutateCompiler(ZorgMutateListener):
    """Listener that compiles zorg mutate commands."""

    def enterMut_prop(
        self, ctx: ZorgMutateParser.Mut_propContext
    ) -> None:  # noqa: D102
        del ctx
