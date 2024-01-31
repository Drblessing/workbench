class Solution:
    def maxArea(self, height: list[int]) -> int:
        l, r = 0, len(height) - 1

        max_area = 0

        for w in range(len(height) - 1, 0, -1):
            h = min(height[l], height[r])
            area = w * h
            max_area = max(max_area, area)

            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        return max_area
