from collections import Counter


class Solution:
    def maxOperations(self, nums: list[int], k: int) -> int:
        """Calculate the maximum number of pairs that sum to k."""

        # Count the frequency of each number
        counter = Counter(nums)

        # Initialize the number of pairs
        pairs = 0
        # Iterate through the numbers, checking for k - num
        for num in counter:
            # If the number is greater than k, skip it
            if num > k:
                continue

            # If the number is half of k, add half the frequency to pairs
            if num * 2 == k:
                pairs += counter[num] // 2
            # Otherwise, add the minimum of the frequency of num and k - num, if it's less than 1/2 of k
            # to avoid duplicates with changing the dictionary while iterating,
            # clever

            elif num < k / 2 and k - num in counter:
                pairs += min(counter[num], counter[k - num])
                # Clear the frequency of num and k - num

        return pairs
