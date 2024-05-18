# 1219. Path with Maximum Gold
# medium
# https://leetcode.com/problems/path-with-maximum-gold

from collections import deque
from typing import List

class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        DIRECTIONS = [1, 0, -1, 0, 1]
        total_gold = sum(sum(row) for row in grid)

        def get_max_gold_for_path_started_from(i: int, j: int):
            visited = set()
            visited.add((i, j))
            queue = deque()
            queue.append((i, j, grid[i][j], visited)) # i, j, current_gold, visited
            max_gold = 0
            while queue:
                i, j, current_gold, visited = queue.popleft()
                if current_gold == total_gold:
                    return total_gold

                max_gold = max(max_gold, current_gold)

                for dir_num in range(4):
                    next_i = i + DIRECTIONS[dir_num]
                    next_j = j + DIRECTIONS[dir_num + 1]
                    if 0 <= next_i < m \
                            and 0 <= next_j < n \
                            and (next_i, next_j) not in visited \
                            and grid[next_i][next_j]:
                        visited.add((next_i, next_j))
                        queue.append((next_i, next_j, current_gold + grid[next_i][next_j], visited.copy()))
                        visited.remove((next_i, next_j))
            return max_gold

        max_gold = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    gold_from_this = get_max_gold_for_path_started_from(i, j)
                    if gold_from_this == total_gold:
                        return total_gold
                    max_gold = max(max_gold, gold_from_this)

        return max_gold
