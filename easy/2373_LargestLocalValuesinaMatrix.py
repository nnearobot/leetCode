# 2373. Largest Local Values in a Matrix
# easy
# https://leetcode.com/problems/largest-local-values-in-a-matrix/

class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid) - 2, len(grid[0]) - 2
        res = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                res[i][j] = max(
                    grid[i][j],
                    grid[i][j + 1],
                    grid[i][j + 2],
                    grid[i + 1][j],
                    grid[i + 1][j + 1],
                    grid[i + 1][j + 2],
                    grid[i + 2][j],
                    grid[i + 2][j + 1],
                    grid[i + 2][j + 2]
                )
        return res