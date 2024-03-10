"""Helper logic that is shared broadly across this package."""

import datetime as dt
import re
from typing import Any

from .types import VarMapType


def process_var_map(var_map: VarMapType) -> dict[str, Any]:
    """Processes and potentially adds to {var_map}."""
    new_var_map = {}
    for k, v in var_map.items():
        new_var_map[k] = _var_map_value(v)
    if any(isinstance(v, dt.datetime) for v in new_var_map.values()):
        new_var_map["one_day"] = dt.timedelta(days=1)
    return new_var_map


def _var_map_value(value: str) -> Any:
    if re.match("^[0-9]{4}[01][0-9][0-3][0-9]$", value):
        return dt.datetime.strptime(value, "%Y%m%d")
    return value
