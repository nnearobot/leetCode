# 896. Monotonic Array
# Easy
# https://leetcode.com/problems/monotonic-array

class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) < 2:
            return True
        dec_inc = 0
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                continue
            if nums[i] > nums[i - 1]:
                if dec_inc < 0:
                    return False
                dec_inc = 1
            if nums[i] < nums[i - 1]:
                if dec_inc > 0:
                    return False
                dec_inc = -1
        return True
