# 62. Unique Paths
# medium
# https://leetcode.com/problems/unique-paths/

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1 for _ in range(n)] for _ in range(m)]
        for i in range(1, m):
            for j in range(n):
                dp[i][j] = 1 if j == 0 else dp[i - 1][j] + dp[i][j - 1]
        return dp[m - 1][n - 1]