"""A utility class used to manage Zorg files lives here."""

from pathlib import Path
from typing import NewType, Optional

from ...domain.models import FileFilter, Note, WhereAndFilter, WhereOrFilter
from ...domain.types import TemplatePatternMapType
from ...service.common import prepend_zdir
from ...service.templates import init_from_template
from ..sql.session import SQLSession


Error = NewType("Error", str)


class FileManager:
    """Zorg (i.e *.zo) file manager."""

    def __init__(
        self,
        zdir: Path,
        session: SQLSession,
        template_pattern_map: TemplatePatternMapType,
    ) -> None:
        self._zdir = zdir
        self._session = session
        self._template_pattern_map = template_pattern_map

    def add_note(self, note: Note, page: Path) -> Optional[Error]:
        """Adds {note} to the bottom of {page}."""
        zpage = prepend_zdir(self._zdir, [page])[0]
        if not zpage.exists():
            init_from_template(self._zdir, self._template_pattern_map, zpage)

        page_query = WhereOrFilter(
            and_filters=[WhereAndFilter(file_filters={FileFilter(str(page))})]
        )
        page_notes = self._session.repo.get_notes_by_query(page_query)
        zlines = zpage.read_text().split("\n")
        if page_notes:
            last_note = max(page_notes, key=lambda note: note.line_no)
            new_note_line_no = last_note.line_no + len(
                last_note.body.split("\n")
            )
        else:
            new_note_line_no = len(zlines)
        start_idx = new_note_line_no - 1
        end_idx = new_note_line_no
        new_zlines = (
            zlines[:start_idx]
            + note.to_string().split("\n")
            + zlines[end_idx:]
        )
        new_zcontents = "\n".join(new_zlines)
        zpage.write_text(new_zcontents)
        return None

    def delete_note(self, note: Note) -> None:
        """Removes {note} from its last known *.zo file."""
        zpage = prepend_zdir(self._zdir, [note.file_path])[0]
        start_idx = note.line_no - 1
        end_idx = note.line_no + len(note.body.split("\n")) - 1
        zlines = zpage.read_text().split("\n")
        new_zlines = zlines[:start_idx] + zlines[end_idx:]
        new_zcontents = "\n".join(new_zlines)
        zpage.write_text(new_zcontents)
