# 1091. Shortest Path in Binary Matrix
# Medium
# https://leetcode.com/problems/shortest-path-in-binary-matrix

from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
            return -1
        if n == 1:
            return 1

        maxLength = n * n
        pathGrid = [[maxLength if grid[i][j] == 0 else -1 for j in range(n)] for i in range(n)]
        pathGrid[0][0] = 1

        q = deque()
        q.append((0, 0)) #row, col
        while q:
            (row, col) = q.popleft()
            for (x, y) in [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]:
                new_row, new_col = row + x, col + y
                if new_row < 0 or new_row >= n or new_col < 0 or new_col >= n:
                    continue
                if pathGrid[new_row][new_col] == -1:
                    continue
                if pathGrid[new_row][new_col] > pathGrid[row][col] + 1:
                    pathGrid[new_row][new_col] = pathGrid[row][col] + 1
                    q.append((new_row, new_col))
        
        return pathGrid[n - 1][n - 1] if pathGrid[n - 1][n - 1] < maxLength else -1
