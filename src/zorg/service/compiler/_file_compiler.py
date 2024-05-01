"""Contains service logic used to compile zorg files."""

from dataclasses import dataclass, field
import datetime as dt
from functools import partial
from typing import Any, Literal, Optional

import antlr4
from antlr4.error.ErrorListener import ErrorListener
from logrus import Logger
from typist import assert_never

from ...domain.models import TodoPayload, ZorgFile, ZorgNote
from ...domain.types import NoteStatus, TodoPriorityType, TodoStatusPrefixChar
from ...grammar.zorg_file.ZorgFileListener import ZorgFileListener
from ...grammar.zorg_file.ZorgFileParser import ZorgFileParser


TagName = Literal["areas", "contexts", "people", "projects"]

_LOGGER = Logger(__name__)


class ErrorManager(ErrorListener):
    """Keeps track of zorg file syntax errors."""

    def __init__(self) -> None:
        super().__init__()
        self.errors: list[str] = []

    def syntaxError(
        self,
        recognizer: Any,
        offendingSymbol: str,
        line: int,
        column: int,
        msg: str,
        e: Any,
    ) -> None:  # noqa: D102
        del recognizer, offendingSymbol, e
        self.errors.append(f"Line {line}:{column} {msg}")


class ZorgFileCompiler(ZorgFileListener):
    """Listener that compiles zorg files.

    This compiler takes as input a single *.zo file. When walked, it produces
    as output the {zorg_file} instance attribute.
    """

    def __init__(
        self, zorg_file: ZorgFile, error_manager: ErrorManager
    ) -> None:
        self.zorg_file = zorg_file
        self.error_manager = error_manager

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
        get_date = partial(
            dt.datetime.strptime, ctx.DATE().getText(), "%Y-%m-%d"
        )
        if (
            self._s.in_note
            and self._s.ids_in_note == 1
            and self._s.note_date is None
        ):
            self._s.note_date = get_date()
        elif self._s.in_h4_header:
            self._s.h4_date = get_date()
        elif self._s.in_h3_header:
            self._s.h3_date = get_date()
        elif self._s.in_h2_header:
            self._s.h2_date = get_date()
        elif self._s.in_h1_header:
            self._s.h1_date = get_date()
        elif self._s.in_first_comment:
            self._s.file_date = get_date()

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

    def enterHead(self, ctx: ZorgFileParser.HeadContext) -> None:  # noqa: D102
        del ctx
        self._s.in_head = True

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
        self._s.todo_priority = ctx.ID().getText()[0].upper()

    def enterProperty(
        self, ctx: ZorgFileParser.PropertyContext
    ) -> None:  # noqa: D102
        key, value = ctx.ID().getText(), ctx.id_group().getText()
        if self._s.in_head:
            self._s.file_props[key] = value
        elif self._s.in_h1_header:
            self._s.h1_props[key] = value
        elif self._s.in_h2_header:
            self._s.h2_props[key] = value
        elif self._s.in_h3_header:
            self._s.h3_props[key] = value
        elif self._s.in_h4_header:
            self._s.h4_props[key] = value
        elif self._s.in_note:
            self._s.note_props[key] = value

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

    def enterTodo_prefix(
        self, ctx: ZorgFileParser.Todo_prefixContext
    ) -> None:  # noqa: D102
        status = NoteStatus.OPEN_TODO
        if self._s.in_note:
            ch: TodoStatusPrefixChar = ctx.getText()[0]
            if ch == "o":
                status = NoteStatus.OPEN_TODO
            elif ch == "x":
                status = NoteStatus.CLOSED_TODO
            elif ch == "~":
                status = NoteStatus.CANCELED_TODO
            elif ch == "<":
                status = NoteStatus.BLOCKED_TODO
            elif ch == ">":
                status = NoteStatus.PARENT_TODO
            else:
                assert_never(ch)

            self._s.todo_status = status

    def enterZid(self, ctx: ZorgFileParser.ZidContext) -> None:  # noqa: D102
        if self._s.in_note and self._s.ids_in_note == 0:
            zid = ctx.getText()
            self._s.zid = zid
            zorg_id_date = f"20{zid.split('#')[0]}"
            self._s.note_date = dt.datetime.strptime(zorg_id_date, "%Y%m%d")

    def exitBase_todo(
        self, ctx: ZorgFileParser.Base_todoContext
    ) -> None:  # noqa: D102
        self._s.in_note = False
        kwargs = self._get_note_kwargs(
            ctx,
            {
                "todo_payload": TodoPayload(
                    priority=self._s.todo_priority, status=self._s.todo_status
                ),
            },
        )
        id_note_body = ctx.id_note_body()
        if id_note_body is None:
            _LOGGER.warning("Skipping todo with no note body")
        elif id_note_body.getText().strip() == "":
            _LOGGER.warning("Skipping todo with empty note body")
        elif self.error_manager.errors:
            _LOGGER.warning(
                "Skipping note since zorg file has errors.",
                file_path=str(self.zorg_file.path),
            )
            self.zorg_file.has_errors = True
        else:
            todo = ZorgNote(id_note_body.getText(), **kwargs)
            self.zorg_file.notes.append(todo)

        # Reset todo priority and status back to defaults.
        self._s.todo_priority = "C"
        self._s.todo_status = NoteStatus.OPEN_TODO

    def exitH1_header(
        self, ctx: ZorgFileParser.H1_headerContext
    ) -> None:  # noqa: D102
        del ctx
        self._s.in_h1_header = False

    def exitH1_section(
        self, ctx: ZorgFileParser.H1_headerContext
    ) -> None:  # noqa: D102
        del ctx
        self._s.h1_tags = _get_default_tags_map()
        self._s.h1_date = None
        self._s.h1_props = {}

    def exitH2_header(
        self, ctx: ZorgFileParser.H2_headerContext
    ) -> None:  # noqa: D102
        del ctx
        self._s.in_h2_header = False

    def exitH2_section(
        self, ctx: ZorgFileParser.H2_headerContext
    ) -> None:  # noqa: D102
        del ctx
        self._s.h2_tags = _get_default_tags_map()
        self._s.h2_date = None
        self._s.h2_props = {}

    def exitH3_header(
        self, ctx: ZorgFileParser.H3_headerContext
    ) -> None:  # noqa: D102
        del ctx
        self._s.in_h3_header = False

    def exitH3_section(
        self, ctx: ZorgFileParser.H3_headerContext
    ) -> None:  # noqa: D102
        del ctx
        self._s.h3_tags = _get_default_tags_map()
        self._s.h3_date = None
        self._s.h3_props = {}

    def exitH4_header(
        self, ctx: ZorgFileParser.H4_headerContext
    ) -> None:  # noqa: D102
        del ctx
        self._s.in_h4_header = False

    def exitH4_section(
        self, ctx: ZorgFileParser.H4_headerContext
    ) -> None:  # noqa: D102
        del ctx
        self._s.h4_tags = _get_default_tags_map()
        self._s.h4_date = None
        self._s.h4_props = {}

    def exitHead(self, ctx: ZorgFileParser.HeadContext) -> None:  # noqa: D102
        del ctx
        self._s.in_head = False

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
        kwargs = self._get_note_kwargs(ctx, extra_kwargs)
        body: str = ctx.id_note_body().getText().strip()
        if body == "":
            _LOGGER.warning(
                "Skipping note with empty body",
                file_path=str(self.zorg_file.path),
            )
            return

        if self.error_manager.errors:
            _LOGGER.warning(
                "Skipping note since zorg file has errors.",
                file_path=str(self.zorg_file.path),
            )
            self.zorg_file.has_errors = True
            return

        note = ZorgNote(body, **kwargs)
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
        self,
        ctx: antlr4.ParserRuleContext,
        extra_kwargs: dict[str, Any] = None,
    ) -> dict[str, Any]:
        if extra_kwargs is None:
            extra_kwargs = {}
        kwargs: dict[str, Any] = {
            "areas": self._s.areas,
            "contexts": self._s.contexts,
            "create_date": self._s.create_date,
            "line_no": ctx.start.line,
            "links": self._s.note_links,
            "people": self._s.people,
            "projects": self._s.projects,
            "properties": self._s.properties,
            "zid": self._s.zid,
        }
        self._s.next_id += 1
        return kwargs | extra_kwargs

    def _reset_note_context(self) -> None:
        self._s.zid = None
        self._s.ids_in_note = 0
        self._s.note_tags = _get_default_tags_map()
        self._s.note_props = {}
        self._s.note_links = []
        self._s.note_date = None

    def _add_tags(
        self, ctx: antlr4.ParserRuleContext, tag_name: TagName
    ) -> None:
        text = ctx.children[1].getText()
        if all(ch.isdigit() for ch in text):
            _LOGGER.debug(
                "Tag identifiers cannot contain only digits.",
                tag_name=tag_name,
                ID=text,
            )
            return
        if self._s.in_first_comment:
            self._s.file_tags[tag_name].append(text)
        elif self._s.in_h1_header:
            self._s.h1_tags[tag_name].append(text)
        elif self._s.in_h2_header:
            self._s.h2_tags[tag_name].append(text)
        elif self._s.in_h3_header:
            self._s.h3_tags[tag_name].append(text)
        elif self._s.in_h4_header:
            self._s.h4_tags[tag_name].append(text)
        elif self._s.in_note:
            self._s.note_tags[tag_name].append(text)


