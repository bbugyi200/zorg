"""Logic for dealing with (e.g. expanding) file groups lives here."""

import datetime as dt
from pathlib import Path
from typing import Iterable, Sequence

from typist import PathLike

from ..domain.types import FileGroupMapType


# TODO(bugyi): See if you can reduce complexity between this and _paths_from_file_group()
def expand_file_group_paths(
    zo_paths: Iterable[PathLike],
    *,
    file_group_map: FileGroupMapType,
) -> list[Path]:
    """Expands any file group names in {zo_paths} into the appropriate files.

    Args:
        zo_paths: The initial set of file paths and/or file group names.
        file_group_map: A mapping from file group names to sets of file paths.

    Returns:
        A new list of paths constructed from {zo_paths} with all file group
        names replaced with the appropriate set of file paths.
    """
    new_zo_paths = []
    for zo_path in zo_paths:
        if str(zo_path).startswith("@"):
            group_name = str(zo_path)[1:]
            file_group = file_group_map[group_name]
            new_zo_paths.extend(
                _paths_from_file_group(file_group, file_group_map)
            )
        else:
            new_zo_paths.append(Path(zo_path))
    return new_zo_paths


def _paths_from_file_group(
    file_group: Sequence[str], file_group_map: FileGroupMapType
) -> list[Path]:
    today = dt.datetime.now()
    yyyymmdd = []
    days = []
    for i in range(7):
        date = today - dt.timedelta(days=i)
        days.append(date)
        yyyymmdd.append(date.strftime("%Y%m%d"))

    paths = []
    for fname in file_group:
        if fname.startswith("@"):
            paths.extend(
                expand_file_group_paths(
                    [Path(fname)], file_group_map=file_group_map
                )
            )
        else:
            paths.append(Path(fname.format(days=days, yyyymmdd=yyyymmdd)))
    return paths
