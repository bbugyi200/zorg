"""The public API for the zorg.service.compiler package."""

from pathlib import Path

import antlr4

from ...domain.models import ZorgFile, ZorgQuery
from ...grammar.zorg_file.ZorgFileLexer import ZorgFileLexer
from ...grammar.zorg_file.ZorgFileParser import ZorgFileParser
from ._file_compiler import ErrorManager, ZorgFileCompiler


def walk_zorg_file(
    zdir: Path, zo_path_part: Path, verbose: bool = False
) -> ZorgFile:
    """Create a new ZorgFileCompiler and walk through notes in {zorg_file}."""
    zo_path = (
        zo_path_part if zo_path_part.is_absolute() else zdir / zo_path_part
    )
    zorg_file = ZorgFile(zo_path)
    stream = antlr4.FileStream(zorg_file.path, errors="ignore")
    lexer = ZorgFileLexer(stream)
    tokens = antlr4.CommonTokenStream(lexer)
    parser = ZorgFileParser(tokens)
    if not verbose:
        parser.removeErrorListeners()
    error_manager = ErrorManager()
    parser.addErrorListener(error_manager)
    tree = parser.prog()  # type: ignore[no-untyped-call]
    compiler = ZorgFileCompiler(zorg_file, error_manager)
    walker = antlr4.ParseTreeWalker()
    walker.walk(compiler, tree)
    return zorg_file


def compile_zorg_query(query: str) -> ZorgQuery:
    """Create a new ZorgQueryCompiler and use it to compile {query}."""
    del query
    return ZorgQuery()
