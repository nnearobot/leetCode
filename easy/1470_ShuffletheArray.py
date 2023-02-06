# 1470. Shuffle the Array
# Easy
# https://leetcode.com/problems/shuffle-the-array/

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = []
        for i in range(0, n):
            res.append(nums[i])
            res.append(nums[i + n])
        return res