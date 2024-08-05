"""This file contains shared fixtures and pytest hooks.

https://docs.pytest.org/en/6.2.x/fixture.html#conftest-py-sharing-fixtures-across-multiple-files

"""

from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING, Any, Iterator

from _pytest.tmpdir import TempPathFactory
from freezegun import freeze_time
from pytest import fixture

from zorg.app.__main__ import main as zorg_main
from zorg.shared import common as c

from . import common as test_c


pytest_plugins = ["clack.pytest_plugin", "vimala.pytest_plugin"]


if TYPE_CHECKING:  # fixes pytest warning
    from clack.pytest_plugin import MakeConfigFile


@fixture
def local_zettel_dir(db_zettel_dir: Path) -> Path:
    """Returns a zettel directory that contains copies of all *.zo files."""
    return _get_zdir(db_zettel_dir)


@fixture(scope="session")
def zettel_dir(db_zettel_dir: Path) -> Path:
    """Returns a zettel directory that contains copies of all *.zo files."""
    return _get_zdir(db_zettel_dir)


@fixture(scope="session")
def db_zettel_dir(
    main: test_c.MainType, tmp_path_factory: TempPathFactory
) -> Path:
    """Returns zettel dir containing pre-initialized database.."""
    zdir = _get_zdir(tmp_path_factory.getbasetemp())
    assert main("--log=null", "--dir", str(zdir), "db", "create") == 0
    return zdir


@fixture(scope="session", name="main")
def main_fixture(make_config_file: MakeConfigFile) -> test_c.MainType:
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
    with freeze_time(f"{test_c.TODAY}T{test_c.hh}:{test_c.mm}:00.123456Z"):
        yield


def _get_zdir(tmp_path: Path) -> Path:
    zdir = tmp_path / "org"
    zdir.mkdir(exist_ok=True)
    for zo_path in _get_all_zo_paths():
        zettel_zo_path = zdir / zo_path.name
        zettel_zo_path.write_bytes(zo_path.read_bytes())
    return zdir


def _get_all_zo_paths() -> list[Path]:
    """Returns a list of Paths for all the *.zo[tq] files.

    These names will be relative to the zorg root directory.
    """
    zorg_root_dir = Path(__file__).parent.parent
    return list(c.get_all_zfiles(zorg_root_dir))
