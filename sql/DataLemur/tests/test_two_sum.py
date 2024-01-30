import pytest
from py_src.two_sum import two_sum


def test_two_sum():
    # Test with positive numbers
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]
    assert two_sum([3, 2, 4], 6) == [1, 2]
    assert two_sum([3, 3], 6) == [0, 1]

    # Test with negative numbers
    assert two_sum([-1, -2, -3, -4, -5], -8) == [2, 4]

    # Test with no solution
    assert two_sum([1, 2, 3, 4, 5], 10) == [-1, -1]

    # Test with non-integer target
    with pytest.raises(TypeError):
        two_sum([1, 2, 3, 4, 5], "10")

    # Test with non-list input
    with pytest.raises(TypeError):
        two_sum("12345", 10)

    # Test with less than two elements in input
    with pytest.raises(ValueError):
        two_sum([1], 1)
    with pytest.raises(ValueError):
        two_sum([], 0)


if __name__ == "__main__":
    pytest.main()
