def contains_duplicate(input: list[int]) -> bool:
    """Returns Ture if any value appears at least twice in the list,
    and False otherwise."""
    return len(set(input)) != len(input)
