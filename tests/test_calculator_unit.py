from quickcalc.calculator import add, subtract, multiply, divide
import pytest


def test_add():
    assert add(5, 3) == 8


def test_subtract():
    assert subtract(10, 4) == 6


def test_multiply():
    assert multiply(6, 7) == 42


def test_divide():
    assert divide(8, 2) == 4


# Edge Cases

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(5, 0)


def test_negative_numbers():
    assert add(-5, -2) == -7


def test_decimal_numbers():
    assert round(add(0.1, 0.2), 1) == 0.3


def test_large_numbers():
    assert multiply(10**6, 10**6) == 10**12