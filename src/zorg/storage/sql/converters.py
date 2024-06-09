"""Contains logic to convert domain models to/from SQL models."""

from collections import defaultdict
from dataclasses import dataclass
from functools import partial
import operator
from pathlib import Path
from typing import Any, Callable, Iterable, Optional, TypeVar, cast

import metaman
from sqlalchemy import func
from sqlmodel import Integer, Session, and_, or_, select
from sqlmodel.sql.expression import Column, ColumnElement, SelectOfScalar

from . import models as sql
from ...domain.models import (
    File,
    Note,
    TodoPayload,
    WhereAndFilter,
    WhereOrFilter,
)
from ...domain.types import (
    DescOperator,
    EntityConverter,
    NoteType,
    PropertyOperator,
    PropertyValueType,
    TodoPriorityType,
)
from ...service import common, dates as zdt


_SONConverterParser = Callable[["_SONConverter"], Optional[ColumnElement]]
# the @_son_converter_parser decorator should be used to mark a _SONConverter
# parser method
_SON_CONVERTER_PARSERS: list[_SONConverterParser] = []
_son_converter_parser = metaman.register_function_factory(
    _SON_CONVERTER_PARSERS
)

_T = TypeVar("_T")


# TODO(bugyi): Rename to_select_of_note() and other related identifiers.
# TODO(bugyi): Move to_select_of_note() out of of this file!
def to_select_of_note(
    or_filter: Optional[WhereOrFilter], session: Session
) -> SelectOfScalar[sql.ZorgNote]:
    """Converts a WhereOrFilter to a SQL SELECT that will fetch ZorgNotes."""
    if or_filter is None or not or_filter.and_filters:
        return select(sql.ZorgNote)

    return (
        select(sql.ZorgNote)
        .join(
            sql.ZorgFileLink,
            cast(ColumnElement, sql.ZorgNote.id == sql.ZorgFileLink.note_id),
        )
        .join(
            sql.ZorgFile,
            cast(
                ColumnElement, sql.ZorgFileLink.zorg_file_id == sql.ZorgFile.id
            ),
        )
        .where(
            or_(*[
                _SONConverter(and_filter, session).to_note_clause()
                for and_filter in or_filter.and_filters
            ])
        )
        .order_by(cast(Column, sql.ZorgNote.id))
    )


