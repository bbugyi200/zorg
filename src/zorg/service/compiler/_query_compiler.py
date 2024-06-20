"""Contains service logic used to compile zorg queries."""

import datetime as dt
from typing import Optional, Union, cast

from logrus import Logger

from .. import dates as zdt
from ...domain.models import (
    DateRange,
    DescFilter,
    FileFilter,
    LinkFilter,
    PropertyFilter,
    Query,
    WhereAndFilter,
    WhereOrFilter,
)
from ...domain.types import (
    DescOperator,
    GroupByType,
    NoteType,
    OrderByType,
    PropertyOperator,
    PropertyValueType,
    SelectType,
    TodoPriorityType,
)
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
        if select_body.HASH():
            select = SelectType.AREA
        elif select_body.AT_SIGN():
            select = SelectType.CONTEXT
        elif select_body.PERCENT():
            select = SelectType.PERSON
        elif select_body.PLUS():
            select = SelectType.PROJECT
        elif select_body.file_():
            select = SelectType.FILE
        elif select_body.note():
            select = SelectType.NOTE
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
        create_date_ranges: set[DateRange] = set()
        modify_date_ranges: set[DateRange] = set()
        people: set[str] = set()
        priorities: set[TodoPriorityType] = set()
        projects: set[str] = set()
        property_filters: set[PropertyFilter] = set()
        desc_filters: set[DescFilter] = set()
        file_filters: set[FileFilter] = set()
        link_filters: set[LinkFilter] = set()

        where_atoms = cast(
            list[ZorgQueryParser.Where_atomContext], ctx.where_atom()
        )
        for where_atom in where_atoms:
            if w := where_atom.note_type():
                note_type = cast(ZorgQueryParser.Note_typeContext, w)
                note_type_chars = cast(
                    list[ZorgQueryParser.Note_type_charContext],
                    note_type.note_type_char(),
                )
                _add_note_types(note_type_chars, allowed_note_types)
            elif w := where_atom.priority_range():
                priority_range = cast(ZorgQueryParser.Priority_rangeContext, w)
                _add_priorities(priority_range, priorities)
            elif w := where_atom.create_range():
                create_range = cast(ZorgQueryParser.Create_rangeContext, w)
                short_start_date = create_range.CREATE_RANGE_HEAD().getText()[
                    1:
                ]
                create_date_ranges.add(
                    _get_date_range(create_range, short_start_date)
                )
            elif w := where_atom.modify_range():
                modify_range = cast(ZorgQueryParser.Modify_rangeContext, w)
                short_start_date = modify_range.MODIFY_RANGE_HEAD().getText()[
                    1:
                ]
                modify_date_ranges.add(
                    _get_date_range(modify_range, short_start_date)
                )
            elif w := where_atom.tag():
                tag = cast(ZorgQueryParser.TagContext, w)
                minus = "-" if tag.not_op() else ""
                if tag.area():
                    tag_set = areas
                    tag_id = tag.area()
                elif tag.context():
                    tag_set = contexts
                    tag_id = tag.context()
                elif tag.person():
                    tag_set = people
                    tag_id = tag.person()
                elif tag.project():
                    tag_set = projects
                    tag_id = tag.project()
                else:
                    raise RuntimeError(f"Invalid Tag: {tag.getText()}")

                tag_set.add(f"{minus}{tag_id.getText()[1:]}")
            elif w := where_atom.prop_filter():
                property_filters.add(_get_property_filter(w))
            elif w := where_atom.desc_filter():
                desc_filters.add(_get_desc_filter(w))
            elif w := where_atom.file_filter():
                if w.getText().startswith("!"):
                    negated = True
                    path_glob = w.getText()[3:]
                else:
                    negated = False
                    path_glob = w.getText()[2:]
                path_glob = (
                    path_glob if path_glob.endswith("*") else f"{path_glob}.zo"
                )
                file_filters.add(FileFilter(path_glob, negated=negated))
            elif w := where_atom.link_filter():
                if w.getText().startswith("!"):
                    negated = True
                    link = w.getText()[3:-2]
                else:
                    negated = False
                    link = w.getText()[2:-2]
                link_filters.add(LinkFilter(link, negated=negated))
            # Subfilters are handled in a different method. See the
            # enterSubfilter() and exitSubfilter() methods for more
            # information.
            elif not where_atom.subfilter():
                _LOGGER.warning(
                    f"Unrecognized where atom: {where_atom.getText()}"
                )

        self._and_filter_groups[-1].append(
            WhereAndFilter(
                allowed_note_types=allowed_note_types,
                areas=areas,
                contexts=contexts,
                create_date_ranges=create_date_ranges,
                desc_filters=desc_filters,
                file_filters=file_filters,
                link_filters=link_filters,
                modify_date_ranges=modify_date_ranges,
                people=people,
                priorities=priorities,
                projects=projects,
                property_filters=property_filters,
            )
        )

    def enterGroup_by_body(
        self, ctx: ZorgQueryParser.Group_by_bodyContext
    ) -> None:  # noqa: D102
        group_by_types = []
        for group_by_atom in cast(
            list[ZorgQueryParser.Group_by_atomContext], ctx.group_by_atom()
        ):
            group_by_type: Optional[GroupByType] = None
            if group_by_atom.AT_SIGN():
                group_by_type = GroupByType.CONTEXT
            elif group_by_atom.HASH():
                group_by_type = GroupByType.AREA
            elif group_by_atom.PERCENT():
                group_by_type = GroupByType.PERSON
            elif group_by_atom.PLUS():
                group_by_type = GroupByType.PROJECT
            elif group_by_atom.file_():
                group_by_type = GroupByType.FILE
            elif group_by_atom.type_():
                group_by_type = GroupByType.NOTE_TYPE
            elif group_by_atom.priority():
                group_by_type = GroupByType.PRIORITY
            else:
                assert (
                    group_by_atom.getText() == "none"
                ), f"Invalid GROUP BY atom: {group_by_atom.getText()}"

            if group_by_type is not None:
                group_by_types.append(group_by_type)
        self.zorg_query.group_by = tuple(group_by_types)

    def enterOrder_by_body(
        self, ctx: ZorgQueryParser.Order_by_bodyContext
    ) -> None:  # noqa: D102
        order_by_types = []
        for order_by_atom in cast(
            list[ZorgQueryParser.Order_by_atomContext], ctx.order_by_atom()
        ):
            if order_by_atom.create():
                order_by_type = OrderByType.CREATE_DATE
            elif order_by_atom.modify():
                order_by_type = OrderByType.MODIFY_DATE
            elif order_by_atom.priority():
                order_by_type = OrderByType.PRIORITY
            elif order_by_atom.type_():
                order_by_type = OrderByType.NOTE_TYPE
            else:
                raise RuntimeError(
                    f"Invalid GROUP BY atom: {order_by_atom.getText()}"
                )

            order_by_types.append(order_by_type)
        self.zorg_query.order_by = tuple(order_by_types)

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


