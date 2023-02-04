"""
189. Rotate Array
Medium
https://leetcode.com/problems/rotate-array/

"""

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)

        if k == 0:
            return

        tmp = nums[len(nums) - k:len(nums)]
        for i in range(len(nums) - k - 1, -1, -1):
            nums[i + k] = nums[i]
        for i in range(k):
            nums[i] = tmp[i]