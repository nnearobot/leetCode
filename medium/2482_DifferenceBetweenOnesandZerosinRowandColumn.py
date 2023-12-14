# 2482. Difference Between Ones and Zeros in Row and Column
# medium
# https://leetcode.com/problems/difference-between-ones-and-zeros-in-row-and-column

class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        rows = [0 for _ in range(m)]
        cols = [0 for _ in range(n)]
        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                rows[i] += 1 if cell == 1 else -1
                cols[j] += 1 if cell == 1 else -1

        diff = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                diff[i][j] = rows[i] + cols[j]

        return diff
