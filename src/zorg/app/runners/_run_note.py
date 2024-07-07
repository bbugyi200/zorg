"""Contains runners for the 'zorg note' command."""

from dataclasses import replace

from logrus import Logger

from zorg.app.config import NoteMoveConfig
from zorg.domain.models import MetadataMutate, Mutate, Note
from zorg.domain.types import cast_tag_name
from zorg.service.compiler import build_zorg_mutate
from zorg.service.note_utils import note_body_has_tag
from zorg.storage.file import FileManager
from zorg.storage.sql.session import SQLSession

from ._runners import runner


_LOGGER = Logger(__name__)


@runner
def run_note_move(cfg: NoteMoveConfig) -> int:
    """Runner for the 'note move' command."""
    with SQLSession(
        cfg.zettel_dir, cfg.database_url, verbose=cfg.verbose
    ) as session:
        return _move_note(cfg, session)


def _move_note(cfg: NoteMoveConfig, session: SQLSession) -> int:
    note = session.repo.get_note_by_zid(cfg.zid)

    if note is None:
        _LOGGER.error("No Zorg note with the given ZID", zid=cfg.zid)
        return 1

    _LOGGER.debug(
        f"Note with ZID={cfg.zid} found |"
        f" {str(note.file_path)}::{note.line_no}"
    )

    file_man = FileManager(cfg.zettel_dir, cfg.template_pattern_map)
    if cfg.note_type is not None:
        mutate = build_zorg_mutate(cfg.note_type)
    else:
        mutate = Mutate()

    mutate = _add_hidden_mdata_mutates(mutate, note)
    mutated_note = mutate.mutate_note(note)
    if error := file_man.add_note(mutated_note, cfg.new_page):
        _LOGGER.error("Failed to add note to page", error=f"'{error.upper()}'")
        return 1

    if error := file_man.delete_note(note):
        _LOGGER.error(
            "Failed to delete note from page", error=f"'{error.upper()}'"
        )
        return 1
    return 0


def _add_hidden_mdata_mutates(mutate: Mutate, note: Note) -> Mutate:
    new_mut = replace(mutate)
    for ch, tag_name, tags in [
        ("+", cast_tag_name("projects"), note.projects),
        ("#", cast_tag_name("areas"), note.areas),
        ("@", cast_tag_name("contexts"), note.contexts),
        ("%", cast_tag_name("people"), note.people),
    ]:
        for tag in sorted(tags):
            tag_word = f"{ch}{tag}"
            if not note_body_has_tag(note.body, tag_word):
                new_mut.metadata_mutates.append(
                    MetadataMutate(mtype=tag_name, value=tag)
                )

    for key, value in sorted(note.properties.items()):
        prop_value = f"{key}::{value}"
        if f"{key}::" not in note.body:
            new_mut.metadata_mutates.append(
                MetadataMutate(mtype="properties", value=prop_value)
            )
    return new_mut
