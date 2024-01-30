import pytest

from py_src.factorial_trailing_zeros import trailing_zeroes


def test_trailing_zeroes():
    # Test with positive numbers
    assert trailing_zeroes(5) == 1
    assert trailing_zeroes(10) == 2
    assert trailing_zeroes(25) == 6
    # Test with zero
    assert trailing_zeroes(0) == 0
    # Test with negative numbers
    with pytest.raises(ValueError):
        trailing_zeroes(-5)
    # Test with non-integer input
    with pytest.raises(TypeError):
        trailing_zeroes(5.5)
    with pytest.raises(TypeError):
        trailing_zeroes("5")


if __name__ == "__main__":
    pytest.main()