def _get_date_range(
    range_ctx: Union[
        ZorgQueryParser.Create_rangeContext,
        ZorgQueryParser.Modify_rangeContext,
    ],
    date_spec: str,
) -> DateRange:
    start_date = zdt.from_date_spec(date_spec)

    end_date: Optional[dt.date] = None
    if date_range_tail := range_ctx.DATE_RANGE_TAIL():
        short_end_date = date_range_tail.getText()[1:]
        end_date = zdt.from_date_spec(short_end_date)

    return DateRange(start_date, end_date)


def _get_desc_filter(w: ZorgQueryParser.Desc_filterContext) -> DescFilter:
    desc_filter = w.getText()
    desc_op = DescOperator.CONTAINS
    case_sensitive: Optional[bool] = None
    if desc_filter[0] == "!":
        desc_op = DescOperator.NOT_CONTAINS
        desc_filter = desc_filter[1:]
    if desc_filter[0] == "c":
        desc_filter = desc_filter[1:]
        case_sensitive = True
    value = desc_filter[1:-1]
    return DescFilter(value=value, op=desc_op, case_sensitive=case_sensitive)


def _get_property_filter(
    w: ZorgQueryParser.Prop_filterContext,
) -> PropertyFilter:
    key, op_value = w.getText().split(":")
    negated = False
    if key[0] == "!":
        negated = True
        key = key[1:]
    op, value = _split_op_value(op_value)
    value_type = _get_value_type(value)
    return PropertyFilter(
        key, value, op=op, value_type=value_type, negated=negated
    )


def _split_op_value(op_value: str) -> tuple[PropertyOperator, str]:
    if op_value[0] == "<":
        op_value = op_value[1:]
        if op_value[0] == "=":
            return (PropertyOperator.LE, op_value[1:])
        return (PropertyOperator.LT, op_value)
    elif op_value[0] == ">":
        op_value = op_value[1:]
        if op_value[0] == "=":
            return (PropertyOperator.GE, op_value[1:])
        return (PropertyOperator.GT, op_value)
    elif op_value[0] == "*" and len(op_value) == 1:
        return (PropertyOperator.EXISTS, "")
    else:
        return (PropertyOperator.EQ, op_value)


def _get_value_type(value: str) -> PropertyValueType:
    if zdt.is_date_spec(value):
        return PropertyValueType.DATE
    elif all(ch.isdigit() for ch in value):
        return PropertyValueType.INTEGER

    return PropertyValueType.STRING


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
    p_start_and_end = list(priority_range.getText().split("-"))
    p_start_idx = int(p_start_and_end.pop(0)[-1])
    p_end_idx = p_start_idx + 1
    if p_start_and_end:
        p_end_idx = int(p_start_and_end.pop(0)) + 1
    for priority in [f"P{n}" for n in range(p_start_idx, p_end_idx)]:
        priorities.add(cast(TodoPriorityType, priority))
