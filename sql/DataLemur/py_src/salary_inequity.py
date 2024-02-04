def min_inequity(salaries: list[int], n: int) -> int:
    """Find the min inequity of salaries for n choices."""

    # Sort salaries in ascending order
    salaries.sort()

    # Initialize min_inequity to the largest possible value
    min_inequity = salaries[-1] - salaries[0]

    # Iterate through salaries
    for i in range(len(salaries) - n + 1):
        # Find the inequity of the current n choices
        inequity = salaries[i + n - 1] - salaries[i]

        # Update min_inequity if necessary
        if inequity < min_inequity:
            min_inequity = inequity

    return min_inequity

