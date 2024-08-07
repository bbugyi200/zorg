"""Tests for the zorg project's 'note' CLI command."""

from __future__ import annotations

from pathlib import Path
from typing import Optional

from pytest import mark, param
from syrupy.assertion import SnapshotAssertion as Snapshot

from . import common as c


params = mark.parametrize


@params(
    "zid,src_name,dest_name,mutate",
    [
        param("240510#02", "basic.zo", "property.zo", None, id="basic"),
        param(
            "240510#0Q",
            "property.zo",
            "tags_and_ids.zo",
            "~",
            id="canceled_multiline",
        ),
        param(
            "301231#X1",
            "tags_and_ids.zo",
            "priority.zo",
            "x",
            id="done_inherited_tags",
        ),
    ],
)
def test_note_move(
    main: c.MainType,
    local_zettel_dir: Path,
    snapshot: Snapshot,
    zid: str,
    src_name: str,
    dest_name: str,
    mutate: Optional[str],
) -> None:
    """Tests the 'note move' command."""
    main_args = [
        "--dir",
        str(local_zettel_dir),
        "note",
        "move",
        zid,
        dest_name,
    ]
    if mutate is not None:
        main_args.append(mutate)
    exit_code = main(*main_args)

    src_path = local_zettel_dir / src_name
    dest_path = local_zettel_dir / dest_name
    assert exit_code == 0
    assert snapshot == src_path.read_text()
    assert snapshot == dest_path.read_text()


@params(
    "zid"
    " ,new_page_name"
    " ,parent_page_name"
    " ,old_parent_name"
    " ,expected_new_page_name",
    [
        param(
            "301231#X0",
            None,
            None,
            "tags_and_ids.zo",
            "pig_is_gross.zo",
            id="pig_is_gross",
        )
    ],
)
def test_note_promote(
    main: c.MainType,
    local_zettel_dir: Path,
    snapshot: Snapshot,
    zid: str,
    new_page_name: Optional[str],
    parent_page_name: Optional[str],
    old_parent_name: str,
    expected_new_page_name: str,
) -> None:
    """Flexes the 'zorg note promote' command."""
    main_args = ["--dir", str(local_zettel_dir), "note", "promote", zid]
    if new_page_name is not None:
        main_args.extend(["--new-page-name", new_page_name])
    if parent_page_name is not None:
        main_args.extend(["--parent-page-name", parent_page_name])

    exit_code = main(*main_args)

    old_parent_path = local_zettel_dir / old_parent_name
    new_page_path = local_zettel_dir / expected_new_page_name
    assert exit_code == 0
    assert snapshot == old_parent_path.read_text()
    assert snapshot == new_page_path.read_text()
