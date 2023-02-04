# 283. Move Zeroes
# Easy
# https://leetcode.com/problems/move-zeroes

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        if len(nums) == 1:
            return

        p = -1
        for i in range(len(nums)):
            if nums[i] == 0:
                if p < 0:
                    p = i
            elif p >= 0:
                nums[p] = nums[i]
                nums[i] = 0
                p += 1
