import pytest
from py_src.salary_inequity import min_inequity


def test_min_inequity():
    # Test with a list of salaries and a number of choices that results in a non-zero inequity
    assert min_inequity([1, 5, 3, 4, 2], 3) == 2

    # Test with a list of salaries and a number of choices that results in a zero inequity
    assert min_inequity([1, 2, 3, 4, 5], 1) == 0

    # Test with a list of identical salaries
    assert min_inequity([2, 2, 2, 2, 2], 3) == 0

    # Test with a list of salaries and a number of choices equal to the length of the list
    assert min_inequity([1, 5, 3, 4, 2], 5) == 4

    # Test with a list of salaries in descending order
    assert min_inequity([5, 4, 3, 2, 1], 3) == 2

    # Test with a list of salaries in ascending order
    assert min_inequity([1, 2, 3, 4, 5], 3) == 2


if __name__ == "__main__":
    pytest.main()
