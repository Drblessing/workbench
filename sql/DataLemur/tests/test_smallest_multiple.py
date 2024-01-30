import pytest
from py_src.smallest_multiple import smallest_multiple


def test_smallest_multiple():
    # Test with small numbers
    assert smallest_multiple(1) == 1
    assert smallest_multiple(2) == 2
    assert smallest_multiple(3) == 6
    assert smallest_multiple(4) == 12
    assert smallest_multiple(5) == 60

    # Test with larger numbers
    assert smallest_multiple(10) == 2520

    # Test with non-integer input
    with pytest.raises(TypeError):
        smallest_multiple(1.5)

    # Test with negative input
    with pytest.raises(ValueError):
        smallest_multiple(-1)


if __name__ == "__main__":
    pytest.main()
