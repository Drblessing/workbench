import pytest
from py_src.missing_integer import missing_int


def test_missing_int():
    # Test with a list that has a missing integer
    assert missing_int([0, 1, 2, 4]) == 3

    # Test with a list that doesn't have a missing integer
    assert missing_int([0, 1, 2, 3, 4]) == 5

    # Test with a list that has multiple missing integers
    assert missing_int([0, 1, 3, 4]) == 2

    # Test with an empty list
    assert missing_int([]) == 0

    # Test with a list that contains one element
    assert missing_int([1]) == 0

    # Test with a list that contains negative integers
    assert missing_int([0, 1, 2]) == 3


if __name__ == "__main__":
    pytest.main()
