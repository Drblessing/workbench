class Solution:
    def compress(self, chars: list[str]) -> int:
        """Compresses a string in-place.
        Replace groups of characters with a character and a count.
        Keep single characters as-is.
        Double digit numbers are split into two characters.
        Return the length of the compressed string, after in-place modification.
        """

        # Initialize answer.
        s = ""

        # Iterate through chars.
        # Two pointers: i is the start of a group, j is the end of a group.
        i, j = 0, 0
        while i <= len(chars) - 1:
            # Get the character at i.
            char = chars[i]
            # Find the end of the group.
            while j < len(chars) and chars[j] == char:
                j += 1

            # Add the character to the answer.
            s += char

            # Add the count to the answer.
            count = j - i
            if count > 1:
                s += str(count)

            # Move i to the next group.
            i = j

        # Copy the answer back into chars.

        # This is a bit tricky.
        # We can't just do chars = list(s) because that would create a new list
        # and assign it to the chars variable.
        # Instead, we need to modify the existing list.
        # We can do that by assigning to the slice chars[:].
        chars[:] = list(s)

        # Return the length of the answer.
        return len(s)


if __name__ == "__main__":
    s = Solution()

    # Example 1
    chars = ["a", "a", "c"]
    assert s.compress(chars) == 6
    assert chars == ["a", "2", "b", "2", "c", "3"]

    # Example 2
    chars = ["a"]
    assert s.compress(chars) == 1
    assert chars == ["a"]
