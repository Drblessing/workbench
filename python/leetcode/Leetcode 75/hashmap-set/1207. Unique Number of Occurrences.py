from collections import Counter


class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        """Return if the number of occurrences of each value in the array is unique."""
        count = Counter(arr)
        return len(count) == len(set(count.values()))
