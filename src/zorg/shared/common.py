"""Helper logic that is shared broadly across this package."""

import datetime as dt
import itertools as it
from pathlib import Path
import re
import sys
from typing import Any, Iterable, Iterator, TypeVar

import rich
from typist import PathLike

from zorg.domain.types import Color, VarMapType


_T = TypeVar("_T")


def get_only_item(items: Iterable[_T]) -> _T:
    """Returns the only element in {items} OR raises a ValueError."""
    items = list(items)
    if len(items) == 1:
        return items[0]
    elif not items:
        raise ValueError("Iterable has NO elements")
    else:
        raise ValueError(f"Iterable has too many elements: {items}")


def process_var_map(var_map: VarMapType) -> dict[str, Any]:
    """Processes and potentially adds to {var_map}."""
    new_var_map = {}
    for k, v in var_map.items():
        new_var_map[k] = _var_map_value(v)
    return new_var_map


def prepend_zdir(zdir: PathLike, paths: Iterable[PathLike]) -> list[Path]:
    """Prepend the given zettel directory to all given paths.

    Returns:
        A new list of paths constructed by prepending {zdir} to each Path in
        {paths}.
    """
    zdir_path = Path(zdir)
    new_paths = []
    for p in paths:
        path = Path(p)
        new_paths.append(
            path if zdir_path in path.parents else zdir_path / path
        )
    return new_paths


def simplify_fname(zdir: PathLike, path: PathLike) -> str:
    """Remove '.zo' extension and strip {zdir} from {path}."""
    fname = strip_zdir(zdir, path)
    if fname.endswith(".zo"):
        fname = fname[:-3]
    return fname


def strip_zdir(zdir: PathLike, path: PathLike) -> str:
    """Strips {zdir} from {path}."""
    return str(path).replace(f"{zdir}/", "")


def zprint(
    *msg_parts: str,
    style: str = "bold",
    bg_color: Color = Color.WHITE,
    fg_color: Color = Color.BLACK,
) -> None:
    """Custom rich.print() wrapper used by Zorg."""
    # get call count
    call_count_attr = "_call_count"
    call_count = getattr(zprint, call_count_attr, 1)

    # prep variables used by final message
    space_call_count = str(call_count)
    while len(space_call_count) < 3:
        space_call_count = f" {space_call_count}"
    hhmmss = dt.datetime.now().strftime("%H:%M:%S")
    msg = " | ".join(msg_parts)
    bg = bg_color.value
    fg = fg_color.value

    # print final message
    contents = f"{space_call_count} | {hhmmss} | {msg}"
    rich.print(f"[{style} {fg} on {bg}]{contents}[/]")

    # set call count
    setattr(zprint, call_count_attr, call_count + 1)


def zinput(prompt: str) -> str:
    """Custom input() wrapper used by Zorg."""
    print(prompt, file=sys.stderr, end="")
    return input()


def get_all_zfiles(zdir: PathLike) -> Iterator[Path]:
    """Returns all *.zo, *.zot, and *.zoq files."""
    zdir = Path(zdir)
    return it.chain(
        zdir.rglob("*.zo"), zdir.rglob("*.zot"), zdir.rglob("*.zoq")
    )


def flatten_h1_notes(h1s: Iterable[Any]) -> list[Any]:
    """Flattens the notes contained in a list of domain/SQL H1 sections."""
    notes = []
    blocks = []
    for h1 in h1s:
        blocks.extend(h1.blocks)
        for h2 in h1.h2s:
            blocks.extend(h2.blocks)
            for h3 in h2.h3s:
                blocks.extend(h3.blocks)
                for h4 in h3.h4s:
                    blocks.extend(h4.blocks)
    for block in blocks:
        notes.extend(block.notes)
    return notes


def _var_map_value(value: str) -> Any:
    if re.match("^[0-9]{4}[01][0-9][0-3][0-9]$", value):
        return dt.datetime.strptime(value, "%Y%m%d")
    return value
