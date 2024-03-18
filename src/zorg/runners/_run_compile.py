"""Contains runners for the 'zorg compile' command."""

import antlr4

from ..config import CompileConfig
from ..grammar.zorg_file.ZorgFileLexer import ZorgFileLexer
from ..grammar.zorg_file.ZorgFileListener import ZorgFileListener
from ..grammar.zorg_file.ZorgFileParser import ZorgFileParser
from ._registry import runner


def _get_default_tags_map() -> dict[str, list[str]]:
    return {"roles": [], "projects": [], "contexts": [], "people": []}


class ZorgFileCompiler(ZorgFileListener):
    """Listener that compiles zorg files into zorc files."""

    in_h1_header: bool = False
    h1_section_tags: dict[str, list[str]] = _get_default_tags_map()

    def enterH1_header(self, ctx: ZorgFileParser.H1_headerContext) -> None:
        del ctx
        self.in_h1_header = True

    def exitH1_header(self, ctx: ZorgFileParser.H1_headerContext) -> None:
        del ctx
        self.in_h1_header = False

    def exitH1_section(self, ctx: ZorgFileParser.H1_headerContext) -> None:
        del ctx
        self.h1_section_tags = _get_default_tags_map()

    def enterProject(self, ctx: ZorgFileParser.ProjectContext) -> None:
        if self.in_h1_header:
            self.h1_section_tags["projects"].append(ctx.children[1].getText())

    def enterPerson(self, ctx: ZorgFileParser.PersonContext) -> None:
        if self.in_h1_header:
            self.h1_section_tags["people"].append(ctx.children[1].getText())

    def enterNote(self, ctx: ZorgFileParser.NoteContext) -> None:
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
