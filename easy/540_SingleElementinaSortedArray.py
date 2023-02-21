# 540. Single Element in a Sorted Array
# Easy
# https://leetcode.com/problems/single-element-in-a-sorted-array/

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        s = 0
        e = len(nums) - 1
        while e > s + 1:
            m = (e + s) // 2
            if nums[m] != nums[m - 1] and nums[m] != nums[m + 1]:
                return nums[m]

            if (m % 2 == 0 and nums[m] == nums[m + 1]) or (m % 2 == 1 and nums[m] != nums[m + 1]):
                s = m + m % 2
            else:
                e = m - m % 2
        
        return nums[s] if s == 0 or nums[s] != nums[s - 1] else nums[e]