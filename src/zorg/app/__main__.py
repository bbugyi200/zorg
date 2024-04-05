"""Contains the zorg package's main entry point."""

from __future__ import annotations

import clack

from .. import APP_NAME
from .config import clack_parser
from .runners import RUNNERS


main = clack.main_factory(APP_NAME, parser=clack_parser, runners=RUNNERS)
if __name__ == "__main__":
    main()
