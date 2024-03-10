"""This file contains shared fixtures and pytest hooks.

https://docs.pytest.org/en/6.2.x/fixture.html#conftest-py-sharing-fixtures-across-multiple-files

"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Iterator

from freezegun import freeze_time
from pytest import fixture

from zorg.__main__ import main as zorg_main

from . import common as c


pytest_plugins = ["clack.pytest_plugin", "vimala.pytest_plugin"]


if TYPE_CHECKING:  # fixes pytest warning
    from clack.pytest_plugin import MakeConfigFile


@fixture
def main(make_config_file: MakeConfigFile) -> c.MainType:
    """Returns a wrapper around zorg's main() function."""

    def inner_main(*args: str, **kwargs: Any) -> int:
        cfg_kwargs = {
            k: v if isinstance(v, (dict, list)) else str(v)
            for (k, v) in kwargs.items()
        }

        config_file = make_config_file("zorg_test_config", **cfg_kwargs)
        argv = ["zorg", "-c", str(config_file.path)] + list(args)
        return zorg_main(argv)

    return inner_main


@fixture(autouse=True, scope="session")
def frozen_time() -> Iterator[None]:
    """Freeze time until our tests are done running."""
    with freeze_time(f"{c.TODAY}T{c.hh}:{c.mm}:00.123456Z"):
        yield
