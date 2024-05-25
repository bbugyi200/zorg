"""zorg.service.swog

(S)ELECT
(W)HERE
(O)RDER BY
(G)ROUP BY

Serves as a data pipeline used to execute zorg queries.
"""

from ._executor import execute
from ._zoq_file import refresh_zoq_file


__all__ = ["execute", "refresh_zoq_file"]
