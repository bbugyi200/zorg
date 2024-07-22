"""Contains service logic used to compile zorg files."""

from dataclasses import dataclass, field
import datetime as dt
from functools import partial
import re
from typing import Any, Final, Mapping, Optional

from antlr4.error.ErrorListener import ErrorListener
from logrus import Logger
from typist import assert_never

from zorg.domain.models import (
    H1,
    H2,
    H3,
    H4,
    Block,
    Note,
    Page,
    Section,
    TodoPayload,
)
from zorg.domain.types import NoteType, TagName, TodoPriorityType, TodoTypeChar
from zorg.grammar.zorg_file.ZorgFileListener import ZorgFileListener
from zorg.grammar.zorg_file.ZorgFileParser import ZorgFileParser
from zorg.shared import dates as zdt


_DEFAULT_PRIORITY: Final[TodoPriorityType] = "P3"
_LOGGER = Logger(__name__)
_TagDict = dict[TagName, list[str]]


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
    as output the {page} instance attribute.
    """

    def __init__(self, page: Page, error_manager: ErrorManager) -> None:
        self.page = page
        self.error_manager = error_manager

        self._s = _ZorgFileCompilerState()

    def enterArea(self, ctx: ZorgFileParser.AreaContext) -> None:  # noqa: D102
        self._add_tag("areas", ctx.children[1].getText())

    def enterBase_note(
        self, ctx: ZorgFileParser.Base_noteContext
    ) -> None:  # noqa: D102
        self._s.in_note = True
        del ctx

    def enterBlock(
        self, ctx: ZorgFileParser.BlockContext
    ) -> None:  # noqa: D102
        del ctx
        self._s.block = Block()
        section: Section
        if self._s.h4 is not None:
            section = self._s.h4
        elif self._s.h3 is not None:
            section = self._s.h3
        elif self._s.h2 is not None:
            section = self._s.h2
        elif self._s.h1 is None:
            if self.page.h0 is None:
                self.page.h0 = H1("", [])
            section = self.page.h0
        else:
            assert self._s.h1 is not None
            section = self._s.h1
        section.blocks.append(self._s.block)

    def enterContext(
        self, ctx: ZorgFileParser.ContextContext
    ) -> None:  # noqa: D102
        self._add_tag("contexts", ctx.children[1].getText())

    def enterDate(self, ctx: ZorgFileParser.DateContext) -> None:  # noqa: D102
        get_datetime = partial(
            dt.datetime.strptime, ctx.DATE().getText(), "%Y-%m-%d"
        )
        if (
            self._s.in_note
            and self._s.ids_in_note == 1
            and self._s.note_date is None
        ):
            self._s.note_date = get_datetime().date()
        elif self._s.in_h4_header:
            self._s.h4_date = get_datetime().date()
        elif self._s.in_h3_header:
            self._s.h3_date = get_datetime().date()
        elif self._s.in_h2_header:
            self._s.h2_date = get_datetime().date()
        elif self._s.in_h1_header:
            self._s.h1_date = get_datetime().date()
        elif self._s.in_first_comment:
            self._s.file_date = get_datetime().date()

    def enterH1_header(
        self, ctx: ZorgFileParser.H1_headerContext
    ) -> None:  # noqa: D102
        self._s.in_h1_header = True
        self._s.h1 = H1(ctx.space_atoms().getText().strip(), [])
        self.page.h1s.append(self._s.h1)

    def enterH2_header(
        self, ctx: ZorgFileParser.H2_headerContext
    ) -> None:  # noqa: D102
        self._s.in_h2_header = True
        if self._s.h1 is None:
            if self.page.h0 is None:
                self.page.h0 = H1("", [])
            h1 = self.page.h0
        else:
            h1 = self._s.h1
        self._s.h2 = H2(ctx.space_atoms().getText().strip(), [])
        h1.h2s.append(self._s.h2)

    def enterH3_header(
        self, ctx: ZorgFileParser.H3_headerContext
    ) -> None:  # noqa: D102
        self._s.in_h3_header = True
        assert self._s.h2 is not None
        self._s.h3 = H3(ctx.space_atoms().getText().strip(), [])
        self._s.h2.h3s.append(self._s.h3)

    def enterH4_header(
        self, ctx: ZorgFileParser.H4_headerContext
    ) -> None:  # noqa: D102
        self._s.in_h4_header = True
        assert self._s.h3 is not None
        self._s.h4 = H4(ctx.space_atoms().getText().strip(), [])
        self._s.h3.h4s.append(self._s.h4)

    def enterGlobal_link(
        self, ctx: ZorgFileParser.Global_linkContext
    ) -> None:  # noqa: D102
        self._add_tag("links", f"global:{ctx.children[1].getText()}")

    def enterHead(self, ctx: ZorgFileParser.HeadContext) -> None:  # noqa: D102
        del ctx
        self._s.in_head = True

    def enterId(self, ctx: ZorgFileParser.IdContext) -> None:  # noqa: D102
        if self._s.in_note:
            self._s.ids_in_note += 1
            if self._s.ids_in_note == 1 and zdt.is_short_date_spec(
                short_date := ctx.getText()
            ):
                self._s.modify_date = zdt.from_short_date_spec(short_date)
            elif (
                self._s.ids_in_note == 1
                or (self._s.ids_in_note == 2 and self._s.modify_date)
            ) and zdt.is_zid(zid := ctx.getText()):
                self._s.zid = zid
                zorg_id_date = f"20{zid.split('#')[0]}"
                self._s.note_date = dt.datetime.strptime(
                    zorg_id_date, "%Y%m%d"
                ).date()

    def enterInline_prop(
        self, ctx: ZorgFileParser.Inline_propContext
    ) -> None:  # noqa: D102
        words = ctx.getText().split(" ")
        if len(words) == 1:
            key, value = words[0][1:-1].split("::")
        else:
            key = words.pop(0)[1:-2]
            value = " ".join(words)[:-1]
        self._add_prop(key, value)

    def enterItem(self, ctx: ZorgFileParser.ItemContext) -> None:  # noqa: D102
        del ctx
        self._reset_note_context()

    def enterLocal_link(
        self, ctx: ZorgFileParser.Local_linkContext
    ) -> None:  # noqa: D102
        local_id = ctx.children[1].getText()
        # HACK: Ignore completed checklists items.
        if local_id == "X":
            return
        self._add_tag("links", f"local:{local_id}")

    def enterLink(self, ctx: ZorgFileParser.LinkContext) -> None:  # noqa: D102
        self._add_tag("links", ctx.children[1].getText())

    def enterPerson(
        self, ctx: ZorgFileParser.PersonContext
    ) -> None:  # noqa: D102
        self._add_tag("people", ctx.children[1].getText())

    def enterProject(
        self, ctx: ZorgFileParser.ProjectContext
    ) -> None:  # noqa: D102
        self._add_tag("projects", ctx.children[1].getText())

    def enterPriority(
        self, ctx: ZorgFileParser.PriorityContext
    ) -> None:  # noqa: D102
        self._s.todo_priority = ctx.getText().upper()

    def enterQuoted_word(
        self, ctx: ZorgFileParser.Quoted_wordContext
    ) -> None:  # noqa: D102
        del ctx
        self._s.in_quoted_word = True

    def enterRef_link(
        self, ctx: ZorgFileParser.Ref_linkContext
    ) -> None:  # noqa: D102
        self._add_tag("links", f"ref:{ctx.children[1].getText()}")

    def enterSimple_prop(
        self, ctx: ZorgFileParser.Simple_propContext
    ) -> None:  # noqa: D102
        key, value = ctx.id_().getText(), ctx.simple_prop_value().getText()
        self._add_prop(key, value)

    def enterTodo(self, ctx: ZorgFileParser.TodoContext) -> None:  # noqa: D102
        self._s.in_note = True
        del ctx

    def enterTodo_prefix(
        self, ctx: ZorgFileParser.Todo_prefixContext
    ) -> None:  # noqa: D102
        status = NoteType.OPEN_TODO
        if self._s.in_note:
            ch: TodoTypeChar = ctx.getText()[0]
            if ch == "o":
                status = NoteType.OPEN_TODO
            elif ch == "x":
                status = NoteType.CLOSED_TODO
            elif ch == "~":
                status = NoteType.CANCELED_TODO
            elif ch == "<":
                status = NoteType.BLOCKED_TODO
            elif ch == ">":
                status = NoteType.PARENT_TODO
            else:
                assert_never(ch)

            self._s.todo_status = status

    def enterUrl(self, ctx: ZorgFileParser.UrlContext) -> None:  # noqa: D102
        url = ctx.getText()
        self._add_tag("links", f"x:{url}")

    def enterZid_link(
        self, ctx: ZorgFileParser.Zid_linkContext
    ) -> None:  # noqa: D102
        self._add_tag("links", f"zid:{ctx.children[1].getText()}")

    def exitBase_todo(
        self, ctx: ZorgFileParser.Base_todoContext
    ) -> None:  # noqa: D102
        extra_kwargs: dict[str, Any] = {
            "todo_payload": TodoPayload(
                priority=self._s.todo_priority, status=self._s.todo_status
            ),
        }
        self._add_note(
            ctx.note_body(),
            **extra_kwargs,
        )
        self._s.in_note = False

        # Reset todo priority and status back to defaults.
        self._s.todo_priority = _DEFAULT_PRIORITY
        self._s.todo_status = NoteType.OPEN_TODO

    def exitH1_header(
        self, ctx: ZorgFileParser.H1_headerContext
    ) -> None:  # noqa: D102
        del ctx
        self._s.in_h1_header = False

    def exitH1_section(
        self, ctx: ZorgFileParser.H1_headerContext
    ) -> None:  # noqa: D102
        del ctx
        self._s.h1 = None
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
        self._s.h2 = None
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
        self._s.h3 = None
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
        self._s.h4 = None
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
        self._add_note(ctx.note_body())
        self._s.in_note = False

    def exitQuoted_word(
        self, ctx: ZorgFileParser.Quoted_wordContext
    ) -> None:  # noqa: D102
        del ctx
        self._s.in_quoted_word = False

    def _get_note_kwargs(
        self,
        line_no: int,
        **extra_kwargs: Mapping[str, Any],
    ) -> dict[str, Any]:
        kwargs: dict[str, Any] = {
            "areas": self._s.areas,
            "contexts": self._s.contexts,
            "create_date": self._s.create_date,
            "line_no": line_no,
            "links": self._s.links,
            "modify_date": (
                self._s.modify_date
                if self._s.modify_date
                else self._s.create_date
            ),
            "people": self._s.people,
            "projects": self._s.projects,
            "properties": self._s.properties,
            "zid": self._s.zid,
        }
        return kwargs | extra_kwargs

    def _reset_note_context(self) -> None:
        self._s.zid = None
        self._s.ids_in_note = 0
        self._s.note_tags = _get_default_tags_map()
        self._s.note_props = {}
        self._s.note_date = None
        self._s.modify_date = None

    def _add_prop(self, key: str, value: str) -> None:
        if self._s.in_quoted_word:
            _LOGGER.debug("Skipping quoted property", key=key, value=value)
            return

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

    def _add_tag(self, tag_name: TagName, tag_value: str) -> None:
        if all(ch.isdigit() for ch in tag_value):
            _LOGGER.debug(
                "Tag identifiers cannot contain only digits.",
                tag_name=tag_name,
                ID=tag_value,
            )
            return
        if self._s.in_first_comment:
            self._s.file_tags[tag_name].append(tag_value)
        elif self._s.in_h1_header:
            self._s.h1_tags[tag_name].append(tag_value)
        elif self._s.in_h2_header:
            self._s.h2_tags[tag_name].append(tag_value)
        elif self._s.in_h3_header:
            self._s.h3_tags[tag_name].append(tag_value)
        elif self._s.in_h4_header:
            self._s.h4_tags[tag_name].append(tag_value)
        elif self._s.in_note:
            self._s.note_tags[tag_name].append(tag_value)

    def _add_note(
        self,
        note_body: Optional[ZorgFileParser.Note_bodyContext],
        **extra_kwargs: Mapping[str, Any],
    ) -> None:
        if note_body is None:
            _LOGGER.warning("Skipping todo with no note body")
        elif note_body.getText().strip() == "":
            _LOGGER.warning("Skipping todo with empty note body")
        elif self.error_manager.errors:
            _LOGGER.warning(
                "Skipping note since zorg file has errors.",
                file_path=str(self.page.path),
            )
            self.page.has_errors = True
        else:
            body = note_body.getText().strip()
            bullets = (
                body.split(" * ")
                if any(val in body for val in [":: ", "::\n"])
                else []
            )
            for bullet in bullets:
                words = bullet.split()
                if zdt.is_short_date_spec(words[0]):
                    words.pop(0)
                if zdt.is_zid(words[0]):
                    words.pop(0)
                first_word = words.pop(0)
                if first_word.endswith("::"):
                    key = first_word[:-2]
                    value = re.sub(r"\s+", " ", " ".join(words).strip())
                    self._add_prop(key, value)
            kwargs = self._get_note_kwargs(
                note_body.start.line, **extra_kwargs
            )
            assert self._s.block is not None
            note = Note(body, file_path=self.page.path, **kwargs)
            self._s.block.notes.append(note)


def _get_default_tags_map() -> _TagDict:
    return {
        "areas": [],
        "contexts": [],
        "links": [],
        "people": [],
        "projects": [],
    }


@dataclass
class _ZorgFileCompilerState:
    """Serves as a data store while parsing zorg files."""

    zid: Optional[str] = None

    ids_in_note: int = 0

    block: Optional[Block] = None
    h1: Optional[H1] = None
    h2: Optional[H2] = None
    h3: Optional[H3] = None
    h4: Optional[H4] = None

    in_first_comment: bool = True
    in_h1_header: bool = False
    in_h2_header: bool = False
    in_h3_header: bool = False
    in_h4_header: bool = False
    in_head: bool = False
    in_note: bool = False
    in_quoted_word: bool = False

    file_tags: _TagDict = field(default_factory=_get_default_tags_map)
    h1_tags: _TagDict = field(default_factory=_get_default_tags_map)
    h2_tags: _TagDict = field(default_factory=_get_default_tags_map)
    h3_tags: _TagDict = field(default_factory=_get_default_tags_map)
    h4_tags: _TagDict = field(default_factory=_get_default_tags_map)
    note_tags: _TagDict = field(default_factory=_get_default_tags_map)

    file_props: dict[str, Any] = field(default_factory=lambda: {})
    h1_props: dict[str, Any] = field(default_factory=lambda: {})
    h2_props: dict[str, Any] = field(default_factory=lambda: {})
    h3_props: dict[str, Any] = field(default_factory=lambda: {})
    h4_props: dict[str, Any] = field(default_factory=lambda: {})
    note_props: dict[str, Any] = field(default_factory=lambda: {})

    file_date: Optional[dt.date] = None
    h1_date: Optional[dt.date] = None
    h2_date: Optional[dt.date] = None
    h3_date: Optional[dt.date] = None
    h4_date: Optional[dt.date] = None
    note_date: Optional[dt.date] = None
    modify_date: Optional[dt.date] = None

    todo_priority: TodoPriorityType = _DEFAULT_PRIORITY
    todo_status: NoteType = NoteType.OPEN_TODO

    @property
    def areas(self) -> list[str]:
        """Area tags that are currently in-scope."""
        return self._get_current_tags("areas")

    @property
    def contexts(self) -> list[str]:
        """Context tags that are currently in-scope."""
        return self._get_current_tags("contexts")

    @property
    def links(self) -> list[str]:
        """Links that are currently in-scope."""
        return self._get_current_tags("links")

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
