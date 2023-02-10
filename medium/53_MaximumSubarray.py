"""
53. Maximum Subarray
Medium
https://leetcode.com/problems/maximum-subarray

"""
import math

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = -math.inf
        curSum = 0
        for n in nums:
            curSum = max(n, curSum + n)
            maxSum = max(maxSum, curSum)
        return int(maxSum)