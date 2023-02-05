"""
213. House Robber II
Medium
https://leetcode.com/problems/house-robber-ii

"""

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        dp1 = [] # without the first
        dp1.append(0)
        dp1.append(nums[1])
        dp2 = [] # with the first
        dp2.append(nums[0])
        dp2.append(nums[0])
        for i in range(2, len(nums)):
            dp1.append(max(dp1[i - 1], dp1[i - 2] + nums[i]))
            dp21 = dp2[i - 1]
            dp22 = dp2[i - 2] + nums[i]
            if i == len(nums) - 1:
                dp22 -= nums[0]
            dp2.append(max(dp21, dp22))
        return max(dp1[len(nums) - 1], dp2[len(nums) - 1])