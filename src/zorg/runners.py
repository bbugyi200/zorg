"""Contains this project's clack runners."""

from __future__ import annotations

import datetime as dt
from pathlib import Path
from typing import Iterable, Iterator, List

from clack.types import ClackRunner
import jinja2
from logrus import Logger
import metaman
import vimala

from .config import EditConfig


RUNNERS: List[ClackRunner] = []
runner = metaman.register_function_factory(RUNNERS)

logger = Logger(__name__)


@runner
def run_edit(cfg: EditConfig) -> int:
    """Runner for the 'edit' command."""
    template_loader = jinja2.FileSystemLoader(searchpath=cfg.zettel_dir)
    template_env = jinja2.Environment(loader=template_loader)
    template = template_env.get_template(cfg.day_log_template)
    habit_template = template_env.get_template(cfg.habit_template)
    done_template = template_env.get_template(cfg.done_template)

    today = dt.datetime.now()
    yesterday = today - dt.timedelta(days=1)
    two_days_ago = today - dt.timedelta(days=2)
    tomorrow = today + dt.timedelta(days=1)

    day_log_vars = {
        "year": str(today.year),
        "month": f"{today.month:02d}",
        "day": f"{today.day:02d}",
        "weekday": today.strftime("%a"),
        "yesterday": yesterday.strftime("%Y%m%d"),
        "tomorrow": tomorrow.strftime("%Y%m%d"),
    }
    day_log_contents = template.render(day_log_vars)
    done_log_contents = done_template.render(day_log_vars)
    habit_tracker_contents = habit_template.render(
        year=str(yesterday.year),
        month=f"{yesterday.month:02d}",
        day=f"{yesterday.day:02d}",
        weekday=yesterday.strftime("%a"),
        day_before=two_days_ago.strftime("%Y%m%d"),
        day_after=today.strftime("%Y%m%d"),
    )

    day_log_path = _get_day_path(cfg.zettel_dir, today)
    if not day_log_path.exists():
        day_log_path.write_text(day_log_contents)

    habit_tracker_path = _get_day_path(
        cfg.zettel_dir, yesterday, suffix="habit"
    )
    if not habit_tracker_path.exists():
        habit_tracker_path.write_text(habit_tracker_contents)

    done_log_path = _get_day_path(cfg.zettel_dir, today, suffix="done")
    if not done_log_path.exists():
        done_log_path.write_text(done_log_contents)

    vimala.vim(
        day_log_path,
        commands=_process_vim_commands(cfg.zettel_dir, cfg.vim_commands),
    )
    return 0


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
