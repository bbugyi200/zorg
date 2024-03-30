"""Contains runners for the 'zorg compile' command."""

from dataclasses import asdict
from pprint import pprint

import antlr4

from ..compiler import ZorgFileCompiler
from ..config import CompileConfig
from ..grammar.zorg_file.ZorgFileLexer import ZorgFileLexer
from ..grammar.zorg_file.ZorgFileParser import ZorgFileParser
from ..models import ZorgFile
from ._runners import runner


@runner
def run_compile(cfg: CompileConfig) -> int:
    """Runner for the 'compile' command."""
    stream = antlr4.FileStream(str(cfg.zo_path))
    lexer = ZorgFileLexer(stream)
    tokens = antlr4.CommonTokenStream(lexer)
    parser = ZorgFileParser(tokens)
    tree = parser.prog()  # type: ignore[no-untyped-call]
    compiler = ZorgFileCompiler(ZorgFile(cfg.zo_path))
    walker = antlr4.ParseTreeWalker()
    walker.walk(compiler, tree)
    zorg_file_dict = asdict(compiler.zorg_file)
    del zorg_file_dict["path"]
    pprint(zorg_file_dict)
    return 0
