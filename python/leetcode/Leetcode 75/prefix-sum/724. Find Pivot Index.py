class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        """Calculate pivot index where the index is discarded."""

        # Calculate left and rigt sums for each index.
        # Return first index where left and right sums are equal.
        # Otherwise, return -1.
        left_sum = 0
        right_sum = sum(nums)
        for i, num in enumerate(nums):
            right_sum -= num
            if left_sum == right_sum:
                return i
            left_sum += num
        return -1
