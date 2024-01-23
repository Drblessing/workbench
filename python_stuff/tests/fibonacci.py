# Fibonacci


def fib(n):
    """Return the nth fibonacci number."""
    # Check that the input is a positive integer
    if type(n) != int or n < 0:
        raise ValueError("n must be a positive integer")
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 2) + fib(n - 1)
