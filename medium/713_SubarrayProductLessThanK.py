# 713. Subarray Product Less Than K
# medium
# https://leetcode.com/problems/subarray-product-less-than-k/


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        left = right = 0
        n = len(nums)
        product = 1
        res = 0
        while right < n:
            product *= nums[right]
            right += 1
            if product >= k:
                while left < right and product >= k:
                    product //= nums[left]
                    left += 1
            res += right - left
        return res
