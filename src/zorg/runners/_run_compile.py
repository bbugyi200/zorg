"""Contains runners for the 'zorg compile' command."""

import antlr4

from ..config import CompileConfig
from ..grammar.zorg_file.ZorgFileLexer import ZorgFileLexer
from ..grammar.zorg_file.ZorgFileListener import ZorgFileListener
from ..grammar.zorg_file.ZorgFileParser import ZorgFileParser
from ._registry import runner


class ZorgFileCompiler(ZorgFileListener):
    """Listener that compiles zorg files into zorc files."""

    def enterBlock(self, ctx: ZorgFileParser.BlockContext) -> None:
        del ctx


@runner
def run_compile(cfg: CompileConfig) -> int:
    """Runner for the 'compile' command."""
    stream = antlr4.FileStream(str(cfg.zo_path))
    lexer = ZorgFileLexer(stream)
    tokens = antlr4.CommonTokenStream(lexer)
    parser = ZorgFileParser(tokens)
    tree = parser.prog()
    compiler = ZorgFileCompiler()
    walker = antlr4.ParseTreeWalker()
    walker.walk(compiler, tree)
    return 0
