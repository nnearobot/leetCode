# 2812. Find the Safest Path in a Grid
# medium
# https://leetcode.com/problems/find-the-safest-path-in-a-grid

from collections import deque

class Solution:
    DIRECTIONS = [1, 0, -1, 0, 1]
    safeness_grid = []
    n = 0

    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        self.n = len(grid)
        multi_source_q = deque()
        self.safeness_grid = [[-1] * self.n for _ in range(self.n)]
        for i in range(self.n):
            for j in range(self.n):
                if grid[i][j]:
                    self.safeness_grid[i][j] = 0
                    multi_source_q.append((i, j))
        while multi_source_q:
            i, j = multi_source_q.popleft()
            for d in range(4):
                next_i = i + self.DIRECTIONS[d]
                next_j = j + self.DIRECTIONS[d + 1]
                if 0 <= next_i < self.n and 0 <= next_j < self.n and self.safeness_grid[next_i][next_j] == -1:
                    self.safeness_grid[next_i][next_j] = self.safeness_grid[i][j] + 1
                    multi_source_q.append((next_i, next_j))

        start, end, res = 0, 0, -1
        for i in range(self.n):
            for j in range(self.n):
                end = max(end, self.safeness_grid[i][j])

        while start <= end:
            middle = start + (end - start) // 2
            if self.has_path_with_safeness(middle):
                res = middle
                start = middle + 1
            else:
                end = middle - 1

        return res


    def has_path_with_safeness(self, safeness) -> bool:
        if self.safeness_grid[0][0] < safeness or self.safeness_grid[self.n - 1][self.n - 1] < safeness:
            return False

        visited = [[False] * self.n for _ in range(self.n)]
        visited[0][0] = True
        queue = deque()
        queue.append((0, 0))
        while queue:
            i, j = queue.popleft()
            if i == self.n - 1 and j == self.n - 1:
                return True

            for dir_num in range(4):
                next_i = i + self.DIRECTIONS[dir_num]
                next_j = j + self.DIRECTIONS[dir_num + 1]
                if 0 <= next_i < self.n \
                        and 0 <= next_j < self.n \
                        and not visited[next_i][next_j] \
                        and self.safeness_grid[next_i][next_j] >= safeness:
                    visited[next_i][next_j] = True
                    queue.append((next_i, next_j))

        return False
