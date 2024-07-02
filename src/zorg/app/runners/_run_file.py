"""Contains runners for the 'zorg file' command."""

from logrus import Logger

from ...service import common as c
from ..config import FileRenameConfig
from ._runners import runner


_LOGGER = Logger(__name__)


@runner
def run_file_rename(cfg: FileRenameConfig) -> int:
    src_name = cfg.src_name if "." in cfg.src_name else cfg.src_name + ".zo"
    dest_name = (
        cfg.dest_name if "." in cfg.dest_name else cfg.dest_name + ".zo"
    )
    src_path = c.prepend_zdir(cfg.zettel_dir, [src_name])[0]
    dest_path = c.prepend_zdir(cfg.zettel_dir, [dest_name])[0]
    src_path.rename(dest_path)
    _LOGGER.info(
        "Moved file", src_path=str(src_path), dest_path=str(dest_path)
    )

    src_link_name = c.simplify_fname(cfg.zettel_dir, cfg.src_name)
    dest_link_name = c.simplify_fname(cfg.zettel_dir, cfg.dest_name)
    link_map = {
        f"[[{src_link_name}]": f"[[{dest_link_name}]",
        f"[[{src_link_name}#": f"[[{dest_link_name}#",
    }
    for zpath in c.get_all_zfiles(cfg.zettel_dir):
        zcontents = zpath.read_text()
        if not any(src_str in zcontents for src_str in link_map):
            _LOGGER.debug("Skipping file that has no links", file=str(zpath))
            continue

        new_zcontents = zcontents
        _LOGGER.info("Replacing links found in file", file=str(zpath))
        for old_link, new_link in link_map.items():
            new_zcontents = new_zcontents.replace(old_link, new_link)
        zpath.write_text(new_zcontents)
    return 0
