import pytest

from py_src.max_trading_stocks import max_subarray_sum


def test_max_subarray_sum():
    # Test with increasing prices
    assert max_subarray_sum([1, 2, 3, 4, 5]) == 4
    # Test with decreasing prices
    assert max_subarray_sum([5, 4, 3, 2, 1]) == 0
    # Test with fluctuating prices
    assert max_subarray_sum([3, 2, 6, 5, 0, 3]) == 4
    # Test with all prices the same
    assert max_subarray_sum([3, 3, 3, 3, 3]) == 0
    # Test with empty list
    assert max_subarray_sum([]) == 0
    # Test with single price
    assert max_subarray_sum([3]) == 0
    # Test with two prices
    assert max_subarray_sum([2, 3]) == 1
    assert max_subarray_sum([3, 2]) == 0


if __name__ == "__main__":
    pytest.main()
