"""Convert domain Pages/Notes to/from SQL ZorgFile/ZorgNote models."""

from collections import defaultdict
from pathlib import Path
from typing import Any, Optional, cast

from sqlmodel import Session, select

from zorg.domain.models import H1, H2, H3, H4, Block, Note, Page, TodoPayload
from zorg.domain.types import EntityConverter, TodoPriorityType
from zorg.shared import common

from . import _models as sql


class PageConverter(EntityConverter[Page, sql.ZorgFile]):
    """Converts Page domain entities to/from ZorgFile sqlmodels."""

    def __init__(self, zdir: Path, session: Session) -> None:
        self._zdir = zdir
        self._h1_converter = _H1Converter(self._zdir, session)

    def from_entity(self, page: Page) -> sql.ZorgFile:
        """Model-to-SQL-model converter for a ZorgFile."""
        sql_h1s = []
        h1s = list(page.h1s)
        if page.h0:
            h1s = [page.h0] + h1s

        sql_zorg_file = sql.ZorgFile(
            path=common.strip_zdir(self._zdir, page.path),
            has_errors=page.has_errors,
        )
        for h1 in h1s:
            sql_h1 = self._h1_converter.from_entity(h1)
            sql_h1s.append(sql_h1)
        sql_zorg_file.h1s = sql_h1s
        return sql_zorg_file

    def to_entity(self, sql_page: sql.ZorgFile) -> Page:
        """Model-to-SQL-model converter for a Page."""
        page = Page(
            Path(common.strip_zdir(self._zdir, sql_page.path)),
            has_errors=sql_page.has_errors,
        )
        sql_h1s = list(sql_page.h1s)
        h0: Optional[H1] = None
        if sql_page.h1s and sql_page.h1s[0].title == "":
            h0 = self._h1_converter.to_entity(sql_h1s.pop(0))
            h0.page = page
        page.h0 = h0

        h1s = []
        for sql_h1 in sql_h1s:
            h1 = self._h1_converter.to_entity(sql_h1)
            h1.page = page
            h1s.append(h1)
        page.h1s = h1s

        return page


class NoteConverter(EntityConverter[Note, sql.ZorgNote]):
    """Converts Note domain entities to/from ZorgNote sqlmodels."""

    def __init__(self, zdir: Path, session: Session) -> None:
        self._zdir = zdir
        self._session = session

        self._tag_cache: dict[Any, dict[str, Any]] = defaultdict(lambda: {})
        self._property_cache: dict[str, sql.Property] = {}

    def from_entity(self, note: Note) -> sql.ZorgNote:
        """Model-to-SQL-model converter for a ZorgNote."""
        # HACK: Needed to prevent errors of the form:
        #   SAWarning: Object of type <ZorgNote> not in session...
        with self._session.no_autoflush as session:
            return self._from_entity_with_session(note, cast(Session, session))

    def _from_entity_with_session(
        self, note: Note, session: Session
    ) -> sql.ZorgNote:
        kwargs: dict[str, Any] = {
            "body": note.body,
            "create_date": note.create_date,
            "modify_date": note.modify_date,
            "zid": note.zid,
        }
        if note.todo_payload:
            kwargs["todo_status"] = note.todo_payload.status
            kwargs["todo_priority"] = note.todo_payload.priority
        sql_zorg_note = sql.ZorgNote(**kwargs)

        stmt: Any
        for attr, tag_model in [
            ("areas", sql.Area),
            ("contexts", sql.Context),
            ("people", sql.Person),
            ("projects", sql.Project),
            ("links", sql.Link),
        ]:
            entity_tag_list = getattr(note, attr)
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
        for k, v in note.properties.items():
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

        sql_zorg_note.line_no = note.line_no
        sql_zorg_note.page_path = common.strip_zdir(self._zdir, note.file_path)
        return sql_zorg_note

    def to_entity(self, sql_note: sql.ZorgNote) -> Note:
        """Model-to-SQL-model converter for a Note."""
        todo_payload = (
            TodoPayload(
                status=sql_note.todo_status,
                priority=cast(TodoPriorityType, sql_note.todo_priority),
            )
            if sql_note.todo_priority is not None
            and sql_note.todo_status is not None
            else None
        )
        properties: dict[str, str] = {}
        for prop_link in sql_note.property_links:
            properties[prop_link.prop.name] = prop_link.value

        return Note(
            sql_note.body,
            areas=list(area.name for area in sql_note.areas),
            contexts=list(context.name for context in sql_note.contexts),
            create_date=sql_note.create_date,
            file_path=Path(sql_note.page_path),
            line_no=sql_note.line_no,
            links=[link.name for link in sql_note.links],
            modify_date=sql_note.modify_date,
            people=list(person.name for person in sql_note.people),
            projects=list(project.name for project in sql_note.projects),
            properties=properties,
            todo_payload=todo_payload,
            zid=sql_note.zid,
        )


