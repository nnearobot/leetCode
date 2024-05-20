# 209. Minimum Size Subarray Sum
# medium
# https://leetcode.com/problems/minimum-size-subarray-sum

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        summ = 0
        minimal_length = float('inf')
        for r in range(n):
            summ += nums[r]

            while summ >= target:
                minimal_length = min(minimal_length, r - l + 1)
                if minimal_length == 1:
                    return 1
                summ -= nums[l]
                l += 1
        return minimal_length if minimal_length != float('inf') else 0
