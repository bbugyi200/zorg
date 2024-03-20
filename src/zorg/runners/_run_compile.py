"""Contains runners for the 'zorg compile' command."""

from dataclasses import dataclass, field
from pprint import pprint
from typing import Any, Literal

import antlr4

from ..config import CompileConfig
from ..grammar.zorg_file.ZorgFileLexer import ZorgFileLexer
from ..grammar.zorg_file.ZorgFileListener import ZorgFileListener
from ..grammar.zorg_file.ZorgFileParser import ZorgFileParser
from ..models import ZorgFile, ZorgNote, ZorgTodo
from ..types import TodoPriorityType
from ._registry import runner


TagName = Literal["areas", "contexts", "people", "projects"]


def _get_default_tags_map() -> dict[TagName, list[str]]:
    return {"areas": [], "projects": [], "contexts": [], "people": []}


@dataclass
class ZorgFileCompilerState:
    """Serves as a data store while parsing zorg files."""

    in_h1_header: bool = False
    in_h2_header: bool = False
    in_h3_header: bool = False
    in_h4_header: bool = False
    in_note: bool = False

    h1_section_tags: dict[TagName, list[str]] = field(
        default_factory=_get_default_tags_map
    )
    h2_section_tags: dict[TagName, list[str]] = field(
        default_factory=_get_default_tags_map
    )
    h3_section_tags: dict[TagName, list[str]] = field(
        default_factory=_get_default_tags_map
    )
    h4_section_tags: dict[TagName, list[str]] = field(
        default_factory=_get_default_tags_map
    )
    note_tags: dict[TagName, list[str]] = field(
        default_factory=_get_default_tags_map
    )

    h1_properties: dict[str, Any] = field(default_factory=lambda: {})
    h2_properties: dict[str, Any] = field(default_factory=lambda: {})
    h3_properties: dict[str, Any] = field(default_factory=lambda: {})
    h4_properties: dict[str, Any] = field(default_factory=lambda: {})
    note_properties: dict[str, Any] = field(default_factory=lambda: {})

    priority: TodoPriorityType = "C"

    @property
    def areas(self) -> list[str]:
        """Area tags that are currently in-scope."""
        return self._get_current_tags("areas")

    @property
    def contexts(self) -> list[str]:
        """Context tags that are currently in-scope."""
        return self._get_current_tags("contexts")

    @property
    def projects(self) -> list[str]:
        """Project tags that are currently in-scope."""
        return self._get_current_tags("projects")

    @property
    def people(self) -> list[str]:
        """People tags that are currently in-scope."""
        return self._get_current_tags("people")

    @property
    def properties(self) -> dict[str, Any]:
        """Properties that are currently in-scope."""
        return (
            self.h1_properties
            | self.h2_properties
            | self.h3_properties
            | self.h4_properties
            | self.note_properties
        )

    def _get_current_tags(self, tag_name: TagName) -> list[str]:
        tags = []
        tags.extend(self.h1_section_tags[tag_name])
        tags.extend(self.h2_section_tags[tag_name])
        tags.extend(self.h3_section_tags[tag_name])
        tags.extend(self.h4_section_tags[tag_name])
        tags.extend(self.note_tags[tag_name])
        return tags


