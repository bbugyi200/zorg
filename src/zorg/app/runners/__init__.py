"""Contains this project's clack runners.

WARNING: This package should contain modules of the form _runners.py or
         _run_*.py ONLY. Do NOT be tempted to add other libraries to this
         package even if they are only used by runners.
"""

from . import (
    _run_action,
    _run_compile,
    _run_db,
    _run_edit,
    _run_query,
    _run_template,
)
from ._runners import RUNNERS


# HACK: It is necessary that we import these runner modules so the '@runner'
# decorator registers functions as runners.
del _run_action, _run_compile, _run_db, _run_edit, _run_query, _run_template

__all__ = ["RUNNERS"]
