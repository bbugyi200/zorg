"""Contains the Mutate domain entity."""

from dataclasses import dataclass, field, replace
import enum
from typing import Optional, Union

from ...domain.types import MetadataType, NoteType, TodoPriorityType
from ._zorg_file import Note, TodoPayload


NoteTypeMutate = Union["OpenTodoNoteTypeMutate", "StaticNoteTypeMutate"]


class OpenTodoType(enum.Enum):
    """The type of an open todo (e.g. o, x, or ~)."""

    OPEN_TODO = "o"
    PARENT_TODO = ">"
    BLOCKED_TODO = "<"


@dataclass(frozen=True)
class OpenTodoNoteTypeMutate:
    """Mutates a note into an open todo with a new priority"""

    todo_type: OpenTodoType
    priority: TodoPriorityType = "P2"


class StaticNoteTypeMutate(enum.Enum):
    """Mutate a note into a type with no priority (e.g. note or done todo)."""

    NOTE = "-"
    DONE_TODO = "x"
    CANCELED_TODO = "~"


@dataclass(frozen=True)
class MetadataMutate:
    """Mutates a tag/link."""

    mtype: MetadataType
    value: str
    negated: bool = False


@dataclass
class Mutate:
    """Zorg domain entitiy that represents a mutate command"""

    note_type_mutate: Optional[NoteTypeMutate] = None
    metadata_mutates: list[MetadataMutate] = field(default_factory=list)

    def mutate_note(self, note: Note) -> Note:
        """The method that is called to actually modify a Note."""
        new_note = replace(note)
        if self.note_type_mutate is not None:
            kwargs: dict[str, TodoPriorityType] = {}
            note_type: Union[StaticNoteTypeMutate, OpenTodoType]
            if isinstance(self.note_type_mutate, OpenTodoNoteTypeMutate):
                kwargs["priority"] = self.note_type_mutate.priority
                note_type = self.note_type_mutate.todo_type
            else:
                note_type = self.note_type_mutate

            if note_type is StaticNoteTypeMutate.NOTE:
                todo_payload = None
            else:
                todo_payload = TodoPayload(
                    status=NoteType(note_type.value), **kwargs
                )
            new_note.todo_payload = todo_payload
        if len(self.metadata_mutates) > 1:
            empty_extra_tags = "  *----->"
        else:
            empty_extra_tags = ""
        extra_tags = empty_extra_tags
        for tag_link_mutate in self.metadata_mutates:
            prefix_chars: str = ""
            suffix_chars: str = ""
            mtype = tag_link_mutate.mtype
            if mtype == "areas":
                prefix_chars = "#"
            elif mtype == "contexts":
                prefix_chars = "@"
            elif mtype == "projects":
                prefix_chars = "+"
            elif mtype == "people":
                prefix_chars = "%"
            elif mtype == "links":
                prefix_chars = "[["
                suffix_chars = "]]"
            elif mtype == "properties":
                pass
            extra_tags += (
                f" {prefix_chars}{tag_link_mutate.value}{suffix_chars}"
            )
        if extra_tags != empty_extra_tags:
            assert new_note.zid is not None
            if len(self.metadata_mutates) > 1:
                new_note.body = f"{new_note.body}\n{extra_tags}"
            else:
                new_note.body = new_note.body.replace(
                    new_note.zid, f"{new_note.zid}{extra_tags}"
                )
        return new_note