@dataclass(frozen=True)
class _SONConverter:
    """Converts a WhereAndFilter to a ColumnElement."""

    and_filter: WhereAndFilter
    session: Session

    def to_note_clause(self) -> ColumnElement:
        """Constructs a SQL statement from the provided WhereAndFilter."""
        and_clauses = []
        for parse in _SON_CONVERTER_PARSERS:
            clause = parse(self)
            if clause is not None:
                and_clauses.append(clause)

        where = (
            and_(and_clauses[0], *and_clauses[1:])
            if len(and_clauses) > 1
            else and_clauses[0]
        )
        return where

    @_son_converter_parser
    def note_type(self) -> Optional[ColumnElement]:
        """Converter for done status (e.g. '-' or 'ox~<>')."""
        if not self.and_filter.allowed_note_types:
            return None

        return or_(*[
            sql.ZorgNote.todo_status == _to_todo_status(note_type)
            for note_type in self.and_filter.allowed_note_types
        ])

    @_son_converter_parser
    def priority_range(self) -> Optional[ColumnElement]:
        """Converter for priority range filters."""
        priorities = self.and_filter.priorities
        if priorities:
            return or_(*[
                sql.ZorgNote.todo_priority == priority
                for priority in priorities
            ])
        else:
            return None

    @_son_converter_parser
    def tags(self) -> Optional[ColumnElement]:
        """Parser for prefix tags (e.g. '@home' or '+zorg')."""
        conditions = []
        for prefix_tag_list, link_model, model in [
            (self.and_filter.areas, sql.AreaLink, sql.Area),
            (self.and_filter.contexts, sql.ContextLink, sql.Context),
            (self.and_filter.people, sql.PersonLink, sql.Person),
            (self.and_filter.projects, sql.ProjectLink, sql.Project),
        ]:
            base_subquery = (
                select(sql.ZorgNote.id).join(link_model).join(model)
            )
            for prefix_tag in prefix_tag_list:
                name = prefix_tag

                if name.startswith("-"):
                    # remove '-' from name
                    name = name[1:]
                    in_op = sql.ZorgNote.id.not_in  # type: ignore[union-attr]
                else:
                    in_op = sql.ZorgNote.id.in_  # type: ignore[union-attr]

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

    @_son_converter_parser
    def or_filters(self) -> Optional[ColumnElement]:
        """Converter that handles nested OR filters."""
        or_filters = self.and_filter.or_filters
        if not or_filters:
            return None

        or_conds = []
        for or_filter in or_filters:
            or_conds.append(
                or_(*[
                    _SONConverter(and_filter, self.session).to_note_clause()
                    for and_filter in or_filter.and_filters
                ])
            )
        return (
            and_(or_conds[0], *or_conds[1:])
            if len(or_conds) > 1
            else or_conds[0]
        )

    @_son_converter_parser
    def date_ranges(self) -> Optional[ColumnElement]:
        """Converter that handles create/modify date ranges."""
        and_conds = []
        for date_range_list, sql_date in [
            (self.and_filter.create_date_ranges, sql.ZorgNote.create_date),
            (self.and_filter.modify_date_ranges, sql.ZorgNote.modify_date),
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

    @_son_converter_parser
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
                select(sql.ZorgNote.id)
                .join(sql.PropertyLink)
                .join(sql.Property)
                .where(sql.Property.name == property_filter.key)
            )

            op = sql.ZorgNote.id.in_  # type: ignore[union-attr]
            if property_filter.op == PropertyOperator.EXISTS and negated:
                op = sql.ZorgNote.id.not_in  # type: ignore[union-attr]
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

    @_son_converter_parser
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
                cond = sql.ZorgNote.body.like(like_arg)  # type: ignore[attr-defined]
                subquery = select(sql.ZorgNote.id, sql.ZorgNote.body).where(
                    cond
                )
                id_list: list[int] = []
                for ID, body in self.session.exec(subquery).all():
                    assert (
                        ID is not None
                    ), "The DB shouldn't contain notes without an ID, right?"
                    if desc_filter.value in body:
                        id_list.append(ID)

                op_map: dict[DescOperator, Any] = {
                    DescOperator.CONTAINS: sql.ZorgNote.id.in_,  # type: ignore[union-attr]
                    DescOperator.NOT_CONTAINS: sql.ZorgNote.id.not_in,  # type: ignore[union-attr]
                }
                op = op_map[desc_filter.op]
                op_arg = id_list
            else:
                op_map = {
                    DescOperator.CONTAINS: sql.ZorgNote.body.ilike,  # type: ignore[attr-defined]
                    DescOperator.NOT_CONTAINS: sql.ZorgNote.body.not_ilike,  # type: ignore[attr-defined]
                }
                op = partial(op_map[desc_filter.op], escape="\\")
                op_arg = like_arg

            and_conds.append(op(op_arg))
        return and_(and_conds[0], *and_conds[1:])

    @_son_converter_parser
    def file_filters(self) -> Optional[ColumnElement]:
        """Converter tht handles file filters."""
        and_conds = []
        if not self.and_filter.file_filters:
            return None
        for file_filter in self.and_filter.file_filters:
            like_op = (
                sql.ZorgFile.path.not_like  # type: ignore[attr-defined]
                if file_filter.negated
                else sql.ZorgFile.path.like  # type: ignore[attr-defined]
            )
            and_conds.append(like_op(file_filter.path_glob.replace("*", "%")))
        return and_(and_conds[0], *and_conds[1:])

    @_son_converter_parser
    def link_filters(self) -> Optional[ColumnElement]:
        """Converter tht handles link filters."""
        and_conds = []
        if not self.and_filter.link_filters:
            return None
        base_subquery = (
            select(sql.ZorgNote.id).join(sql.LinkLink).join(sql.Link)
        )
        for link_filter in self.and_filter.link_filters:
            if link_filter.negated:
                in_op = sql.ZorgNote.id.not_in  # type: ignore[union-attr]
                like_op = sql.Link.name.not_like  # type: ignore[attr-defined]
            else:
                in_op = sql.ZorgNote.id.in_  # type: ignore[union-attr]
                like_op = sql.Link.name.like  # type: ignore[attr-defined]

            link_name = link_filter.link
            notes_in_file = _get_notes_in_file(self.session, link_name)
            subquery = base_subquery.where(
                or_(
                    sql.Link.name == link_name,
                    like_op(f"{link_name}#%"),
                    *_global_link_conds(notes_in_file),
                    *_zid_link_conds(notes_in_file),
                )
            )
            and_conds.append(in_op(subquery))
        return and_(and_conds[0], *and_conds[1:])


def _get_notes_in_file(session: Session, file_name: str) -> list[sql.ZorgNote]:
    stmt = (
        select(sql.ZorgNote)
        .join(sql.ZorgFileLink)
        .join(sql.ZorgFile)
        .where(sql.ZorgFile.path == f"{file_name}.zo")
    )
    return list(session.exec(stmt).all())


def _global_link_conds(notes: Iterable[sql.ZorgNote]) -> list[ColumnElement]:
    conds = []
    for note in notes:
        for prop_link in note.property_links:
            if prop_link.prop.name == "id":
                conds.append(
                    cast(
                        ColumnElement,
                        sql.Link.name == f"global:{prop_link.value}",
                    )
                )
    return conds


def _zid_link_conds(notes: Iterable[sql.ZorgNote]) -> list[ColumnElement]:
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


