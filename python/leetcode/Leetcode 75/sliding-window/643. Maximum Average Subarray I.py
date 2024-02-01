class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        """Finds the maximum average of a slidingwindow
        of size k."""

        # Initialize the sum of the first k elements
        cur_sum = max_sum = sum(nums[:k])

        # Iterate through the rest of the elements
        for i in range(k, len(nums)):
            # Add the next element and remove the first element
            cur_sum += nums[i] - nums[i - k]
            max_sum = max(max_sum, cur_sum)

        return max_sum / k
