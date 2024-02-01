class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        """Calculate the maximum number of vowels in
        any length k substring of s."""

        vowels = ["a", "e", "i", "o", "u"]

        cur_v = 0
        for letter in s[:k]:
            if letter in vowels:
                cur_v += 1
        max_vowels = cur_v

        # Iterate through remaining letters
        for i in range(k, len(s)):
            cur_v += (s[i] in vowels) - (s[i - k] in vowels)
            max_vowels = max(max_vowels, cur_v)

        return max_vowels


if __name__ == "__main__":
    s = "abciiidef"
    k = 3
    print(Solution().maxVowels(s, k))  # 3
    s = "aeiou"
    k = 2
    print(Solution().maxVowels(s, k))  # 2
