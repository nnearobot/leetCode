# 704. Binary Search
# Easy
# https://leetcode.com/problems/binary-search

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            return 0 if nums[0] == target else -1

        s = 0
        e = len(nums) - 1
        if nums[s] == target:
            return s
        if nums[e] == target:
            return e
        while e > s + 1:
            n = math.ceil((e - s) / 2) + s
            num = nums[n]
            if num == target:
                return n
            if target > num:
                s = n
            else:
                e = n

        return -1