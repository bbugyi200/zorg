"""Contains zorg's SQL model class definitions."""

# WARNING: Don't bother importing __future__.annotations in this module!
import datetime as dt
from typing import List, Optional

from sqlmodel import Field, Relationship, SQLModel, String
from sqlmodel.sql.expression import Select, SelectOfScalar

from zorg.domain.types import NoteType


# HACK: see https://github.com/tiangolo/sqlmodel/issues/189
Select.inherit_cache = True
SelectOfScalar.inherit_cache = True


###############################################################################
# abstract model classes
###############################################################################
class Base(SQLModel):
    """Abstract base model class."""

    id: Optional[int] = Field(default=None, primary_key=True)


class NoteLink(SQLModel):
    """Abstract model for association/link models."""

    note_id: Optional[int] = Field(
        default=None, foreign_key="zorgnote.id", primary_key=True
    )


class Tag(Base):
    """Abstract model class for todo.txt tags."""

    name: str = Field(sa_type=String)


###############################################################################
# link models (i.e. assocation tables for many-to-many relationships)
###############################################################################
class ProjectLink(NoteLink, table=True):
    """Association model for notes-to-projects relationships."""

    project_id: Optional[int] = Field(
        default=None, foreign_key="project.id", primary_key=True
    )


class ContextLink(NoteLink, table=True):
    """Association model for notes-to-contexts relationships."""

    context_id: Optional[int] = Field(
        default=None, foreign_key="context.id", primary_key=True
    )


class AreaLink(NoteLink, table=True):
    """Association model for notes-to-areas relationships."""

    area_id: Optional[int] = Field(
        default=None, foreign_key="area.id", primary_key=True
    )


class PersonLink(NoteLink, table=True):
    """Association model for notes-to-areas relationships."""

    person_id: Optional[int] = Field(
        default=None, foreign_key="person.id", primary_key=True
    )


class PropertyLink(NoteLink, table=True):
    """Association model for note-to-property relationships."""

    prop_id: Optional[int] = Field(
        default=None, foreign_key="property.id", primary_key=True
    )

    note: "ZorgNote" = Relationship(back_populates="property_links")
    prop: "Property" = Relationship(back_populates="links")

    value: str


class LinkLink(NoteLink, table=True):
    """Association model for note-to-link relationships."""

    link_id: Optional[int] = Field(
        default=None, foreign_key="link.id", primary_key=True
    )


###############################################################################
# models used to track zorg file sections
###############################################################################
class H1(Base, table=True):
    """Model class for H1 sections in zorg files."""

    zorg_file_id: int = Field(foreign_key="zorgfile.id")

    zorg_file: "ZorgFile" = Relationship(back_populates="h1s")
    h2s: List["H2"] = Relationship(back_populates="h1")


class H2(Base, table=True):
    """Model class for H2 sections in zorg files."""

    h1_id: int = Field(foreign_key="h1.id")

    h1: H1 = Relationship(back_populates="h2s")
    h3s: List["H3"] = Relationship(back_populates="h2")


class H3(Base, table=True):
    """Model class for H3 sections in zorg files."""

    h2_id: int = Field(foreign_key="h2.id")

    h2: H2 = Relationship(back_populates="h3s")
    h4s: List["H4"] = Relationship(back_populates="h3")


class H4(Base, table=True):
    """Model class for H4 sections in zorg files."""

    h3_id: int = Field(foreign_key="h3.id")

    h3: H3 = Relationship(back_populates="h4s")


###############################################################################
# model used to track zorg (*.zo) files
###############################################################################
class ZorgFile(Base, table=True):
    """Model class for zorg (*.zo) files."""

    path: str
    has_errors: bool = False
    notes: List["ZorgNote"] = Relationship(back_populates="zorg_file")
    h1s: List[H1] = Relationship(back_populates="zorg_file")


###############################################################################
# model used to store notes
###############################################################################
class ZorgNote(Base, table=True):
    """Model class for zorg notes."""

    # table columns
    body: str
    line_no: int

    # TODO(bugyi): Make zid required to persist to DB.
    # TODO(bugyi): Make zid unique.
    zid: Optional[str] = Field(default=None)

    create_date: dt.date = Field(default_factory=dt.date.today)
    modify_date: dt.date = Field(default_factory=dt.date.today)
    todo_priority: Optional[str] = None
    todo_status: Optional[NoteType] = None

    zorg_file_id: int = Field(foreign_key="zorgfile.id")

    # relationships
    zorg_file: ZorgFile = Relationship(back_populates="notes")
    links: List["Link"] = Relationship(
        back_populates="notes", link_model=LinkLink
    )
    contexts: List["Context"] = Relationship(
        back_populates="notes", link_model=ContextLink
    )
    areas: List["Area"] = Relationship(
        back_populates="notes", link_model=AreaLink
    )
    people: List["Person"] = Relationship(
        back_populates="notes", link_model=PersonLink
    )
    projects: List["Project"] = Relationship(
        back_populates="notes", link_model=ProjectLink
    )
    property_links: List["PropertyLink"] = Relationship(back_populates="note")


###############################################################################
# tag models
###############################################################################
class Project(Tag, table=True):
    """Model class for todo.txt project tags (e.g. +zorg)."""

    notes: List[ZorgNote] = Relationship(
        back_populates="projects", link_model=ProjectLink
    )


class Context(Tag, table=True):
    """Model class for todo.txt context tags (e.g. @home)."""

    notes: List[ZorgNote] = Relationship(
        back_populates="contexts", link_model=ContextLink
    )


class Area(Tag, table=True):
    """Model class for todo.txt area tags (e.g. #gtd)."""

    notes: List[ZorgNote] = Relationship(
        back_populates="areas", link_model=AreaLink
    )


class Person(Tag, table=True):
    """Model class for todo.txt person tags (e.g. %john)."""

    notes: List[ZorgNote] = Relationship(
        back_populates="people", link_model=PersonLink
    )


class Property(Tag, table=True):
    """Model class for properties (e.g. due::2022-06-01)."""

    links: List[PropertyLink] = Relationship(back_populates="prop")


class Link(Tag, table=True):
    """Model class for links (e.g. [[foobar]])."""

    notes: List[ZorgNote] = Relationship(
        back_populates="links", link_model=LinkLink
    )
