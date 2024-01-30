def largest_prime_factor(target: int) -> int:
    """Returns the largest prime factor of target."""

    # Check that target is an integer
    if not isinstance(target, int):
        raise TypeError("target must be an integer.")

    # Check that target is positive
    if target < 1:
        raise ValueError("target must be positive.")

    # Find the largest prime factor of target
    # Start with 2
    i = 2
    # Only iterate whil  i * i <= target,
    # because if i * i > target, then target is prime.
    while i * i <= target:
        # If target is divisible by i, then divide target by i.
        # Otherwise, increment i.
        if (target % i) != 0:
            i += 1
        else:
            target //= i
    # Return the largest prime factor of target
    return target
