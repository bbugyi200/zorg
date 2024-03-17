"""Contains the RUNNERS list and @runner annotation.

The RUNNERS list will eventually hold all runner functions, each of which
should be marked as a runner using the @runner annotation.
"""

from clack.types import ClackRunner
import metaman


RUNNERS: list[ClackRunner] = []
runner = metaman.register_function_factory(RUNNERS)
