import pytest

from py_src.fizz_buzz_sum import fizz_buzz_sum


def test_fizz_buzz_sum():
    assert (
        fizz_buzz_sum(10) == 23
    )  # The sum of numbers divisible by 3 or 5 below 10 is 23
    assert fizz_buzz_sum(0) == 0  # The sum below 0 should be 0
    assert fizz_buzz_sum(1) == 0  # The sum below 1 should be 0
    assert fizz_buzz_sum(5) == 3  # The sum of numbers divisible by 3 or 5 below 5 is 3
    assert (
        fizz_buzz_sum(6) == 8
    )  # The sum of numbers divisible by 3 or 5 below 6 is 8 (3+5)
    assert (
        fizz_buzz_sum(100) == 2318
    )  # The sum of numbers divisible by 3 or 5 below 100 is 2318


if __name__ == "__main__":
    pytest.main()
