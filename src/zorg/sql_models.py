"""Contains zorg's SQL model class definitions."""

# WARNING: Don't bother importing __future__.annotations in this module!
import datetime as dt
from typing import List, Optional

from sqlmodel import Field, Relationship, SQLModel, String
from sqlmodel.sql.expression import Select, SelectOfScalar


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
        default=None, foreign_key="note.id", primary_key=True
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
    """Association model for notes-to-metatags relationships."""

    metatag_id: Optional[int] = Field(
        default=None, foreign_key="prop.id", primary_key=True
    )

    note: "Note" = Relationship(back_populates="property_links")
    prop: "Property" = Relationship(back_populates="links")

    value: str


###############################################################################
# model used to store notes
###############################################################################
class Note(Base, table=True):
    """Model class for zorg notes."""

    # table columns
    create_date: dt.date
    desc: str
    done: bool
    done_date: Optional[dt.date]
    priority: str

    # relationships
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

    notes: List[Note] = Relationship(
        back_populates="projects", link_model=ProjectLink
    )


class Context(Tag, table=True):
    """Model class for todo.txt context tags (e.g. @home)."""

    notes: List[Note] = Relationship(
        back_populates="contexts", link_model=ContextLink
    )


class Area(Tag, table=True):
    """Model class for todo.txt area tags (e.g. #gtd)."""

    notes: List[Note] = Relationship(
        back_populates="areas", link_model=AreaLink
    )


class Person(Tag, table=True):
    """Model class for todo.txt person tags (e.g. %john)."""

    notes: List[Note] = Relationship(
        back_populates="people", link_model=PersonLink
    )


class Property(Tag, table=True):
    """Model class for metadata tags (e.g. due:2022-06-01)."""

    links: List[PropertyLink] = Relationship(back_populates="prop")
