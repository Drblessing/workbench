# test_fibonacci.py
import pytest

from fibonacci import (
    fib,
)  # Assuming your Fibonacci function is in a file named fibonacci.py


def test_fib_zero():
    assert fib(0) == 0, "Incorrect value for fib(0)"


def test_fib_one():
    assert fib(1) == 1, "Incorrect value for fib(1)"


def test_fib_five():
    assert fib(5) == 5, "Incorrect value for fib(5)"


def test_fib_ten():
    assert fib(10) == 55, "Incorrect value for fib(10)"


def test_fib_negative():
    # Assuming your function should handle negative numbers by raising an error
    # This test expects a ValueError for negative inputs

    with pytest.raises(ValueError):
        fib(-1)
