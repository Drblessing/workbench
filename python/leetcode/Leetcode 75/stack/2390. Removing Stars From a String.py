class Solution:
    def removeStars(self, s: str) -> str:
        """Remove all stars from the string, but each time a star is removed, the previous character is also removed."""
        stack = []
        for c in s:
            if c == "*":
                if stack:
                    stack.pop()
            else:
                stack.append(c)
        return "".join(stack)
