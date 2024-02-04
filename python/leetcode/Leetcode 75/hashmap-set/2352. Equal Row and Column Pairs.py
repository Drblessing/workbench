from collections import Counter


class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:
        """Return the number of congruent row and column pairs in a grid.
        Congruent includes order and count of elements."""

        # Count the number of congruent row and column pairs
        congruent_pairs = 0

        # Use a trie to store each row of the grid,
        # and use it to check for congruent columns.
        rows = {}

        # Iterate through the rows of the grid
        for i, row in enumerate(grid):
            # Use a trie to store the elements of the row
            node = rows
            for num in row:
                if num not in node:
                    node[num] = {}
                node = node[num]
            # Store the row number in the trie node
            node["#"] = i

        # Check the columns
        for j in range(len(grid[0])):
            node = rows
            for i in range(len(grid)):
                num = grid[i][j]
                if num in node:
                    node = node[num]
                else:
                    break
            else:
                # If we've reached the end of the column and found a row number,
                # increment the count of congruent pairs
                if "#" in node:
                    congruent_pairs += 1

        return congruent_pairs
