def two_sum(input: list[int], target: int) -> list[int]:
    """Returns the indices of two integers in input that sum to target."""

    # Check that input is a list of integers
    if not isinstance(input, list):
        raise TypeError("input must be a list.")

    # Check that target is an integer
    if not isinstance(target, int):
        raise TypeError("target must be an integer.")

    # Check that input has at least two elements
    if len(input) < 2:
        raise ValueError("input must have at least two elements.")

    # Check that there are two elements in input that sum to target
    seen = {}
    for i, num in enumerate(input):
        if target - num in seen:
            return [seen[target - num], i]
        seen[num] = i

    return [-1, -1]
