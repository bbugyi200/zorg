"""Contains logic to convert domain Query model to SQL select statement."""

from dataclasses import dataclass
from functools import partial
import operator
from typing import Any, Callable, Final, Iterable, Optional, TypeVar, cast

from logrus import Logger
import metaman
from sqlalchemy import func
from sqlmodel import Integer, Session, and_, or_, select
from sqlmodel.sql.expression import Column, ColumnElement, SelectOfScalar

from zorg.domain.models import WhereAndFilter, WhereOrFilter
from zorg.domain.types import (
    DescOperator,
    NoteType,
    PropertyOperator,
    PropertyValueType,
)
from zorg.shared import dates as zdt

from . import _models as sql


_BASE_SELECTOR: Final = (
    select(sql.Note)
    .join(sql.Page, cast(ColumnElement, sql.Page.path == sql.Note.page_path))
    .distinct()
)
_LOGGER: Final = Logger(__name__)

_ToSqlWhereHelper = Callable[["_AndFilterToSqlWhere"], Optional[ColumnElement]]
# The @_to_sql_where_helper decorator should be used to mark a
# _AndFilterToSqlWhere parser method.
_TO_SQL_WHERE_HELPERS: list[_ToSqlWhereHelper] = []
_to_sql_where_helper = metaman.register_function_factory(_TO_SQL_WHERE_HELPERS)

_T = TypeVar("_T")


def to_sql_select(
    or_filter: Optional[WhereOrFilter], session: Session
) -> SelectOfScalar[sql.Note]:
    """Converts a WhereOrFilter to a SQL SELECT that will fetch ZorgNotes."""
    if or_filter is None or not or_filter.and_filters:
        return select(sql.Note)

    select_query = _BASE_SELECTOR.where(
        or_(*[
            _AndFilterToSqlWhere(and_filter, session).to_sql_where()
            for and_filter in or_filter.and_filters
        ])
    ).order_by(cast(Column, sql.Note.zid))
    _LOGGER.debug("Converted query", query=str(select_query))
    return select_query


