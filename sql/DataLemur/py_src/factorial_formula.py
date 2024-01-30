def factorial(n: int) -> int:
    """Calculates the factorial of n."""

    if not isinstance(n, int):
        raise TypeError("n must be an integer.")
    elif n < 0:
        raise ValueError("n must be positive.")
    elif n == 0:
        return 1
    return n * factorial(n - 1)
