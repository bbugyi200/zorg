"""Helper logic that is shared broadly across this package."""

import datetime as dt
from pathlib import Path
import re
from typing import Any, Iterable

from typist import PathLike

from ..domain.types import VarMapType


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


def _var_map_value(value: str) -> Any:
    if re.match("^[0-9]{4}[01][0-9][0-3][0-9]$", value):
        return dt.datetime.strptime(value, "%Y%m%d")
    return value
