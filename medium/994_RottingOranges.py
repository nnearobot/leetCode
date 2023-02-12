# 994. Rotting Oranges
# Medium
# https://leetcode.com/problems/rotting-oranges

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        q = []
        box = grid.copy()
        rottens = []
        for i in range(n):
            for j in range(m):
                if box[i][j] == 2:
                    rottens.append([i, j])
        q.append(rottens)
        time = 0
        while len(q) > 0:
            rottens = q.pop(0)
            newRottens = []
            for pair in rottens:
                i = pair[0]
                j = pair[1]
                if i > 0 and box[i - 1][j] == 1:
                    box[i - 1][j] = 2
                    newRottens.append([i - 1, j])
                if j > 0 and box[i][j - 1] == 1:
                    box[i][j - 1] = 2
                    newRottens.append([i, j - 1])
                if i < n - 1 and box[i + 1][j] == 1:
                    box[i + 1][j] = 2
                    newRottens.append([i + 1, j])
                if j < m - 1 and box[i][j + 1] == 1:
                    box[i][j + 1] = 2
                    newRottens.append([i, j + 1])
            if len(newRottens) > 0:
                time += 1
                q.append(newRottens)
        for i in range(n):
            for j in range(m):
                if box[i][j] == 1:
                    return -1
        return time