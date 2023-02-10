# 45. Jump Game II
# Easy
# https://leetcode.com/problems/jump-game-ii/

import math

class Solution:
    def jump(self, nums: List[int]) -> int:
        memo = [math.inf for i in range(len(nums))]
        memo[len(nums) - 1] = 0
        for num in range(len(nums) - 2, -1, -1):
            for step in range(1, min(nums[num] + 1, len(nums) - num)):
                memo[num] = min(memo[num], memo[num + step] + 1)
        return 0 if memo[0] == math.inf else int(memo[0])

