import pytest
from py_src.intersection_of_two_lists import intersection


def test_intersection():
    # Test with two lists that have an intersection
    assert intersection([1, 2, 3, 4], [3, 4, 5, 6]) == [3, 4]

    # Test with two lists that have no intersection
    assert intersection([1, 2, 3, 4], [5, 6, 7, 8]) == []

    # Test with two lists that are identical
    assert intersection([1, 2, 3, 4], [1, 2, 3, 4]) == [1, 2, 3, 4]

    # Test with two empty lists
    assert intersection([], []) == []

    # Test with one empty list and one non-empty list
    assert intersection([], [1, 2, 3, 4]) == []

    # Test with two lists that have multiple intersecting elements
    assert intersection([1, 2, 2, 3, 4, 4], [2, 2, 4, 4, 5, 6]) == [2, 4]


if __name__ == "__main__":
    pytest.main()