def _get_default_tags_map() -> dict[TagName, list[str]]:
    return {"areas": [], "projects": [], "contexts": [], "people": []}


@dataclass
class _ZorgFileCompilerState:
    """Serves as a data store while parsing zorg files."""

    zid: Optional[str] = None

    ids_in_note: int = 0

    # TODO(bugyi): Figure out a better way to track parent/child relationship
    next_id: int = 1
    parent_id: Optional[int] = None

    in_first_comment: bool = True
    in_head: bool = False
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
    h1_tags: dict[TagName, list[str]] = field(
        default_factory=_get_default_tags_map
    )
    h2_tags: dict[TagName, list[str]] = field(
        default_factory=_get_default_tags_map
    )
    h3_tags: dict[TagName, list[str]] = field(
        default_factory=_get_default_tags_map
    )
    h4_tags: dict[TagName, list[str]] = field(
        default_factory=_get_default_tags_map
    )
    note_tags: dict[TagName, list[str]] = field(
        default_factory=_get_default_tags_map
    )

    file_props: dict[str, Any] = field(default_factory=lambda: {})
    h1_props: dict[str, Any] = field(default_factory=lambda: {})
    h2_props: dict[str, Any] = field(default_factory=lambda: {})
    h3_props: dict[str, Any] = field(default_factory=lambda: {})
    h4_props: dict[str, Any] = field(default_factory=lambda: {})
    note_props: dict[str, Any] = field(default_factory=lambda: {})

    note_links: list[str] = field(default_factory=lambda: [])

    file_date: Optional[dt.date] = None
    h1_date: Optional[dt.date] = None
    h2_date: Optional[dt.date] = None
    h3_date: Optional[dt.date] = None
    h4_date: Optional[dt.date] = None
    note_date: Optional[dt.date] = None

    todo_priority: TodoPriorityType = "C"
    todo_status: NoteStatus = NoteStatus.OPEN_TODO

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
            self.file_props
            | self.h1_props
            | self.h2_props
            | self.h3_props
            | self.h4_props
            | self.note_props
        )

    @property
    def create_date(self) -> dt.date:
        """Create date based on file header, sections, zorg IDs, etc...."""
        if self.note_date:
            return self.note_date
        elif self.h4_date:
            return self.h4_date
        elif self.h3_date:
            return self.h3_date
        elif self.h2_date:
            return self.h2_date
        elif self.h1_date:
            return self.h1_date
        elif self.file_date:
            return self.file_date
        else:
            return dt.date.today()

    def _get_current_tags(self, tag_name: TagName) -> list[str]:
        tags = []
        tags.extend(self.file_tags[tag_name])
        tags.extend(self.h1_tags[tag_name])
        tags.extend(self.h2_tags[tag_name])
        tags.extend(self.h3_tags[tag_name])
        tags.extend(self.h4_tags[tag_name])
        tags.extend(self.note_tags[tag_name])
        return sorted(set(tags))
