"""The public API for the zorg.service.compiler package."""

from pathlib import Path

import antlr4
from antlr4.error.ErrorListener import ErrorListener
from logrus import Logger
from typist import assert_never

from ...domain.models import TodoPayload, ZorgFile, ZorgNote
from ...domain.types import TodoPriorityType, TodoStatus, TodoStatusPrefixChar
from ...grammar.zorg_file.ZorgFileLexer import ZorgFileLexer
from ...grammar.zorg_file.ZorgFileListener import ZorgFileListener
from ...grammar.zorg_file.ZorgFileParser import ZorgFileParser


def walk_zorg_file(
    zdir: Path, zo_path_part: Path, verbose: bool = False
) -> ZorgFile:
    """Create a new _ZorgFileCompiler and walk through notes in {zorg_file}."""
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
    error_manager = _ErrorManager()
    parser.addErrorListener(error_manager)
    tree = parser.prog()
    compiler = _ZorgFileCompiler(zorg_file, error_manager)
    walker = antlr4.ParseTreeWalker()
    walker.walk(compiler, tree)
    return zorg_file
