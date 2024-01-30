import pytest
from py_src.contains_duplicate import contains_duplicate


def test_contains_duplicate():
    # Test with a list that contains duplicates
    assert contains_duplicate([1, 2, 3, 2]) == True

    # Test with a list that doesn't contain duplicates
    assert contains_duplicate([1, 2, 3, 4]) == False

    # Test with a list that contains multiple duplicates
    assert contains_duplicate([1, 1, 2, 2, 3, 3]) == True

    # Test with an empty list
    assert contains_duplicate([]) == False

    # Test with a list that contains one element
    assert contains_duplicate([1]) == False

    # Test with a list that contains two identical elements
    assert contains_duplicate([1, 1]) == True


if __name__ == "__main__":
    pytest.main()
