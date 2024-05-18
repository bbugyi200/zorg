"""Contains service logic used to compile zorg queries."""

import datetime as dt
from typing import Optional, cast

from logrus import Logger

from .. import dates as zdt
from ...domain.models import (
    DateRange,
    DescFilter,
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
            # TODO(bugyi): De-duplicate create range and modify range parsing.
            elif x := where_atom.create_range():
                create_range = cast(ZorgQueryParser.Create_rangeContext, x)
                short_start_date = create_range.CREATE_RANGE_HEAD().getText()[
                    1:
                ]
                start_date = zdt.from_short_date(short_start_date)

                end_date: Optional[dt.date] = None
                if date_range_tail := create_range.DATE_RANGE_TAIL():
                    short_end_date = date_range_tail.getText()[1:]
                    end_date = zdt.from_short_date(short_end_date)

                date_range = DateRange(start_date, end_date)
                create_date_ranges.add(date_range)
            elif x := where_atom.modify_range():
                modify_range = cast(ZorgQueryParser.Modify_rangeContext, x)
                short_start_date = modify_range.MODIFY_RANGE_HEAD().getText()[
                    1:
                ]
                start_date = zdt.from_short_date(short_start_date)

                end_date = None
                if date_range_tail := modify_range.DATE_RANGE_TAIL():
                    short_end_date = date_range_tail.getText()[1:]
                    end_date = zdt.from_short_date(short_end_date)

                date_range = DateRange(start_date, end_date)
                modify_date_ranges.add(date_range)
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
            elif where_atom.prop_filter():
                key, op_value = where_atom.prop_filter().getText().split(":")
                negated = False
                if key[0] == "!":
                    negated = True
                    key = key[1:]
                op, value = _split_op_value(op_value)
                value_type = _get_value_type(value)
                property_filter = PropertyFilter(
                    key, value, op=op, value_type=value_type, negated=negated
                )
                property_filters.add(property_filter)
            elif where_atom.desc_filter():
                desc_filter = where_atom.desc_filter().getText()
                desc_op = DescOperator.CONTAINS
                case_sensitive: Optional[bool] = None
                if desc_filter[0] == "!":
                    desc_op = DescOperator.NOT_CONTAINS
                    desc_filter = desc_filter[1:]
                if desc_filter[0] == "c":
                    desc_filter = desc_filter[1:]
                    case_sensitive = True
                value = desc_filter[1:-1]
                desc_filters.add(
                    DescFilter(
                        value=value, op=desc_op, case_sensitive=case_sensitive
                    )
                )

        self._and_filter_groups[-1].append(
            WhereAndFilter(
                allowed_note_types=allowed_note_types,
                areas=areas,
                contexts=contexts,
                create_date_ranges=create_date_ranges,
                desc_filters=desc_filters,
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
                raise RuntimeError(
                    f"Invalid GROUP BY atom: {group_by_atom.getText()}"
                )

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
                group_by_type = OrderByType.CREATE_DATE
            elif order_by_atom.modify():
                group_by_type = OrderByType.MODIFY_DATE
            elif order_by_atom.priority():
                group_by_type = OrderByType.PRIORITY
            elif order_by_atom.type_():
                group_by_type = OrderByType.NOTE_TYPE
            else:
                raise RuntimeError(
                    f"Invalid GROUP BY atom: {order_by_atom.getText()}"
                )

            order_by_types.append(group_by_type)
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
    if zdt.is_date(value):
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
