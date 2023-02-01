# 504. Base 7
# Easy
# https://leetcode.com/problems/base-7

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 0 if nums[0] == val else 1

        count = 0
        end = len(nums)
        for i, n in enumerate(nums):
            if i == end:
                break
            while n == val:
                end -= 1
                if i == end:
                    return count
                tmp = nums[end]
                if tmp != val:
                    nums[end] = n
                    nums[i] = tmp
                n = tmp
            count += 1
        return count