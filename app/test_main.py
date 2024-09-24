import pytest
from app.main import is_isogram


@pytest.mark.parametrize("word, expected", [
    ("playgrounds", True),
    ("look", False),
    ("Adam", False),
    ("", True),
    ("AaBbCc", False),
    ("JavaScript", False),
    ("Mississippi", False)
])
def test_is_isogram(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected
