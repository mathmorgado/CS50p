from bank import greeting
import pytest


def test_hello_argument():
    assert greeting("hello Powder") == "$0"


def test_h_argument():
    assert greeting("hi Powder") == "$20"
    assert greeting("hey Powder") == "$20"
    assert greeting("how are you?") == "$20"


def test_non_h_argument():
    assert greeting("what's up") == "$100"
    assert greeting("good morning") == "$100"


def test_lowercase_argument():
    assert greeting("hello Powder") == "$0"
    assert greeting("hi Powder") == "$20"
    assert greeting("what's up Powder") == "$100"


def test_uppercase_argument():
    assert greeting("HELLO POWDER") == "$0"
    assert greeting("HI POWDER") == "$20"
    assert greeting("WHAT'S UP POWDER") == "$100"
    assert greeting("WHAT'S UP POWDER") == "$100"


def test_punctuation_argument():
    assert greeting("hello, POWDER") == "$0"
    assert greeting("hi! POWDER") == "$20"


def test_non_str_argument():
    with pytest.raises(TypeError, match="Greet must be a string"):
        greeting(123)
