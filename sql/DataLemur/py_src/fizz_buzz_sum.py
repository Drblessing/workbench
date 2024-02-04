def fizz_buzz_sum(target: int) -> int:
    """
    Calculate the sum of all numbers divisible by 3 or 5 below a target number.
    """

    # Initialize the sum to 0
    s = 0

    # Iterate over the range up to the target number
    for i in range(target):
        # If the current number is divisible by 3 or 5
        if i % 3 == 0 or i % 5 == 0:
            print(i)
            # Add the current number to the sum
            s += i

    # Return the final sum
    return s
