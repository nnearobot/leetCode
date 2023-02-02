# 509. Fibonacci Number
# Easy
# https://leetcode.com/problems/fibonacci-number/

class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        dp = [0 for i in range(n + 1)]
        dp[0] = 0
        dp[1] = 1
        for i in range(n - 1):
            dp[i + 2] = dp[i] + dp[i + 1]
        return dp[n]