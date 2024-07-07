"""Contains runners for the 'zorg edit' command."""

from zorg.app.config import EditConfig
from zorg.domain.messages import commands
from zorg.service import messagebus
from zorg.service.common import prepend_zdir
from zorg.service.file_groups import expand_file_group_paths
from zorg.service.templates import init_from_template

from ._runners import runner


@runner
def run_edit(cfg: EditConfig) -> int:
    """Runner for the 'edit' command."""
    zo_paths = expand_file_group_paths(
        cfg.zo_paths, file_group_map=cfg.file_group_map
    )
    zo_paths = prepend_zdir(cfg.zettel_dir, zo_paths)
    for zo_path in zo_paths:
        init_from_template(cfg.zettel_dir, cfg.template_pattern_map, zo_path)

    messagebus.handle(
        cfg.zettel_dir,
        cfg.database_url,
        [
            commands.EditCommand(
                keep_alive_file=cfg.keep_alive_file,
                paths=zo_paths,
                verbose=cfg.verbose,
                vim_commands=cfg.vim_commands,
                zettel_dir=cfg.zettel_dir,
            ),
        ],
        verbose=cfg.verbose,
    )
    return 0
