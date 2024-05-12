# 55. Jump Game
# Medium
# https://leetcode.com/problems/jump-game/


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last = len(nums) - 1
        for num in range(len(nums) - 1, -1, -1):
            if num + nums[num] >= last:
                last = num
        return last == 0