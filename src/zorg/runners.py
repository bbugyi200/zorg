"""Contains this project's clack runners."""

from __future__ import annotations

import datetime as dt
from functools import partial
from pathlib import Path
from typing import Iterable, Iterator, List

from clack.types import ClackRunner
import jinja2
from logrus import Logger
import metaman
import vimala

from .config import DayConfig


RUNNERS: List[ClackRunner] = []
runner = metaman.register_function_factory(RUNNERS)

logger = Logger(__name__)


@runner
def run_day(cfg: DayConfig) -> int:
    """Runner for the 'day' command."""
    template_loader = jinja2.FileSystemLoader(searchpath=cfg.zettel_dir)
    template_env = jinja2.Environment(loader=template_loader)
    day_log_template = template_env.get_template(cfg.day_log_template)
    habit_log_template = template_env.get_template(cfg.habit_log_template)
    done_log_template = template_env.get_template(cfg.done_log_template)

    today = dt.datetime.now()
    two_days_ago = today - dt.timedelta(days=2)
    yesterday = today - dt.timedelta(days=1)
    tomorrow = today + dt.timedelta(days=1)

    day_log_vars = {
        "two_days_ago": two_days_ago,
        "yesterday": yesterday,
        "today": today,
        "tomorrow": tomorrow,
    }
    day_log_contents = day_log_template.render(day_log_vars)
    done_log_contents = done_log_template.render(day_log_vars)
    habit_log_contents = habit_log_template.render(day_log_vars)

    ensureDayLogFileExists = partial(_ensureDayLogFileExists, cfg.zettel_dir)
    day_log_path = ensureDayLogFileExists(day_log_contents, today)
    ensureDayLogFileExists(habit_log_contents, yesterday, suffix="habit")
    ensureDayLogFileExists(done_log_contents, today, suffix="done")

    if cfg.edit_day_log:
        vimala.vim(
            day_log_path,
            commands=_process_vim_commands(cfg.zettel_dir, cfg.vim_commands),
        )
    return 0


def _ensureDayLogFileExists(
    zettel_dir: Path, contents: str, date: dt.date, *, suffix: str = None
) -> Path:
    path = _get_day_path(zettel_dir, date, suffix=suffix)
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.exists():
        path.write_text(contents)
    return path


def _get_day_path(
    zettel_dir: Path, date: dt.date, *, suffix: str = None
) -> Path:
    suffix = f"_{suffix}" if suffix else ""
    return zettel_dir / str(date.year) / date.strftime(f"%Y%m%d{suffix}.zo")


def _process_vim_commands(
    zettel_dir: Path, vim_commands: Iterable[str]
) -> Iterator[str]:
    for vim_cmd in vim_commands:
        if "{zdir}" in vim_cmd:
            yield vim_cmd.format(zdir=zettel_dir)
        else:
            yield vim_cmd
