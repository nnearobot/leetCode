# 55. Jump Game
# Medium
# https://leetcode.com/problems/jump-game/


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False] * n
        dp[-1] = True
        for i in range(n - 2, -1, -1):
            max_jump = min(i + nums[i], n - 1)
            for j in range(i + 1, max_jump + 1):
                if dp[j]:
                    dp[i] = True
                    break
        print(dp)
        return dp[0]