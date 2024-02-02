def max_subarray_sum(input: list[int]) -> int:
    """Returns the maximum sum of a contiguous subarray of the input list."""

    if not isinstance(input, list):
        raise TypeError("Input must be a list.")

    if len(input) == 0:
        raise ValueError("Input must not be empty.")

    # Initialize max_sum to 0
    max_sum = 0

    # Iterate through the input list
    for i, v in enumerate(input):
        # Keep track of max sum up to current index
        # by replacing values in input list with cumulative max sum
        if i > 0:
            input[i] = max(v, v + input[i - 1])
        # Update max_sum if current value is greater than current max_sum
        max_sum = max(max_sum, input[i])

    return max_sum
