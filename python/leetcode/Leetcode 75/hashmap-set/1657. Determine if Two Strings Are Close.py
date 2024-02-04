from collections import Counter as C


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        c1, c2 = C(word1), C(word2)
        return sorted(c1.keys()) == sorted(c2.keys()) and sorted(c1.values()) == sorted(
            c2.values()
        )
