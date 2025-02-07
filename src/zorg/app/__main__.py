"""Contains the zorg package's main entry point."""

from __future__ import annotations

import clack

from zorg import APP_NAME
from zorg.app.config import clack_parser
from zorg.app.runners import RUNNERS

main = clack.main_factory(APP_NAME, parser=clack_parser, runners=RUNNERS)
if __name__ == "__main__":
    main()
