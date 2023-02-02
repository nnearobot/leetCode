# 35. Search Insert Position
# Easy
# https://leetcode.com/problems/first-bad-version/

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            return 0 if target <= nums[0] else 1

        if target <= nums[0]:
            return 0
        if target > nums[len(nums) - 1]:
            return len(nums)
        if len(nums) == 2:
            return 1

        s = 0
        e = len(nums) - 1
        while e > s + 1:
            n = math.ceil((e - s) / 2) + s
            num = nums[n]
            if num == target:
                return n
            if target > num:
                s = n
            else:
                e = n
            if e == s + 1:
                return e

        return 0