@dataclass(frozen=True)
class _AndFilterToSqlWhere:
    """Converts a WhereAndFilter to a SQL WHERE filter."""

    and_filter: WhereAndFilter
    session: Session

    def to_sql_where(self) -> ColumnElement:
        """Constructs a SQL statement from the provided WhereAndFilter."""
        and_clauses = []
        for parse in _TO_SQL_WHERE_HELPERS:
            clause = parse(self)
            if clause is not None:
                and_clauses.append(clause)

        where = (
            and_(and_clauses[0], *and_clauses[1:])
            if len(and_clauses) > 1
            else and_clauses[0]
        )
        return where

    @_to_sql_where_helper
    def note_type(self) -> Optional[ColumnElement]:
        """Converter for done status (e.g. '-' or 'ox~<>')."""
        if not self.and_filter.allowed_note_types:
            return None

        return or_(*[
            sql.Note.todo_status == _to_todo_status(note_type)
            for note_type in self.and_filter.allowed_note_types
        ])

    @_to_sql_where_helper
    def priority_range(self) -> Optional[ColumnElement]:
        """Converter for priority range filters."""
        priorities = self.and_filter.priorities
        if priorities:
            return or_(*[
                sql.Note.todo_priority == priority for priority in priorities
            ])
        else:
            return None

    @_to_sql_where_helper
    def tags(self) -> Optional[ColumnElement]:
        """Parser for prefix tags (e.g. '@home' or '+zorg')."""
        conditions = []
        for prefix_tag_list, link_model, model in [
            (self.and_filter.areas, sql.AreaLink, sql.Area),
            (self.and_filter.contexts, sql.ContextLink, sql.Context),
            (self.and_filter.people, sql.PersonLink, sql.Person),
            (self.and_filter.projects, sql.ProjectLink, sql.Project),
        ]:
            base_subquery = select(sql.Note.id).join(link_model).join(model)
            for prefix_tag in prefix_tag_list:
                name = prefix_tag

                if name.startswith("-"):
                    # remove '-' from name
                    name = name[1:]
                    in_op = sql.Note.id.not_in  # type: ignore[union-attr]
                else:
                    in_op = sql.Note.id.in_  # type: ignore[union-attr]

                subquery = base_subquery.where(model.name == name)
                conditions.append(in_op(subquery))
        if conditions:
            return (
                and_(conditions[0], *conditions[1:])
                if len(conditions) > 1
                else conditions[0]
            )
        else:
            return None

    @_to_sql_where_helper
    def or_filters(self) -> Optional[ColumnElement]:
        """Converter that handles nested OR filters."""
        or_filters = self.and_filter.or_filters
        if not or_filters:
            return None

        or_conds = []
        for or_filter in or_filters:
            or_conds.append(
                or_(*[
                    _AndFilterToSqlWhere(
                        and_filter, self.session
                    ).to_sql_where()
                    for and_filter in or_filter.and_filters
                ])
            )
        return (
            and_(or_conds[0], *or_conds[1:])
            if len(or_conds) > 1
            else or_conds[0]
        )

    @_to_sql_where_helper
    def date_ranges(self) -> Optional[ColumnElement]:
        """Converter that handles create/modify date ranges."""
        and_conds = []
        for date_range_list, sql_date in [
            (self.and_filter.create_date_ranges, sql.Note.create_date),
            (self.and_filter.modify_date_ranges, sql.Note.modify_date),
        ]:
            for date_range in date_range_list:
                date_filters = [sql_date >= date_range.start]
                end_date = (
                    date_range.end if date_range.end else date_range.start
                )
                date_filters.append(sql_date <= end_date)
                and_conds.append(and_(*date_filters))

        if and_conds:
            return and_(and_conds[0], *and_conds[1:])
        else:
            return None

    @_to_sql_where_helper
    def property_filters(self) -> Optional[ColumnElement]:
        """Converter tht handles property filters."""
        if not self.and_filter.property_filters:
            return None
        and_conds = []
        for property_filter in self.and_filter.property_filters:
            negated = property_filter.negated
            comp_op_map = {
                PropertyOperator.EQ: operator.ne if negated else operator.eq,
                PropertyOperator.LT: operator.ge if negated else operator.lt,
                PropertyOperator.GT: operator.le if negated else operator.gt,
                PropertyOperator.LE: operator.gt if negated else operator.le,
                PropertyOperator.GE: operator.lt if negated else operator.ge,
            }
            subquery = (
                select(sql.Note.id)
                .join(sql.PropertyLink)
                .join(sql.Property)
                .where(sql.Property.name == property_filter.key)
            )

            op = sql.Note.id.in_  # type: ignore[union-attr]
            if property_filter.op == PropertyOperator.EXISTS and negated:
                op = sql.Note.id.not_in  # type: ignore[union-attr]
            elif property_filter.op != PropertyOperator.EXISTS:
                comp_op = comp_op_map[property_filter.op]

                value_type_map: dict[
                    PropertyValueType,
                    tuple[Callable[[Any], Any], Callable[[Any], Any]],
                ] = {
                    PropertyValueType.DATE: (func.date, zdt.from_date_spec),
                    PropertyValueType.INTEGER: (_col_to_int, int),
                    PropertyValueType.STRING: (_noop, _noop),
                }
                cast_model, cast_value = value_type_map[
                    property_filter.value_type
                ]
                subquery = subquery.where(
                    comp_op(
                        cast_model(sql.PropertyLink.value),
                        cast_value(property_filter.value),
                    )
                )

            and_conds.append(op(subquery))

        return and_(and_conds[0], *and_conds[1:])

    @_to_sql_where_helper
    def desc_filters(self) -> Optional[ColumnElement]:
        """Converter tht handles desc filters."""
        and_conds = []
        if not self.and_filter.desc_filters:
            return None

        for desc_filter in self.and_filter.desc_filters:
            case_sensitive = desc_filter.case_sensitive
            if case_sensitive is None:
                case_sensitive = not bool(desc_filter.value.islower())

            like_arg = f"%{desc_filter.value}%".replace("_", "\\_")
            op_arg: Any
            if case_sensitive:
                cond = sql.Note.body.like(like_arg)  # type: ignore[attr-defined]
                subquery = select(sql.Note.id, sql.Note.body).where(cond)
                id_list: list[int] = []
                for ID, body in self.session.exec(subquery).all():
                    assert (
                        ID is not None
                    ), "The DB shouldn't contain notes without an ID, right?"
                    if desc_filter.value in body:
                        id_list.append(ID)

                op_map: dict[DescOperator, Any] = {
                    DescOperator.CONTAINS: sql.Note.id.in_,  # type: ignore[union-attr]
                    DescOperator.NOT_CONTAINS: sql.Note.id.not_in,  # type: ignore[union-attr]
                }
                op = op_map[desc_filter.op]
                op_arg = id_list
            else:
                op_map = {
                    DescOperator.CONTAINS: sql.Note.body.ilike,  # type: ignore[attr-defined]
                    DescOperator.NOT_CONTAINS: sql.Note.body.not_ilike,  # type: ignore[attr-defined]
                }
                op = partial(op_map[desc_filter.op], escape="\\")
                op_arg = like_arg

            and_conds.append(op(op_arg))
        return and_(and_conds[0], *and_conds[1:])

    @_to_sql_where_helper
    def file_filters(self) -> Optional[ColumnElement]:
        """Converter tht handles file filters."""
        and_conds = []
        if not self.and_filter.file_filters:
            return None
        for file_filter in self.and_filter.file_filters:
            like_op = (
                sql.Page.path.not_like  # type: ignore[attr-defined]
                if file_filter.negated
                else sql.Page.path.like  # type: ignore[attr-defined]
            )
            and_conds.append(like_op(file_filter.path_glob.replace("*", "%")))
        return and_(and_conds[0], *and_conds[1:])

    @_to_sql_where_helper
    def link_filters(self) -> Optional[ColumnElement]:
        """Converter tht handles link filters."""
        and_conds = []
        if not self.and_filter.link_filters:
            return None
        base_subquery = select(sql.Note.id).join(sql.LinkLink).join(sql.Link)
        for link_filter in self.and_filter.link_filters:
            if link_filter.negated:
                in_op = sql.Note.id.not_in  # type: ignore[union-attr]
                like_op = sql.Link.name.not_like  # type: ignore[attr-defined]
            else:
                in_op = sql.Note.id.in_  # type: ignore[union-attr]
                like_op = sql.Link.name.like  # type: ignore[attr-defined]

            link_name = link_filter.link
            notes_in_file = _get_notes_in_file(self.session, link_name)
            subquery = base_subquery.where(
                or_(
                    sql.Link.name == link_name,
                    like_op(f"{link_name}#%"),
                    *_global_link_conds(notes_in_file),
                    *_ref_link_conds(notes_in_file),
                    *_zid_link_conds(notes_in_file),
                )
            )
            and_conds.append(in_op(subquery))
        return and_(and_conds[0], *and_conds[1:])


