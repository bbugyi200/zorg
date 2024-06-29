"""Contains service logic used to compile mutate commands."""

from typing import Optional, cast

from ...domain.models import (
    MetadataMutate,
    Mutate,
    NoteTypeMutate,
    OpenTodoNoteTypeMutate,
    OpenTodoType,
    StaticNoteTypeMutate,
)
from ...domain.types import MetadataType, TodoPriorityType
from ...grammar.zorg_mutate.ZorgMutateListener import ZorgMutateListener
from ...grammar.zorg_mutate.ZorgMutateParser import ZorgMutateParser


class ZorgMutateCompiler(ZorgMutateListener):
    """Listener that compiles zorg mutate commands."""

    def __init__(self) -> None:
        self._note_type_mutate: Optional[NoteTypeMutate] = None
        self._metadata_mutates: list[MetadataMutate] = []

    def enterMut_link(
        self, ctx: ZorgMutateParser.Mut_linkContext
    ) -> None:  # noqa: D102
        id_ctx = cast(ZorgMutateParser.IdContext, ctx.id_())
        self._metadata_mutates.append(
            MetadataMutate(mtype="links", value=id_ctx.getText())
        )

    def enterMut_note_type(
        self, ctx: ZorgMutateParser.Mut_note_typeContext
    ) -> None:  # noqa: D102
        mut_note_type = ctx.getText()
        priority: TodoPriorityType = "P2"
        if mut_note_type[0].isdigit():
            priority = cast(TodoPriorityType, "P" + mut_note_type[0])
            mut_note_type = mut_note_type[1:]
        if mut_note_type in ["o", "<", ">"]:
            self._note_type_mutate = OpenTodoNoteTypeMutate(
                OpenTodoType(mut_note_type), priority=priority
            )
        else:
            self._note_type_mutate = StaticNoteTypeMutate(mut_note_type)

    def enterMut_prop(
        self, ctx: ZorgMutateParser.Mut_propContext
    ) -> None:  # noqa: D102
        key = ctx.key().getText()
        value = ctx.value().getText()
        prop = f"{key}::{value}"
        self._metadata_mutates.append(
            MetadataMutate(mtype="properties", value=prop)
        )

    def enterMut_tag(
        self, ctx: ZorgMutateParser.Mut_tagContext
    ) -> None:  # noqa: D102
        tag = cast(ZorgMutateParser.TagContext, ctx.tag())
        mtype: MetadataType
        if t := tag.area():
            mtype = "areas"
            value = t.id_().getText()
        elif t := tag.context():
            mtype = "contexts"
            value = t.id_().getText()
        elif t := tag.person():
            mtype = "people"
            value = t.id_().getText()
        elif t := tag.project():
            mtype = "projects"
            value = t.id_().getText()
        else:
            raise RuntimeError(f"Unknnown tag type: {tag.getText()}")
        self._metadata_mutates.append(MetadataMutate(mtype=mtype, value=value))

    @property
    def mutate(self) -> Mutate:
        """Constructs a Mutate command.

        Should only be accessed AFTER parsing a mutate command with this class.
        """
        return Mutate(
            note_type_mutate=self._note_type_mutate,
            metadata_mutates=self._metadata_mutates,
        )
