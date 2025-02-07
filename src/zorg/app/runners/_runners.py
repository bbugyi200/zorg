"""Contains the RUNNERS list and @runner annotation.

The RUNNERS list will eventually hold all runner functions, each of which
should be marked as a runner using the @runner annotation.
"""

import metaman
from clack.types import ClackRunner

RUNNERS: list[ClackRunner] = []
runner = metaman.register_function_factory(RUNNERS)