def _get_notes_in_file(session: Session, file_name: str) -> list[sql.Note]:
    stmt = _BASE_SELECTOR.where(sql.Page.path == f"{file_name}.zo")
    return list(session.exec(stmt).all())


def _global_link_conds(notes: Iterable[sql.Note]) -> list[ColumnElement]:
    conds = []
    for note in notes:
        for prop_link in note.property_links:
            if prop_link.prop.name == "ID":
                conds.append(
                    cast(
                        ColumnElement,
                        sql.Link.name == f"global:{prop_link.value}",
                    )
                )
    return conds


def _ref_link_conds(notes: Iterable[sql.Note]) -> list[ColumnElement]:
    conds = []
    for note in notes:
        for prop_link in note.property_links:
            if prop_link.prop.name == "RID":
                conds.append(
                    cast(
                        ColumnElement,
                        sql.Link.name == f"ref:{prop_link.value}",
                    )
                )
    return conds


def _zid_link_conds(notes: Iterable[sql.Note]) -> list[ColumnElement]:
    conds = []
    for note in notes:
        conds.append(cast(ColumnElement, sql.Link.name == f"zid:{note.zid}"))
    return conds


def _noop(value: _T) -> _T:
    """A function that does nothing."""
    return value


def _col_to_int(value: Any) -> Any:
    """Casts SQL table's column to integer."""
    return func.cast(value, Integer)  # pylint: disable=not-callable


def _to_todo_status(note_type: NoteType) -> Optional[NoteType]:
    if note_type is NoteType.BASIC:
        return None
    else:
        return note_type
