# 64. Minimum Path Sum
# Medium
# https://leetcode.com/problems/minimum-path-sum/

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[0][0] = grid[0][0]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                fromTop = math.inf if i == 0 else dp[i - 1][j]
                fromLeft = math.inf if j == 0 else dp[i][j - 1]
                dp[i][j] = int(grid[i][j] + min(fromTop, fromLeft))
        
        return dp[m - 1][n - 1]