class _H1Converter(EntityConverter[H1, sql.H1]):
    """Converts H1 domain entities to/from H1 sqlmodels."""

    def __init__(self, zdir: Path, session: Session) -> None:
        self._block_converter = _BlockConverter(zdir, session)
        self._h2_converter = _H2Converter(self._block_converter)

    def from_entity(self, h1: H1) -> sql.H1:  # noqa: D102
        sql_h2s = []
        for h2 in h1.h2s:
            sql_h2s.append(self._h2_converter.from_entity(h2))

        sql_h1 = sql.H1(title=h1.title)
        sql_h1.h2s = sql_h2s
        sql_h1.blocks = [
            self._block_converter.from_entity(block) for block in h1.blocks
        ]
        return sql_h1

    def to_entity(self, sql_h1: sql.H1) -> H1:  # noqa: D102
        h1 = H1(title=sql_h1.title, blocks=[])

        h2s = []
        for sql_h2 in sql_h1.h2s:
            h2 = self._h2_converter.to_entity(sql_h2)
            h2.h1 = h1
            h2s.append(h2)
        h1.h2s = h2s

        for sql_block in sql_h1.blocks:
            block = self._block_converter.to_entity(sql_block)
            block.section = h1
            h1.blocks.append(block)

        return h1


class _H2Converter(EntityConverter[H2, sql.H2]):
    """Converts H2 domain entities to/from H2 sqlmodels."""

    def __init__(self, block_converter: "_BlockConverter") -> None:
        self._h3_converter = _H3Converter(block_converter)
        self._block_converter = block_converter

    def from_entity(self, h2: H2) -> sql.H2:  # noqa: D102
        sql_h2 = sql.H2(
            title=h2.title,
            h3s=[self._h3_converter.from_entity(h3) for h3 in h2.h3s],
        )
        sql_h2.blocks = [
            self._block_converter.from_entity(block) for block in h2.blocks
        ]
        return sql_h2

    def to_entity(self, sql_h2: sql.H2) -> H2:  # noqa: D102
        h2 = H2(title=sql_h2.title, blocks=[])

        h3s = []
        for sql_h3 in sql_h2.h3s:
            h3 = self._h3_converter.to_entity(sql_h3)
            h3.h2 = h2
            h3s.append(h3)
        h2.h3s = h3s

        for sql_block in sql_h2.blocks:
            block = self._block_converter.to_entity(sql_block)
            block.section = h2
            h2.blocks.append(block)

        return h2


class _H3Converter(EntityConverter[H3, sql.H3]):
    """Converts H3 domain entities to/from H3 sqlmodels."""

    def __init__(self, block_converter: "_BlockConverter") -> None:
        self._h4_converter = _H4Converter(block_converter)
        self._block_converter = block_converter

    def from_entity(self, h3: H3) -> sql.H3:  # noqa: D102
        sql_h4s = []
        for h4 in h3.h4s:
            sql_h4s.append(self._h4_converter.from_entity(h4))

        sql_h3 = sql.H3(title=h3.title)
        sql_h3.h4s = sql_h4s
        sql_h3.blocks = [
            self._block_converter.from_entity(block) for block in h3.blocks
        ]
        return sql_h3

    def to_entity(self, sql_h3: sql.H3) -> H3:  # noqa: D102
        h3 = H3(title=sql_h3.title, blocks=[])

        h4s = []
        for sql_h4 in sql_h3.h4s:
            h4 = self._h4_converter.to_entity(sql_h4)
            h4.h3 = h3
            h4s.append(h4)
        h3.h4s = h4s

        for sql_block in sql_h3.blocks:
            block = self._block_converter.to_entity(sql_block)
            block.section = h3
            h3.blocks.append(block)

        return h3


class _H4Converter(EntityConverter[H4, sql.H4]):
    """Converts H4 domain entities to/from H4 sqlmodels."""

    def __init__(self, block_converter: "_BlockConverter") -> None:
        self._block_converter = block_converter

    def from_entity(self, h4: H4) -> sql.H4:  # noqa: D102
        sql_h4 = sql.H4(title=h4.title)
        sql_h4.blocks = [
            self._block_converter.from_entity(block) for block in h4.blocks
        ]
        return sql_h4

    def to_entity(self, sql_h4: sql.H4) -> H4:  # noqa: D102
        h4 = H4(title=sql_h4.title, blocks=[])
        for sql_block in sql_h4.blocks:
            block = self._block_converter.to_entity(sql_block)
            block.section = h4
            h4.blocks.append(block)
        return h4


class _BlockConverter(EntityConverter[Block, sql.Block]):
    """Converts Block domain entities to/from Block sqlmodels."""

    def __init__(self, zdir: Path, session: Session) -> None:
        self._note_converter = NoteConverter(zdir, session)

    def from_entity(self, block: Block) -> sql.Block:  # noqa: D102
        sql_block = sql.Block(
            notes=[
                self._note_converter.from_entity(note) for note in block.notes
            ]
        )
        return sql_block

    def to_entity(self, sql_block: sql.Block) -> Block:  # noqa: D102
        block = Block()
        notes = []
        for sql_note in sql_block.notes:
            note = self._note_converter.to_entity(sql_note)
            note.block = block
            notes.append(note)
        block.notes = notes
        return block
