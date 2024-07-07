"""A utility class used to manage Zorg files lives here."""

from pathlib import Path
from typing import NewType, Optional

from zorg.domain.models import Note
from zorg.service.common import prepend_zdir


Error = NewType("Error", str)


class FileManager:
    """Zorg (i.e *.zo) file manager."""

    def __init__(
        self,
        zdir: Path,
    ) -> None:
        self._zdir = zdir

    def add_note(  # pylint: disable=useless-return
        self, note: Note, page: Path
    ) -> Optional[Error]:
        """Adds {note} to the bottom of {page}."""
        zpage = prepend_zdir(self._zdir, [page])[0]
        if not zpage.exists():
            return Error(f"Page does NOT exist: {zpage}")

        zlines = zpage.read_text().split("\n")
        in_note = False
        start_idx = len(zlines) - 1
        for i, line in enumerate(zlines):
            if line.startswith(("- ", "o ", "~ ", "x ", "< ", "> ")):
                in_note = True
            if in_note and line.strip() == "":
                in_note = False
                start_idx = i
        end_idx = start_idx + 1
        new_zlines = (
            zlines[:start_idx]
            + note.to_string().split("\n")
            + zlines[end_idx:]
        )
        new_zcontents = "\n".join(new_zlines)
        zpage.write_text(new_zcontents)
        return None

    def delete_note(self, note: Note) -> Optional[Error]:
        """Removes {note} from its last known *.zo file."""
        zpage = prepend_zdir(self._zdir, [note.file_path])[0]
        assert note.zid is not None
        for i, line in enumerate(zpage.read_text().split("\n")):
            if f" {note.zid} " in line:
                start_idx = i
                break
        else:
            err_ctx = f"ZID={note.zid} FILE={note.file_path}"
            return Error(f"Unable to find note in file | {err_ctx}")
        end_idx = start_idx + len(note.body.split("\n"))
        zlines = zpage.read_text().split("\n")
        new_zlines = zlines[:start_idx] + zlines[end_idx:]
        new_zcontents = "\n".join(new_zlines)
        zpage.write_text(new_zcontents)
        return None
