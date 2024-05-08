"""Helper logic that is shared broadly across this package."""

import datetime as dt
from pathlib import Path
import re
import sys
from typing import Any, Iterable

import rich
from typist import PathLike

from ..domain.types import Color, VarMapType


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
    bg = bg_color.to_rich_spec()
    fg = fg_color.to_rich_spec()

    # print final message
    contents = f"{space_call_count} | {hhmmss} | {msg}"
    rich.print(f"[{style} {fg} on {bg}]{contents}[/]")

    # set call count
    setattr(zprint, call_count_attr, call_count + 1)


def zinput(prompt: str) -> str:
    """Custom input() wrapper used by Zorg."""
    print(prompt, file=sys.stderr, end="")
    return input()


def _var_map_value(value: str) -> Any:
    if re.match("^[0-9]{4}[01][0-9][0-3][0-9]$", value):
        return dt.datetime.strptime(value, "%Y%m%d")
    return value
