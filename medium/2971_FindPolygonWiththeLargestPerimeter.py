# 2971. Find Polygon With the Largest Perimeter
# medium
# https://leetcode.com/problems/find-polygon-with-the-largest-perimeter/

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        maxPerimeter = sum(nums)
        nums.sort()
        for i in range(len(nums) - 1, 1, -1):
            if nums[i] < maxPerimeter - nums[i]:
                return maxPerimeter
            maxPerimeter -= nums[i]

        return -1