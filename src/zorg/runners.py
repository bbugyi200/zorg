"""Contains this project's clack runners."""

from __future__ import annotations

from dataclasses import dataclass
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

from .config import EditConfig


RUNNERS: list[ClackRunner] = []
runner = metaman.register_function_factory(RUNNERS)

logger = Logger(__name__)


@runner
def run_edit(cfg: EditConfig) -> int:
    """Runner for the 'edit' command."""
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
    past_present_future = _get_past_present_future(today, 2, 2)
    day_log_vars = {
        "dates": past_present_future,
    }
    day_log_contents = day_log_template.render(day_log_vars)
    done_log_contents = done_log_template.render(day_log_vars)
    habit_log_contents = habit_log_template.render(day_log_vars)

    ensure_daily_log_file_exists = partial(
        _ensure_daily_log_file_exists, cfg.zettel_dir
    )
    day_log_path = ensure_daily_log_file_exists(day_log_contents, today)
    ensure_daily_log_file_exists(
        habit_log_contents, past_present_future.past[0], suffix="habit"
    )
    ensure_daily_log_file_exists(done_log_contents, today, suffix="done")

    if cfg.edit_day_log:
        vimala.vim(
            day_log_path,
            commands=_process_vim_commands(cfg.zettel_dir, cfg.vim_commands),
        )
    return 0


@dataclass(frozen=True)
class _PastPresentFuture:
    past: list[dt.datetime]
    present: dt.datetime
    future: list[dt.datetime]

    @property
    def yesterday(self) -> dt.datetime:
        return self.past[0]

    @property
    def today(self) -> dt.datetime:
        return self.present

    @property
    def tomorrow(self) -> dt.datetime:
        return self.future[0]


def _get_past_present_future(
    present: dt.datetime, past_count: int, future_count: int
) -> _PastPresentFuture:
    past = []
    for p in range(past_count):
        past.append(present - dt.timedelta(days=p + 1))

    future = []
    for f in range(future_count):
        future.append(present + dt.timedelta(days=f + 1))

    return _PastPresentFuture(past, present, future)


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


def _process_vim_commands(
    zettel_dir: Path, vim_commands: Iterable[str]
) -> Iterator[str]:
    for vim_cmd in vim_commands:
        if "{zdir}" in vim_cmd:
            yield vim_cmd.format(zdir=zettel_dir)
        else:
            yield vim_cmd
