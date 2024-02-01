class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        """Find the maximum number of consecutive ones in a list, allowing up to k zero flips."""

        max_ones = 0  # Maximum number of consecutive ones found
        left = 0  # Left pointer for the sliding window
        zero_count = 0  # Count of zeros in the current window

        for right in range(len(nums)):
            # Expand the window to the right
            if nums[right] == 0:
                zero_count += 1

            # If there are more than k zeros, shrink the window from the left
            while zero_count > k:
                left += 1
                if nums[left - 1] == 0:
                    zero_count -= 1

            # Update the maximum number of ones
            max_ones = max(max_ones, right - left + 1)

        return max_ones


if __name__ == "__main__":
    # Create a random binary list 10^5 elements long
    import random

    test_case = [random.randint(0, 1) for _ in range(10**5)]

    ans = Solution().longestOnes(test_case, 1000000)

    print(len(test_case))
    print(ans)
