import heapq


def max_three(input: list[int]) -> int:
    """Returns the maximum product of three integers in input."""
    largest = heapq.nlargest(3, input)
    smallest = heapq.nsmallest(2, input)
    return max(
        largest[2] * largest[1] * largest[0], smallest[1] * smallest[0] * largest[0]
    )
