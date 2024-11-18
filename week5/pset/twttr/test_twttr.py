from twttr import shorten
import pytest


def test_empty():
    assert shorten("") == ""


def test_lowercase_vogals():
    assert shorten("hello world") == "hll wrld"


def test_uppercase_vogals():
    assert shorten("HELLO WORLD") == "HLL WRLD"


def test_str_numbers():
    assert shorten("123") == "123"


def test_punctuation():
    assert shorten("!,#$.") == "!,#$."


def test_non_str():
    with pytest.raises(TypeError, match="'int' object is not iterable"):
        shorten(123)
