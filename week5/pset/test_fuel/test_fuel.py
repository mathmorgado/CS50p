from fuel import convert, gauge
import pytest


def test_gauge():
    assert gauge(99) == "F"
    assert gauge(43) == "43%"
    assert gauge(1) == "E"


def test_convert():
    assert convert("2/2") == 100
    assert convert("3/7") == 43
    assert convert("0/2") == 0


def test_convert_x_greater_then_y():
    with pytest.raises(ValueError):
        convert("4/3")


def test_convert_y_equal_0():
    with pytest.raises(ZeroDivisionError):
        convert("2/0")


def test_convert_non_integer():
    with pytest.raises(ValueError):
        convert("2.3/3")


def test_convert_non_fraction():
    with pytest.raises(ValueError):
        convert("cat")
        convert(12)
