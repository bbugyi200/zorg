"""Contains this project's clack runners."""

from __future__ import annotations

import datetime as dt
from functools import partial
from pathlib import Path
import tempfile
from typing import Any, Iterable, Iterator

from clack.types import ClackRunner
import jinja2
from logrus import Logger
import metaman
import vimala

from .config import Config, EditConfig, NewConfig


RUNNERS: list[ClackRunner] = []
runner = metaman.register_function_factory(RUNNERS)

logger = Logger(__name__)


@runner
def run_edit(cfg: EditConfig) -> int:
    """Runner for the 'edit' command."""
    tmpl_manager = _ZorgTemplateManager(cfg)

    today = dt.datetime.now()
    yesterday = today - dt.timedelta(days=1)

    day_log_contents = tmpl_manager.render(
        cfg.day_log_template, _date_var_map(today)
    )
    done_log_contents = tmpl_manager.render(
        cfg.done_log_template, _date_var_map(today)
    )
    habit_log_contents = tmpl_manager.render(
        cfg.habit_log_template, _date_var_map(yesterday)
    )

    ensure_daily_log_file_exists = partial(
        _ensure_daily_log_file_exists, cfg.zettel_dir
    )
    day_log_path = ensure_daily_log_file_exists(day_log_contents, today)
    ensure_daily_log_file_exists(habit_log_contents, yesterday, suffix="habit")
    ensure_daily_log_file_exists(done_log_contents, today, suffix="done")

    if cfg.edit_day_log:
        vimala.vim(
            day_log_path,
            commands=_process_vim_commands(cfg.zettel_dir, cfg.vim_commands),
        )
    return 0


def _date_var_map(date: dt.datetime) -> dict[str, Any]:
    return {"date": date, "one_day": dt.timedelta(days=1)}


@runner
def run_new(cfg: NewConfig) -> int:
    """Runner for the 'new' command."""
    tmpl_manager = _ZorgTemplateManager(cfg)
    print(tmpl_manager.render(cfg.template, cfg.var_map))
    return 0


class _ZorgTemplateManager:
    tmp_dir = tempfile.TemporaryDirectory()

    def __init__(self, cfg: Config) -> None:
        tmp_dir_path = Path(self.tmp_dir.name)
        loader = jinja2.FileSystemLoader(searchpath=tmp_dir_path)

        self._temp_dir_path = tmp_dir_path
        self._template_env = jinja2.Environment(loader=loader)
        self._cfg = cfg

    def render(self, template_path: Path, var_map: dict[str, Any]) -> str:
        """Renders {template_path} using {var_map} for template variables."""
        self._build_template_in_dir(
            self._temp_dir_path, self._cfg.zettel_dir / template_path
        )
        template = self._template_env.get_template(template_path.name)
        return template.render(var_map)

    @classmethod
    def _build_template_in_dir(
        cls, tmp_dir: Path, template_path: Path
    ) -> None:
        temp_template_path = tmp_dir / template_path.name
        new_lines = []
        blank_line_found = False
        for line in template_path.open("r"):
            if not blank_line_found and not line.strip():
                blank_line_found = True
                continue
            if blank_line_found:
                new_lines.append(
                    line[1:]
                    if line.startswith("## ") or line.strip() == "##"
                    else line
                )
        temp_template_path.write_text("".join(new_lines))


def _ensure_daily_log_file_exists(
    zettel_dir: Path, contents: str, date: dt.date, *, suffix: str = None
) -> Path:
    path = _get_day_path(zettel_dir, date, suffix=suffix)
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.exists():
        logger.info(
            "Constructing new day log file from template", path=str(path)
        )
        path.write_text(contents)
    return path


def _get_day_path(
    zettel_dir: Path, date: dt.date, *, suffix: str = None
) -> Path:
    suffix = f"_{suffix}" if suffix else ""
    return zettel_dir / str(date.year) / date.strftime(f"%Y%m%d{suffix}.zo")


# TODO(bugyi): Move to config.py?
def _process_vim_commands(
    zettel_dir: Path, vim_commands: Iterable[str]
) -> Iterator[str]:
    for vim_cmd in vim_commands:
        if "{zdir}" in vim_cmd:
            yield vim_cmd.format(zdir=zettel_dir)
        else:
            yield vim_cmd
