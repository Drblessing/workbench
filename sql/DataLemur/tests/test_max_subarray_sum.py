import pytest
from py_src.max_subarray_sum import max_subarray_sum


def test_max_subarray_sum():
    # Test with positive numbers
    assert max_subarray_sum([1, 2, 3, 4, 5]) == 15

    # Test with negative numbers
    assert max_subarray_sum([-1, -2, -3, -4, -5]) == 0

    # Test with a mix of positive and negative numbers
    assert max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6

    # Test with a single positive number
    assert max_subarray_sum([5]) == 5

    # Test with a single negative number
    assert max_subarray_sum([-5]) == 0

    # Test with zero
    assert max_subarray_sum([0]) == 0

    # Test with an empty list
    with pytest.raises(ValueError):
        max_subarray_sum([])

    # Test with non-list input
    with pytest.raises(TypeError):
        max_subarray_sum("not a list")


if __name__ == "__main__":
    pytest.main()
