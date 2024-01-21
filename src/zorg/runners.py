"""Contains this project's clack runners."""

from __future__ import annotations

import datetime as dt
from functools import partial
from pathlib import Path
import tempfile
from typing import Iterable, Iterator

from clack.types import ClackRunner
import jinja2
from logrus import Logger
import metaman
import vimala

from .config import DayConfig


RUNNERS: list[ClackRunner] = []
runner = metaman.register_function_factory(RUNNERS)

logger = Logger(__name__)


@runner
def run_day(cfg: DayConfig) -> int:
    """Runner for the 'day' command."""
    temp_dir = tempfile.TemporaryDirectory()
    temp_dir_path = Path(temp_dir.name)
    template_loader = jinja2.FileSystemLoader(searchpath=temp_dir_path)
    template_env = jinja2.Environment(loader=template_loader)
    _build_template_in_dir(
        temp_dir_path, cfg.zettel_dir / cfg.day_log_template
    )
    _build_template_in_dir(
        temp_dir_path, cfg.zettel_dir / cfg.habit_log_template
    )
    _build_template_in_dir(
        temp_dir_path, cfg.zettel_dir / cfg.done_log_template
    )
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

    ensureDailyLogFileExists = partial(
        _ensureDailyLogFileExists, cfg.zettel_dir
    )
    day_log_path = ensureDailyLogFileExists(day_log_contents, today)
    ensureDailyLogFileExists(habit_log_contents, yesterday, suffix="habit")
    ensureDailyLogFileExists(done_log_contents, today, suffix="done")

    if cfg.edit_day_log:
        vimala.vim(
            day_log_path,
            commands=_process_vim_commands(cfg.zettel_dir, cfg.vim_commands),
        )
    return 0


def _build_template_in_dir(temp_dir: Path, template_path: Path) -> None:
    temp_template_path = temp_dir / template_path.name
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


def _ensureDailyLogFileExists(
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


def _process_vim_commands(
    zettel_dir: Path, vim_commands: Iterable[str]
) -> Iterator[str]:
    for vim_cmd in vim_commands:
        if "{zdir}" in vim_cmd:
            yield vim_cmd.format(zdir=zettel_dir)
        else:
            yield vim_cmd
