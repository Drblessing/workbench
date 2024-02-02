from itertools import accumulate, compress, chain, starmap, pairwise
from operator import add, not_


class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        """Find the maximum number of consecutive ones in a list, allowing up to one zero drop."""

        # Max number of consecutive ones
        # Left and right pointers for the sliding window
        # Count of zeros in the current window
        max_ones = left = right = zero_count = 0

        # Anchor the right pointer to the end of the sliding window,
        # and adjust the left pointer to only contain one zero.
        for right in range(len(nums)):
            # Expand the window to the right
            if nums[right] == 0:
                zero_count += 1

            # If there are more than one zero, shrink the window from the left
            while zero_count > 1:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1

            # Update the maximum number of ones
            max_ones = max(max_ones, right - left)

        return max_ones

    def longestSubarrayFunc(self, nums: list[int]) -> int:
        streaks_of_1s = accumulate(nums, lambda a, x: (a + 1) * (x != 0), initial=0)
        streaks_at_0 = compress(streaks_of_1s, map(not_, chain(nums, (0,))))
        return max(starmap(add, pairwise(streaks_at_0)), default=len(nums) - 1)
