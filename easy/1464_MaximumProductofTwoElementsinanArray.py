# 1464. Maximum Product of Two Elements in an Array
# easy
# https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        biggest1, biggest2 = 0, 0
        for num in nums:
            if num > biggest1:
                biggest2 = biggest1
                biggest1 = num
            elif num > biggest2:
                biggest2 = num
        return (biggest1 - 1) * (biggest2 - 1)

        '''
        nums = sorted(nums, reverse=True)
        return (nums[0] - 1) * (nums[1] - 1)
        '''
