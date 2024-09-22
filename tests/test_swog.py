"""Unit tests for zorg.service.swog service logic."""

from pathlib import Path

from zorg.service.swog._saved_queries import expand_saved_queries


def test_expand_saved_queries__good(zettel_dir: Path) -> None:
    """Flexes the expand_saved_queries() service method."""
    foo_zoq_path = zettel_dir / "zoq/foo.zoq"
    bar_zoq_path = zettel_dir / "zoq/bar.zoq"
    baz_zoq_path = zettel_dir / "zoq/baz.zoq"
    foo_zoq_path.parent.mkdir()
    bar_where = "#foo +bar"
    baz_where = "@BAZ buz:*"
    foo_where = "o {bar} %bob {baz}"
    foo_zoq_path.write_text(f"# W {foo_where} G file")
    bar_zoq_path.write_text(f"# W {bar_where} O priority G file")
    baz_zoq_path.write_text(f"# W {baz_where} G priority file")

    actual_q = expand_saved_queries(zettel_dir, "W #fat {foo} O create G none")

    expected_q = f"W #fat o {bar_where} %bob {baz_where} O create G none"
    assert actual_q == expected_q


def test_expand_saved_queries__bad(zettel_dir: Path) -> None:
    """Flexes the expand_saved_queries() service method."""
    assert (
        expand_saved_queries(zettel_dir, "S count(+) W @CALL {does_not_exist}")
        is None
    )
