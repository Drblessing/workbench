class Solution:
    def decodeString(self, s: str) -> str:
        """Decode a string with a number followed by a string in brackets."""

        stack = []
        for c in s:
            if c == "]":
                # Pop the string inside the brackets.
                string = ""
                while stack and stack[-1] != "[":
                    string = stack.pop() + string
                stack.pop()
                # Pop the number before the brackets.
                number = ""
                while stack and stack[-1].isdigit():
                    number = stack.pop() + number
                stack.append(int(number) * string)
            else:
                stack.append(c)
        return "".join(stack)