class ZorgFileConverter(EntityConverter[File, sql.ZorgFile]):
    """Converts File domain entities to/from ZorgFile sqlmodels."""

    def __init__(self, zdir: Path, session: Session) -> None:
        self._zdir = zdir
        self._note_converter = ZorgNoteConverter(zdir, session)
        self._all_sql_notes: list[sql.ZorgNote] = []

    def from_entity(self, entity: File) -> sql.ZorgFile:
        """Model-to-SQL-model converter for a ZorgFile."""
        sql_notes = []
        for note in entity.notes:
            sql_note = self._note_converter.from_entity(note)
            self._all_sql_notes.append(sql_note)
            sql_notes.append(sql_note)
        return sql.ZorgFile(
            path=common.strip_zdir(self._zdir, entity.path),
            notes=sql_notes,
            has_errors=entity.has_errors,
        )

    def to_entity(self, sql_model: sql.ZorgFile) -> File:
        """Model-to-SQL-model converter for a File."""
        return File(
            Path(common.strip_zdir(self._zdir, sql_model.path)),
            has_errors=sql_model.has_errors,
            notes=[
                self._note_converter.to_entity(sql_note)
                for sql_note in sql_model.notes
            ],
        )


class ZorgNoteConverter(EntityConverter[Note, sql.ZorgNote]):
    """Converts Note domain entities to/from ZorgNote sqlmodels."""

    def __init__(self, zdir: Path, session: Session) -> None:
        self._zdir = zdir
        self._session = session

        self._tag_cache: dict[Any, dict[str, Any]] = defaultdict(lambda: {})
        self._property_cache: dict[str, sql.Property] = {}

    def from_entity(self, entity: Note) -> sql.ZorgNote:
        """Model-to-SQL-model converter for a ZorgNote."""
        # HACK: Needed to prevent errors of the form:
        #   SAWarning: Object of type <ZorgNote> not in session...
        with self._session.no_autoflush as session:
            return self._from_entity_with_session(
                entity, cast(Session, session)
            )

    def _from_entity_with_session(
        self, entity: Note, session: Session
    ) -> sql.ZorgNote:
        kwargs: dict[str, Any] = {
            "body": entity.body,
            "create_date": entity.create_date,
            "modify_date": entity.modify_date,
            "zid": entity.zid,
        }
        if entity.todo_payload:
            kwargs["todo_status"] = entity.todo_payload.status
            kwargs["todo_priority"] = entity.todo_payload.priority
        sql_zorg_note = sql.ZorgNote(**kwargs)

        stmt: Any
        for attr, tag_model in [
            ("areas", sql.Area),
            ("contexts", sql.Context),
            ("people", sql.Person),
            ("projects", sql.Project),
            ("links", sql.Link),
        ]:
            entity_tag_list = getattr(entity, attr)
            sql_tag_list = []
            tag_cache = self._tag_cache[tag_model]
            for tag_name in entity_tag_list:
                if tag_name not in tag_cache:
                    stmt = select(tag_model).where(tag_model.name == tag_name)
                    results = session.exec(stmt)
                    tag = results.first()
                    if tag is None:
                        tag = tag_model(name=tag_name)
                    tag_cache[tag_name] = tag

                tag = tag_cache[tag_name]
                sql_tag_list.append(tag)
            setattr(sql_zorg_note, attr, sql_tag_list)

        property_links = []
        for k, v in entity.properties.items():
            if k not in self._property_cache:
                stmt = select(sql.Property).where(sql.Property.name == k)
                results = session.exec(stmt)
                prop = results.first()
                if prop is None:
                    prop = sql.Property(name=k)
                self._property_cache[k] = prop

            prop = self._property_cache[k]
            stmt = (
                select(sql.PropertyLink)
                .where(sql.PropertyLink.note_id == sql_zorg_note.id)
                .where(sql.PropertyLink.prop_id == prop.id)
            )
            results = session.exec(stmt)
            prop_link = results.first()

            if prop_link is None:
                prop_link = sql.PropertyLink(
                    prop=prop, todo=sql_zorg_note, value=v
                )

            property_links.append(prop_link)

        sql_zorg_note.property_links = property_links

        # Convert 'zorg_file' field.
        if entity.file_path is not None:
            stripped_file_path = common.strip_zdir(
                self._zdir, entity.file_path
            )
            stmt = select(sql.ZorgFile).where(
                sql.ZorgFile.path == stripped_file_path
            )
            results = session.exec(stmt)
            sql_zorg_note.zorg_file = results.first()

        return sql_zorg_note

    def to_entity(self, sql_model: sql.ZorgNote) -> Note:
        """Model-to-SQL-model converter for a Note."""
        todo_payload = (
            TodoPayload(
                status=sql_model.todo_status,
                priority=cast(TodoPriorityType, sql_model.todo_priority),
            )
            if sql_model.todo_priority is not None
            and sql_model.todo_status is not None
            else None
        )
        return Note(
            sql_model.body,
            areas=list(area.name for area in sql_model.areas),
            contexts=list(context.name for context in sql_model.contexts),
            create_date=sql_model.create_date,
            file_path=Path(sql_model.zorg_file.path),
            links=[link.name for link in sql_model.links],
            modify_date=sql_model.modify_date,
            people=list(person.name for person in sql_model.people),
            projects=list(project.name for project in sql_model.projects),
            todo_payload=todo_payload,
            zid=sql_model.zid,
        )
