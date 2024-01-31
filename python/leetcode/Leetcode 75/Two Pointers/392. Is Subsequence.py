class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == "":
            return True

        slow, fast = 0, 0

        if len(s) > len(t):
            return False

        if s == t:
            return True

        while fast < len(t):
            if s[slow] == t[fast]:
                slow += 1

            if slow == len(s):
                return True

            fast += 1

        return slow == len(s)
