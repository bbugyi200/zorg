"""Unit tests for zorg.service.note_utils service logic."""

from typing import Final

from pytest import mark, param

from zorg.service.note_utils import _note_body_has_tag

params = mark.parametrize
fat_pig_body: Final = (
    "P0 240704 240701#00 Hey there @MR +pig. You are age::11 years old and are"
    " [body_desc:: fat and ugly]."
)


@params(
    "body,word,expected",
    [
        param(fat_pig_body, "+pig", True, id="+pig"),
        param(fat_pig_body, "+thin", False, id="+thin"),
    ],
)
def test_note_body_has_tag(body: str, word: str, expected: bool) -> None:
    """Flexes the _note_body_has_tag() function."""
    assert _note_body_has_tag(body, word) == expected
