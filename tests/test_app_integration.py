import pytest
from quickcalc.app import calculate, clear


def test_full_user_flow_addition():
    # Simulate: enter 5, press +, enter 3, press =
    result = calculate(5, "+", 3)
    assert result == 8


def test_clear_resets_to_zero():
    # Simulate: after any calculation, pressing Clear resets display to 0
    _ = calculate(9, "*", 9)
    assert clear() == 0