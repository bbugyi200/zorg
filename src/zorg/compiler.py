"""Contains the ZorgFileCompiler class."""

from dataclasses import dataclass, field
from typing import Any, Literal

import antlr4
from logrus import Logger

from .grammar.zorg_file.ZorgFileListener import ZorgFileListener
from .grammar.zorg_file.ZorgFileParser import ZorgFileParser
from .models import ZorgFile, ZorgNote, ZorgTodo
from .types import TodoPriorityType


TagName = Literal["areas", "contexts", "people", "projects"]

logger = Logger(__name__)


class ZorgFileCompiler(ZorgFileListener):
    """Listener that compiles zorg files into zorc files."""

    def __init__(self, zorg_file: ZorgFile) -> None:
        self.zorg_file = zorg_file

        self._s = _ZorgFileCompilerState()

    def enterArea(self, ctx: ZorgFileParser.AreaContext) -> None:  # noqa: D102
        self._add_tags(ctx, "areas")

    def enterContext(
        self, ctx: ZorgFileParser.ContextContext
    ) -> None:  # noqa: D102
        self._add_tags(ctx, "contexts")

    def enterH1_header(
        self, ctx: ZorgFileParser.H1_headerContext
    ) -> None:  # noqa: D102
        del ctx
        self._s.in_h1_header = True

    def enterH2_header(
        self, ctx: ZorgFileParser.H2_headerContext
    ) -> None:  # noqa: D102
        del ctx
        self._s.in_h2_header = True

    def enterH3_header(
        self, ctx: ZorgFileParser.H3_headerContext
    ) -> None:  # noqa: D102
        del ctx
        self._s.in_h3_header = True

    def enterH4_header(
        self, ctx: ZorgFileParser.H4_headerContext
    ) -> None:  # noqa: D102
        del ctx
        self._s.in_h4_header = True

    def enterLink(self, ctx: ZorgFileParser.LinkContext) -> None:  # noqa: D102
        if self._s.in_note:
            link_text = ctx.children[1].getText()
            self._s.note_links.append(link_text)

    def enterNote(self, ctx: ZorgFileParser.NoteContext) -> None:  # noqa: D102
        self._s.in_note = True
        del ctx

    def enterPerson(
        self, ctx: ZorgFileParser.PersonContext
    ) -> None:  # noqa: D102
        self._add_tags(ctx, "people")

    def enterProject(
        self, ctx: ZorgFileParser.ProjectContext
    ) -> None:  # noqa: D102
        self._add_tags(ctx, "projects")

    def enterPriority(
        self, ctx: ZorgFileParser.PriorityContext
    ) -> None:  # noqa: D102
        self._s.priority = ctx.ID().getText()[0].upper()

    def enterProperty(
        self, ctx: ZorgFileParser.PropertyContext
    ) -> None:  # noqa: D102
        key, value = ctx.ID().getText(), ctx.id_group().getText()
        if self._s.in_h1_header:
            self._s.h1_properties[key] = value
        elif self._s.in_h2_header:
            self._s.h2_properties[key] = value
        elif self._s.in_h3_header:
            self._s.h3_properties[key] = value
        elif self._s.in_h4_header:
            self._s.h4_properties[key] = value
        elif self._s.in_note:
            self._s.note_properties[key] = value

    def enterTodo(self, ctx: ZorgFileParser.TodoContext) -> None:  # noqa: D102
        self._s.in_note = True
        del ctx

    def exitH1_header(
        self, ctx: ZorgFileParser.H1_headerContext
    ) -> None:  # noqa: D102
        del ctx
        self._s.in_h1_header = False

    def exitH1_section(
        self, ctx: ZorgFileParser.H1_headerContext
    ) -> None:  # noqa: D102
        del ctx
        self._s.h1_section_tags = _get_default_tags_map()
        self._s.h1_properties = {}

    def exitH2_header(
        self, ctx: ZorgFileParser.H2_headerContext
    ) -> None:  # noqa: D102
        del ctx
        self._s.in_h2_header = False

    def exitH2_section(
        self, ctx: ZorgFileParser.H2_headerContext
    ) -> None:  # noqa: D102
        del ctx
        self._s.h2_section_tags = _get_default_tags_map()
        self._s.h2_properties = {}

    def exitH3_header(
        self, ctx: ZorgFileParser.H3_headerContext
    ) -> None:  # noqa: D102
        del ctx
        self._s.in_h3_header = False

    def exitH3_section(
        self, ctx: ZorgFileParser.H3_headerContext
    ) -> None:  # noqa: D102
        del ctx
        self._s.h3_section_tags = _get_default_tags_map()
        self._s.h3_properties = {}

    def exitH4_header(
        self, ctx: ZorgFileParser.H4_headerContext
    ) -> None:  # noqa: D102
        del ctx
        self._s.in_h4_header = False

    def exitH4_section(
        self, ctx: ZorgFileParser.H4_headerContext
    ) -> None:  # noqa: D102
        del ctx
        self._s.h4_section_tags = _get_default_tags_map()
        self._s.h4_properties = {}

    def exitNote(self, ctx: ZorgFileParser.NoteContext) -> None:  # noqa: D102
        self._s.in_note = False
        kwargs: dict[str, Any] = {
            "areas": self._s.areas,
            "contexts": self._s.contexts,
            "links": self._s.note_links,
            "people": self._s.people,
            "projects": self._s.projects,
            "properties": self._s.properties,
        }
        self.zorg_file.notes.append(
            ZorgNote(ctx.space_atoms().getText(), **kwargs)
        )
        self._reset_note_context()

    def exitTodo(self, ctx: ZorgFileParser.TodoContext) -> None:  # noqa: D102
        self._s.in_note = False
        kwargs: dict[str, Any] = {
            "areas": self._s.areas,
            "contexts": self._s.contexts,
            "links": self._s.note_links,
            "people": self._s.people,
            "projects": self._s.projects,
            "properties": self._s.properties,
            "priority": self._s.priority,
        }
        self.zorg_file.todos.append(
            ZorgTodo(ctx.space_atoms().getText(), **kwargs)
        )
        # Reset priority back to default.
        self._s.priority = "C"
        self._reset_note_context()

    def _reset_note_context(self) -> None:
        self._s.note_tags = _get_default_tags_map()
        self._s.note_properties = {}
        self._s.note_links = []

    def _add_tags(
        self, ctx: antlr4.ParserRuleContext, tag_name: TagName
    ) -> None:
        text = ctx.children[1].getText()
        if all(ch.isdigit() for ch in text):
            logger.debug(
                "Tag identifiers cannot contain only digits.",
                tag_name=tag_name,
                ID=text,
            )
            return
        if self._s.in_h1_header:
            self._s.h1_section_tags[tag_name].append(text)
        elif self._s.in_h2_header:
            self._s.h2_section_tags[tag_name].append(text)
        elif self._s.in_h3_header:
            self._s.h3_section_tags[tag_name].append(text)
        elif self._s.in_h4_header:
            self._s.h4_section_tags[tag_name].append(text)
        elif self._s.in_note:
            self._s.note_tags[tag_name].append(text)


def _get_default_tags_map() -> dict[TagName, list[str]]:
    return {"areas": [], "projects": [], "contexts": [], "people": []}


@dataclass
class _ZorgFileCompilerState:
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

    note_links: list[str] = field(default_factory=lambda: [])

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
