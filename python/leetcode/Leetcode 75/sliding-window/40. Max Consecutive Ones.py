class MaxConsecutiveOnes:
    """A class for exploring the Max Consecutive Ones problems."""

    def __init__(self, nums: list[int]) -> None:
        self.nums = nums

    def findMaxConsecutiveOnes(self) -> int:
        """Find max consecutive ones in the list of numbers,
        with zero flip allowed.
        """

        max_ones = 0
        count = 0
        for num in self.nums:
            if num == 1:
                count += 1
                max_ones = max(max_ones, count)
            else:
                count = 0
        return max_ones

    def max_consecutive_ones(self) -> int:
        """Find the maximum number of consecutive ones in a list, allowing one zero flip."""

        max_ones = 0  # Maximum number of consecutive ones found
        left = 0  # Left pointer for the sliding window
        right = 0  # Right pointer for the sliding window
        zero_count = 0  # Count of zeros in the current window

        while right < len(self.nums):
            # Expand the window to the right
            if self.nums[right] == 0:
                zero_count += 1

            # If there are more than one zero, shrink the window from the left
            while zero_count > 1:
                left += 1
                if self.nums[left - 1] == 0:
                    zero_count -= 1

            # Update the maximum number of ones
            max_ones = max(max_ones, right - left + 1)
            right += 1

        return max_ones


if __name__ == "__main__":
    nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1]
    max_ones = MaxConsecutiveOnes(nums)
    print(max_ones.findMaxConsecutiveOnes())
    print(max_ones.max_consecutive_ones())
