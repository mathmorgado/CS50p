from plates import is_valid
import pytest


def test_plate_size():
    assert is_valid("AB") == True
    assert is_valid("ABCDEF") == True
    assert is_valid("ABCD") == True
    assert is_valid("") == False
    assert is_valid("A") == False
    assert is_valid("ABCDEFG") == False


def test_beginning_alphabetical():
    assert is_valid("AB1") == True
    assert is_valid("12") == False
    assert is_valid("3B") == False
    assert is_valid("A5") == False


def test_first_digit():
    assert is_valid("ABC0") == False
    assert is_valid("ABC1") == True


def test_just_digits_after():
    assert is_valid("ABC123") == True
    assert is_valid("ABC12C") == False
    assert is_valid("ABC1C2") == False


def test_invalid_char():
    assert is_valid("AB!") == False
    assert is_valid("AB#") == False
    assert is_valid("AB.") == False
    assert is_valid("AB,") == False
    assert is_valid("AB?") == False
    assert is_valid("AB$") == False
    assert is_valid("AB@") == False
    assert is_valid("AB&") == False
    assert is_valid("AB*") == False
    assert is_valid("AB;") == False
    assert is_valid("AB:") == False
    assert is_valid("AB ") == False


def test_non_str():
    with pytest.raises(TypeError):
        is_valid(123) == False
