def gcd(a: int, b: int) -> int:
    """Compute the greatest common divisor of a and b"""
    while b > 0:
        a, b = b, a % b
    return a


def lcm(a: int, b: int) -> int:
    """Compute the lowest common multiple of a and b"""
    return a * b // gcd(a, b)


def smallest_multiple(n: int) -> int:
    """Compute the lcm of all numbers from 1 to n."""

    # Type check
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    if n < 1:
        raise ValueError("n must be positive")

    # Compute the lcm of all numbers from 1 to n
    lcm_all = 1
    for i in range(1, n + 1):
        lcm_all = lcm(lcm_all, i)
    return lcm_all
