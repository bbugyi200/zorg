"""Contains the ZorgFileCompiler class."""

from dataclasses import dataclass, field
import datetime as dt
from typing import Any, Literal, Optional

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

    def enterBase_note(
        self, ctx: ZorgFileParser.Base_noteContext
    ) -> None:  # noqa: D102
        self._s.in_note = True
        del ctx

    def enterContext(
        self, ctx: ZorgFileParser.ContextContext
    ) -> None:  # noqa: D102
        self._add_tags(ctx, "contexts")

    def enterDate(self, ctx: ZorgFileParser.DateContext) -> None:  # noqa: D102
        if self._s.in_note and self._s.ids_in_note == 1:
            self._s.note_date = dt.datetime.strptime(
                ctx.DATE().getText(), "%Y-%m-%d"
            )

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

    def enterId(self, ctx: ZorgFileParser.IdContext) -> None:  # noqa: D102
        del ctx
        if self._s.in_note:
            self._s.ids_in_note += 1

    def enterItem(self, ctx: ZorgFileParser.ItemContext) -> None:  # noqa: D102
        del ctx
        self._reset_note_context()

    def enterLink(self, ctx: ZorgFileParser.LinkContext) -> None:  # noqa: D102
        if self._s.in_note:
            link_text = ctx.children[1].getText()
            self._s.note_links.append(link_text)

    def enterNote(self, ctx: ZorgFileParser.NoteContext) -> None:  # noqa: D102
        del ctx
        self._s.parent_id = None

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

    def enterSubnote(
        self, ctx: ZorgFileParser.SubnoteContext
    ) -> None:  # noqa: D102
        del ctx
        if not self._s.in_subnote:
            self._s.parent_id = self._s.next_id - 1
        self._s.in_subnote = True
        self._reset_note_context()

    def enterSubsubnote(
        self, ctx: ZorgFileParser.SubsubnoteContext
    ) -> None:  # noqa: D102
        del ctx
        if not self._s.in_subsubnote:
            self._s.parent_id = self._s.next_id - 1
        self._s.in_subsubnote = True
        self._reset_note_context()

    def enterTodo(self, ctx: ZorgFileParser.TodoContext) -> None:  # noqa: D102
        self._s.in_note = True
        self._s.parent_id = None
        del ctx

    def exitBase_todo(
        self, ctx: ZorgFileParser.Base_todoContext
    ) -> None:  # noqa: D102
        self._s.in_note = False
        kwargs = self._get_note_kwargs({"priority": self._s.priority})
        todo = ZorgTodo(ctx.item_body().getText(), **kwargs)
        self.zorg_file.todos.append(todo)
        # Reset priority back to default.
        self._s.priority = "C"

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

    def exitComment(
        self, ctx: ZorgFileParser.CommentContext
    ) -> None:  # noqa: D102
        del ctx
        self._s.in_first_comment = False

    def exitBase_note(
        self, ctx: ZorgFileParser.Base_noteContext
    ) -> None:  # noqa: D102
        self._s.in_note = False
        extra_kwargs = {}
        if self._s.parent_id is not None:
            extra_kwargs["parent_note_id"] = self._s.parent_id
        kwargs = self._get_note_kwargs(extra_kwargs)
        note = ZorgNote(ctx.item_body().getText(), **kwargs)
        self.zorg_file.notes.append(note)

    def exitItem(self, ctx: ZorgFileParser.ItemContext) -> None:  # noqa: D102
        del ctx
        self._s.in_subnote = False

    def exitSubnote(
        self, ctx: ZorgFileParser.SubnoteContext
    ) -> None:  # noqa: D102
        self._s.in_subsubnote = False
        del ctx

    def exitSubsubnote(
        self, ctx: ZorgFileParser.SubsubnoteContext
    ) -> None:  # noqa: D102
        del ctx

    def _get_note_kwargs(
        self, extra_kwargs: dict[str, Any] = None
    ) -> dict[str, Any]:
        if extra_kwargs is None:
            extra_kwargs = {}
        kwargs: dict[str, Any] = {
            "areas": self._s.areas,
            "contexts": self._s.contexts,
            "ident": self._s.next_id,
            "links": self._s.note_links,
            "people": self._s.people,
            "projects": self._s.projects,
            "properties": self._s.properties,
        }
        self._s.next_id += 1
        if self._s.note_date is not None:
            kwargs["create_date"] = self._s.note_date
        return kwargs | extra_kwargs

    def _reset_note_context(self) -> None:
        self._s.ids_in_note = 0
        self._s.note_tags = _get_default_tags_map()
        self._s.note_properties = {}
        self._s.note_links = []
        self._s.note_date = None

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
        if self._s.in_first_comment:
            self._s.file_tags[tag_name].append(text)
        elif self._s.in_h1_header:
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

    ids_in_note: int = 0

    next_id: int = 1
    parent_id: Optional[int] = None

    in_first_comment: bool = True
    in_h1_header: bool = False
    in_h2_header: bool = False
    in_h3_header: bool = False
    in_h4_header: bool = False
    in_note: bool = False
    in_subnote: bool = False
    in_subsubnote: bool = False

    file_tags: dict[TagName, list[str]] = field(
        default_factory=_get_default_tags_map
    )
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
    note_date: Optional[dt.date] = None

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
        project: Optional[str] = None
        for tag_map in [
            self.file_tags,
            self.h1_section_tags,
            self.h2_section_tags,
            self.h3_section_tags,
            self.h4_section_tags,
            self.note_tags,
        ]:
            project_list = tag_map["projects"]
            if not project_list:
                continue
            inner_project = project_list[0]
            if project is None:
                project = inner_project
            elif project != inner_project:
                project = f"{project}/{inner_project}"

        return [] if project is None else [project]

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
        tags.extend(self.file_tags[tag_name])
        tags.extend(self.h1_section_tags[tag_name])
        tags.extend(self.h2_section_tags[tag_name])
        tags.extend(self.h3_section_tags[tag_name])
        tags.extend(self.h4_section_tags[tag_name])
        tags.extend(self.note_tags[tag_name])
        return tags
