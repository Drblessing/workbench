from collections import Counter


class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:
        # Count the occurrences of each row pattern
        row_c = Counter(tuple(row) for row in grid)

        # Count the occurrences of each column pattern
        col_c = Counter(zip(*grid))

        # Count congruent pairs by matching row and column patterns
        return sum([row_c[row] * col_c[row] for row in row_c])
