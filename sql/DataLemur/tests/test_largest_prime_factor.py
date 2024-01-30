# FILEPATH: /Users/dbless/Github/sql/DataLemur/tests/test_largest_prime_factor.py

import pytest
from py_src.largest_prime_factor import largest_prime_factor


def test_largest_prime_factor():
    # Test with prime numbers
    assert largest_prime_factor(2) == 2
    assert largest_prime_factor(13) == 13
    assert largest_prime_factor(29) == 29

    # Test with composite numbers
    assert largest_prime_factor(4) == 2
    assert largest_prime_factor(15) == 5
    assert largest_prime_factor(100) == 5

    # Test with 1
    assert largest_prime_factor(1) == 1

    # Test with non-integer input
    with pytest.raises(TypeError):
        largest_prime_factor(1.5)

    # Test with negative input
    with pytest.raises(ValueError):
        largest_prime_factor(-1)


if __name__ == "__main__":
    pytest.main()
