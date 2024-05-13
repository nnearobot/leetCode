# 861. Score After Flipping Matrix
# medium
# https://leetcode.com/problems/score-after-flipping-matrix

class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        toggled = [[0] * n for _ in range(m)]
        for i in range(m):
            if grid[i][0]:
                toggled[i] = grid[i]
            else:
                for j in range(n):
                    toggled[i][j] = 1 - grid[i][j]
        for j in range(n):
            ones = 0
            for i in range(m):
                if toggled[i][j]:
                    ones += 1
            if ones < m - ones:
                for i in range(m):
                    toggled[i][j] = 1 - toggled[i][j]

        res = 0
        for i in range(m):
            power = 0
            for j in range(n - 1, -1, -1):
                res += toggled[i][j] * int(math.pow(2, power)) if toggled[i][j] else 0
                power += 1

        return res