class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        slow = 0
        # Check each element in the array
        for fast in range(len(nums)):
            # If the fast pointer is not zero and the slow pointer is zero, swap the two elements
            # because the slow pointer is always pointing to the first zero element in the array,
            # and the fast pointer is always pointing to the first non-zero element in the array.
            if nums[fast] != 0 and nums[slow] == 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]

            if nums[slow] != 0:
                slow += 1


if __name__ == "__main__":
    nums = [0, 1, 1]
    solution = Solution()
    solution.moveZeroes(nums)
    print(nums)
