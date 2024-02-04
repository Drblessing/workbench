from collections import Counter


class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:
        # Count the occurrences of each row pattern
        row_patterns = Counter(tuple(row) for row in grid)

        # Count the occurrences of each column pattern
        column_patterns = Counter(
            tuple(grid[row][col] for row in range(len(grid)))
            for col in range(len(grid[0]))
        )

        # Count congruent pairs by matching row and column patterns
        congruent_pairs = sum(
            row_patterns[row] * column_patterns.get(row, 0) for row in row_patterns
        )

        return congruent_pairs
