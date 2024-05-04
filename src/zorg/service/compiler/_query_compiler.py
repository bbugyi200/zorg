"""Contains service logic used to compile zorg queries."""

from typing import cast

from logrus import Logger

from ...domain.models import Query, WhereAndFilter, WhereOrFilter
from ...domain.types import NoteType, SelectType, TodoPriorityType
from ...grammar.zorg_query.ZorgQueryListener import ZorgQueryListener
from ...grammar.zorg_query.ZorgQueryParser import ZorgQueryParser


_LOGGER = Logger(__name__)


class ZorgQueryCompiler(ZorgQueryListener):
    """Listener that compiles zorg queries."""

    def __init__(self, zorg_query: Query) -> None:
        self.zorg_query = zorg_query

        self._and_filter_groups: list[list[WhereAndFilter]] = []

    def enterSelect(
        self, ctx: ZorgQueryParser.SelectContext
    ) -> None:  # noqa: D102
        select_body = cast(
            ZorgQueryParser.Select_bodyContext, ctx.select_body()
        )
        select: SelectType
        if select_body.AT_SIGN():
            select = SelectType.CONTEXTS
        elif select_body.HASH():
            select = SelectType.AREAS
        elif select_body.PERCENT():
            select = SelectType.PEOPLE
        elif select_body.PLUS():
            select = SelectType.PROJECTS
        elif select_body.getText() == "file":
            select = SelectType.FILES
        elif select_body.getText() == "note":
            select = SelectType.NOTES
        else:
            emsg = "Unrecognized select body"
            _LOGGER.error(emsg, select_body=select_body.getText())
            raise RuntimeError(emsg)

        self.zorg_query.select = select

    def enterAnd_filter(
        self, ctx: ZorgQueryParser.And_filterContext
    ) -> None:  # noqa: D102
        allowed_note_types: set[NoteType] = set()
        areas: set[str] = set()
        contexts: set[str] = set()
        people: set[str] = set()
        priorities: set[TodoPriorityType] = set()
        projects: set[str] = set()

        where_atoms = cast(
            list[ZorgQueryParser.Where_atomContext], ctx.where_atom()
        )
        for where_atom in where_atoms:
            if where_atom.note_type():
                note_type = cast(
                    ZorgQueryParser.Note_typeContext,
                    where_atom.note_type(),
                )
                note_type_chars = cast(
                    list[ZorgQueryParser.Note_type_charContext],
                    note_type.note_type_char(),
                )
                _add_note_types(note_type_chars, allowed_note_types)
            elif where_atom.priority_range():
                priority_range = cast(
                    ZorgQueryParser.Priority_rangeContext,
                    where_atom.priority_range(),
                )
                _add_priorities(priority_range, priorities)
            elif where_atom.tag():
                tag = cast(ZorgQueryParser.TagContext, where_atom.tag())
                minus = "-" if tag.not_op() else ""
                if tag.area():
                    tag_set = areas
                    tag_id = tag.area().ID()
                elif tag.context():
                    tag_set = contexts
                    tag_id = tag.context().ID()
                elif tag.person():
                    tag_set = people
                    tag_id = tag.person().ID()
                elif tag.project():
                    tag_set = projects
                    tag_id = tag.project().ID()
                else:
                    raise RuntimeError(f"Invalid Tag: {tag.getText()}")

                tag_set.add(f"{minus}{tag_id.getText()}")

        self._and_filter_groups[-1].append(
            WhereAndFilter(
                allowed_note_types=allowed_note_types,
                areas=areas,
                contexts=contexts,
                people=people,
                priorities=priorities,
                projects=projects,
            )
        )

    def enterSubfilter(
        self, ctx: ZorgQueryParser.SubfilterContext
    ) -> None:  # noqa: D102
        del ctx
        self._and_filter_groups.append([])

    def enterWhere(
        self, ctx: ZorgQueryParser.WhereContext
    ) -> None:  # noqa: D102
        del ctx
        self._and_filter_groups.append([])

    def exitSubfilter(
        self, ctx: ZorgQueryParser.SubfilterContext
    ) -> None:  # noqa: D102
        del ctx
        and_filters = self._and_filter_groups.pop()
        self._and_filter_groups[-1][-1].or_filters.append(
            WhereOrFilter(and_filters)
        )

    def exitWhere(
        self, ctx: ZorgQueryParser.WhereContext
    ) -> None:  # noqa: D102
        del ctx
        where = WhereOrFilter(self._and_filter_groups[-1])
        self.zorg_query.where = where


def _add_note_types(
    note_type_chars: list[ZorgQueryParser.Note_type_charContext],
    allowed_note_types: set[NoteType],
) -> None:
    for note_type_char in note_type_chars:
        if note_type_char.DASH():
            allowed_note_types.add(NoteType.BASIC)
        elif note_type_char.LOWER_O():
            allowed_note_types.add(NoteType.OPEN_TODO)
        elif note_type_char.LOWER_X():
            allowed_note_types.add(NoteType.CLOSED_TODO)
        elif note_type_char.TILDE():
            allowed_note_types.add(NoteType.CANCELED_TODO)
        elif note_type_char.LANGLE():
            allowed_note_types.add(NoteType.BLOCKED_TODO)
        elif note_type_char.RANGLE():
            allowed_note_types.add(NoteType.PARENT_TODO)
        else:
            emsg = "Unrecognized note status character"
            _LOGGER.error(emsg, note_type_char=note_type_char.getText())
            raise RuntimeError(emsg)


def _add_priorities(
    priority_range: ZorgQueryParser.Priority_rangeContext,
    priorities: set[TodoPriorityType],
) -> None:
    for ID in priority_range.ID():
        pletter: str = ID.getText().upper()
        assert (
            len(pletter) == 1 and pletter.isalpha()
        ), f"Invalid priority: {pletter}"
        priorities.add(cast(TodoPriorityType, pletter))
