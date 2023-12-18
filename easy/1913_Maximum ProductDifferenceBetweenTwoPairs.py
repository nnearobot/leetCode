# 1913. Maximum Product Difference Between Two Pairs
# easy
# https://leetcode.com/problems/maximum-product-difference-between-two-pairs

class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()
        return (nums[-1] * nums[-2]) - (nums[0] * nums[1])