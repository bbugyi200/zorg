"""Contains runners for the 'zorg note' command."""

from dataclasses import replace

from logrus import Logger

from ...domain.models import MetadataMutate, Mutate, Note
from ...service.compiler import build_zorg_mutate, build_zorg_query
from ...storage.file import FileManager
from ...storage.sql.session import SQLSession
from ..config import NoteMoveConfig, NoteMutateConfig
from ._runners import runner


_LOGGER = Logger(__name__)


@runner
def run_note_move(cfg: NoteMoveConfig) -> int:
    """Runner for the 'note move' command."""
    with SQLSession(
        cfg.zettel_dir, cfg.database_url, verbose=cfg.verbose
    ) as session:
        return _move_note(cfg, session)


@runner
def run_note_mutate(cfg: NoteMutateConfig) -> int:
    """Runner for the 'note move' command."""
    with SQLSession(
        cfg.zettel_dir, cfg.database_url, verbose=cfg.verbose
    ) as session:
        return _mutate_notes(cfg, session)


def _move_note(cfg: NoteMoveConfig, session: SQLSession) -> int:
    note = session.repo.get_note_by_zid(cfg.zid)

    if note is None:
        _LOGGER.error("No Zorg note with the given ZID", zid=cfg.zid)
        return 1

    _LOGGER.debug(
        f"Note with ZID={cfg.zid} found |"
        f" {str(note.file_path)}::{note.line_no}"
    )

    file_man = FileManager(cfg.zettel_dir, session)
    if cfg.mutate is not None:
        mutate = build_zorg_mutate(cfg.mutate)
        mutate = _add_hidden_mdata_mutates(mutate, note)
        mutated_note = mutate.mutate_note(note)
    else:
        mutated_note = note
    if error := file_man.add_note(mutated_note, cfg.new_page):
        _LOGGER.error("Failed to add note to page", error=f"'{error.upper()}'")
        return 1
    file_man.delete_note(note)
    return 0


def _add_hidden_mdata_mutates(mutate: Mutate, note: Note) -> Mutate:
    new_mut = replace(mutate)
    new_mut.metadata_mutates.append(
        MetadataMutate(
            mtype="links", value=str(note.file_path).replace(".zo", "")
        )
    )
    for ch, tag_name, tags in [
        ("+", "projects", note.projects),
        ("#", "areas", note.areas),
        ("@", "contexts", note.contexts),
        ("%", "people", note.people),
    ]:
        for tag in tags:
            if f"{ch}{tag}" not in note.body:
                new_mut.metadata_mutates.append(
                    MetadataMutate(mtype=tag_name, value=tag)
                )

    for key, value in note.properties.items():
        prop_value = f"{key}::{value}"
        if prop_value not in note.body:
            new_mut.metadata_mutates.append(
                MetadataMutate(mtype="properties", value=prop_value)
            )
    return new_mut


def _mutate_notes(cfg: NoteMutateConfig, session: SQLSession) -> int:
    where_query = build_zorg_query(cfg.where_query).where
    notes = session.repo.get_notes_by_query(where_query)
    mutate = build_zorg_mutate(cfg.mutate)
    for note in notes:
        print(mutate.mutate_note(note).to_string())
    return 0
