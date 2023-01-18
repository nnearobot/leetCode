"""
918. Maximum Sum Circular Subarray
Medium
https://leetcode.com/problems/maximum-sum-circular-subarray/description/

"""

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        
        summ, maxSum, curMax, minSum, curMin = 0, nums[0], 0, nums[0], 0
        for num in nums:
            curMax = max(curMax + num, num)
            maxSum = max(maxSum, curMax)
            curMin = min(curMin + num, num)
            minSum = min(minSum, curMin)
            summ += num

        return max(maxSum, summ - minSum) if maxSum > 0 else maxSum