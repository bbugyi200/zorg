"""The public API for the zorg.service.compiler package."""

from pathlib import Path

import antlr4

from zorg.domain.models import Page, Query
from zorg.grammar.zorg_file.ZorgFileLexer import ZorgFileLexer
from zorg.grammar.zorg_file.ZorgFileParser import ZorgFileParser
from zorg.grammar.zorg_query.ZorgQueryLexer import ZorgQueryLexer
from zorg.grammar.zorg_query.ZorgQueryParser import ZorgQueryParser

from ._file_compiler import ErrorManager, ZorgFileCompiler
from ._query_compiler import ZorgQueryCompiler


def walk_zorg_page(
    zdir: Path, zo_path_part: Path, verbose: bool = False
) -> Page:
    """Create a new ZorgFileCompiler and walk through notes in {zorg_page}."""
    zo_path = (
        zo_path_part if zo_path_part.is_absolute() else zdir / zo_path_part
    )
    zorg_page = Page(zo_path)
    stream = antlr4.FileStream(zorg_page.path, errors="ignore")
    lexer = ZorgFileLexer(stream)
    tokens = antlr4.CommonTokenStream(lexer)
    parser = ZorgFileParser(tokens)
    if not verbose:
        parser.removeErrorListeners()
    error_manager = ErrorManager()
    parser.addErrorListener(error_manager)
    tree = parser.prog()  # type: ignore[no-untyped-call]
    compiler = ZorgFileCompiler(zorg_page, error_manager)
    walker = antlr4.ParseTreeWalker()
    walker.walk(compiler, tree)
    return zorg_page


def build_zorg_query(qstring: str) -> Query:
    """Constructs a new Query using {qstring}."""
    stream = antlr4.InputStream(qstring)
    lexer = ZorgQueryLexer(stream)
    tokens = antlr4.CommonTokenStream(lexer)
    parser = ZorgQueryParser(tokens)
    tree = parser.prog()  # type: ignore[no-untyped-call]
    zorg_query = Query()
    compiler = ZorgQueryCompiler(zorg_query)
    walker = antlr4.ParseTreeWalker()
    walker.walk(compiler, tree)
    return zorg_query