class ZorgFileCompiler(ZorgFileListener):
    """Listener that compiles zorg files into zorc files."""

    def __init__(self, zorg_file: ZorgFile) -> None:
        self.zorg_file = zorg_file

        self._state = ZorgFileCompilerState()

    def enterH1_header(self, ctx: ZorgFileParser.H1_headerContext) -> None:
        del ctx
        self._state.in_h1_header = True

    def exitH1_header(self, ctx: ZorgFileParser.H1_headerContext) -> None:
        del ctx
        self._state.in_h1_header = False

    def exitH1_section(self, ctx: ZorgFileParser.H1_headerContext) -> None:
        del ctx
        self._state.h1_section_tags = _get_default_tags_map()
        self._state.h1_properties = {}

    def enterH2_header(self, ctx: ZorgFileParser.H2_headerContext) -> None:
        del ctx
        self._state.in_h2_header = True

    def exitH2_header(self, ctx: ZorgFileParser.H2_headerContext) -> None:
        del ctx
        self._state.in_h2_header = False

    def exitH2_section(self, ctx: ZorgFileParser.H2_headerContext) -> None:
        del ctx
        self._state.h2_section_tags = _get_default_tags_map()
        self._state.h2_properties = {}

    def enterH3_header(self, ctx: ZorgFileParser.H3_headerContext) -> None:
        del ctx
        self._state.in_h3_header = True

    def exitH3_header(self, ctx: ZorgFileParser.H3_headerContext) -> None:
        del ctx
        self._state.in_h3_header = False

    def exitH3_section(self, ctx: ZorgFileParser.H3_headerContext) -> None:
        del ctx
        self._state.h3_section_tags = _get_default_tags_map()
        self._state.h3_properties = {}

    def enterH4_header(self, ctx: ZorgFileParser.H4_headerContext) -> None:
        del ctx
        self._state.in_h4_header = True

    def exitH4_header(self, ctx: ZorgFileParser.H4_headerContext) -> None:
        del ctx
        self._state.in_h4_header = False

    def exitH4_section(self, ctx: ZorgFileParser.H4_headerContext) -> None:
        del ctx
        self._state.h4_section_tags = _get_default_tags_map()
        self._state.h4_properties = {}

    def enterProject(self, ctx: ZorgFileParser.ProjectContext) -> None:
        self._add_tags(ctx, "projects")

    def enterPerson(self, ctx: ZorgFileParser.PersonContext) -> None:
        self._add_tags(ctx, "people")

    def enterContext(self, ctx: ZorgFileParser.ContextContext) -> None:
        self._add_tags(ctx, "contexts")

    def enterArea(self, ctx: ZorgFileParser.AreaContext) -> None:
        self._add_tags(ctx, "areas")

    def enterPriority(self, ctx: ZorgFileParser.PriorityContext) -> None:
        self._state.priority = ctx.ID().getText()[0].upper()

    def enterProperty(self, ctx: ZorgFileParser.PropertyContext) -> None:
        key, value = [x.getText() for x in ctx.ID()]
        if self._state.in_h1_header:
            self._state.h1_properties[key] = value
        elif self._state.in_h2_header:
            self._state.h2_properties[key] = value
        elif self._state.in_h3_header:
            self._state.h3_properties[key] = value
        elif self._state.in_h4_header:
            self._state.h4_properties[key] = value
        elif self._state.in_note:
            self._state.note_properties[key] = value

    def enterNote(self, ctx: ZorgFileParser.NoteContext) -> None:
        self._state.in_note = True
        del ctx

    def exitNote(self, ctx: ZorgFileParser.NoteContext) -> None:
        self._state.in_note = False
        kwargs: dict[str, Any] = {
            "areas": self._state.areas,
            "contexts": self._state.contexts,
            "people": self._state.people,
            "projects": self._state.projects,
            "properties": self._state.properties,
        }
        self.zorg_file.notes.append(
            ZorgNote(ctx.space_atoms().getText(), self.zorg_file, **kwargs)
        )
        self._state.note_properties = {}

    def enterTodo(self, ctx: ZorgFileParser.TodoContext) -> None:
        self._state.in_note = True
        del ctx

    def exitTodo(self, ctx: ZorgFileParser.TodoContext) -> None:
        self._state.in_note = False
        kwargs: dict[str, Any] = {
            "areas": self._state.areas,
            "contexts": self._state.contexts,
            "people": self._state.people,
            "projects": self._state.projects,
            "properties": self._state.properties,
            "priority": self._state.priority,
        }
        self.zorg_file.todos.append(
            ZorgTodo(ctx.space_atoms().getText(), self.zorg_file, **kwargs)
        )
        # Reset priority back to default.
        self._state.priority = "C"
        self._state.note_properties = {}

    def _add_tags(
        self, ctx: antlr4.ParserRuleContext, tag_name: TagName
    ) -> None:
        text = ctx.children[1].getText()
        if self._state.in_h1_header:
            self._state.h1_section_tags[tag_name].append(text)
        elif self._state.in_h2_header:
            self._state.h2_section_tags[tag_name].append(text)
        elif self._state.in_h3_header:
            self._state.h3_section_tags[tag_name].append(text)
        elif self._state.in_h4_header:
            self._state.h4_section_tags[tag_name].append(text)
        elif self._state.in_note:
            self._state.note_tags[tag_name].append(text)


@runner
def run_compile(cfg: CompileConfig) -> int:
    """Runner for the 'compile' command."""
    stream = antlr4.FileStream(str(cfg.zo_path))
    lexer = ZorgFileLexer(stream)
    tokens = antlr4.CommonTokenStream(lexer)
    parser = ZorgFileParser(tokens)
    tree = parser.prog()
    compiler = ZorgFileCompiler(ZorgFile(cfg.zo_path))
    walker = antlr4.ParseTreeWalker()
    walker.walk(compiler, tree)
    pprint(compiler.zorg_file)
    return 0
