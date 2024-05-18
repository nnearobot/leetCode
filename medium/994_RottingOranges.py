# 994. Rotting Oranges
# Medium
# https://leetcode.com/problems/rotting-oranges

from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        fresh = 0

        queue = deque()
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 2:
                    queue.append((row, col, 0))
                elif grid[row][col] == 1:
                    fresh += 1

        DIRECTIONS = [1, 0, -1, 0, 1]
        max_minutes = 0
        seen = set()

        while queue:
            row, col, minutes = queue.popleft()
            max_minutes = max(max_minutes, minutes)

            for dir_num in range(4):
                next_row = row + DIRECTIONS[dir_num]
                next_col = col + DIRECTIONS[dir_num + 1]
                if 0 <= next_row < m \
                        and 0 <= next_col < n \
                        and grid[next_row][next_col] == 1 \
                        and (next_row, next_col) not in seen:
                    seen.add((next_row, next_col))
                    queue.append((next_row, next_col, minutes + 1))
                    fresh -= 1

        return max_minutes if fresh == 0 else -1
