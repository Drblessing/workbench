def trailing_zeroes(n: int) -> int:
    """Calculates the factorial of n, then counts the trailing zeroes."""

    if not isinstance(n, int):
        raise TypeError("n must be an integer.")
    elif n < 0:
        raise ValueError("n must be positive.")

    # Calculate the factorial of n
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i

    # Count the trailing zeroes
    trailing_zeroes = 0
    while factorial % 10 == 0:
        trailing_zeroes += 1
        factorial //= 10

    # Return the number of trailing zeroes
    return trailing_zeroes
