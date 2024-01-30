import pytest
from py_src.corr_coeff import corr


def test_corr():
    # Test with positive correlation
    assert corr([1, 3, 5, 7], [2, 4, 6, 8]) == 0.7500000000000001

    # Test with mismatched lengths
    with pytest.raises(ValueError):
        corr([1, 2, 3], [1, 2])

    # Test with empty vectors
    with pytest.raises(ValueError):
        corr([], [])


if __name__ == "__main__":
    pytest.main()
