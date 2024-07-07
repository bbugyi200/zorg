"""zorg.service.compiler

Provides functions that help with compiling custom zorg grammars (e.g. zorg
queries or zorg files).
"""

from ._api import build_zorg_query, walk_zorg_file


__all__ = ["build_zorg_query", "walk_zorg_file"]
