# 463. Island Perimeter
# easy
# https://leetcode.com/problems/island-perimeter/

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    continue
                if i == 0 or grid[i - 1][j] == 0:
                    perimeter += 1
                if i == m - 1 or grid[i + 1][j] == 0:
                    perimeter += 1
                if j == 0 or grid[i][j - 1] == 0:
                    perimeter += 1
                if j == n - 1 or grid[i][j + 1] == 0:
                    perimeter += 1
        return perimeter