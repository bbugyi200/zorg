"""zorg.service.swog

(S)ELECT
(W)HERE
(O)RDER BY
(G)ROUP BY

Serves as a data pipeline used to execute zorg queries.
"""

from ._executor import execute


__all__ = ["execute"]
