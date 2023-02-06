# 70. Climbing Stairs
# Easy
# https://leetcode.com/problems/climbing-stairs/

class Solution:
    def climbStairs(self, n: int) -> int:
        dp = []
        dp.append(1)
        dp.append(2)
        for i in range(n - 2):
            dp.append(dp[i] + dp[i + 1])
        return dp[n - 1]