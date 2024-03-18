"""Contains this project's clack runners."""

from ._registry import RUNNERS
from . import _run_action, _run_compile, _run_db, _run_edit, _run_template

del _run_action, _run_compile, _run_db, _run_edit, _run_template

__all__ = ["RUNNERS"]
