# factorial.py


def factorial(n):
    """Return the factorial of n."""
    # Check that the input is a positive integer using isinstance
    if not isinstance(n, int) or n < 0:
        raise ValueError("n must be a positive integer")

    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


if __name__ == "__main__":
    print(factorial(4))
