from convert import convert
import pytest


def test_zero_argument():
    assert convert(0) == 0


def test_argument():
    assert convert(7) == 1047185094900.0


def test_float_argument():
    assert convert(3.3) == 493672973310.0


def test_string_argument():
    with pytest.raises(TypeError, match="au must be an integer or float"):
        convert("cat")
