# 2101. Detonate the Maximum Bombs
# Medium
# https://leetcode.com/problems/detonate-the-maximum-bombs

from collections import deque

class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        children = [[] for _ in bombs]
        for i, bomb1 in enumerate(bombs):
            for j, bomb2 in enumerate(bombs):
                if i == j:
                    continue
                dist_square = (bomb1[0] - bomb2[0]) * (bomb1[0] - bomb2[0]) + (bomb1[1] - bomb2[1]) * (bomb1[1] - bomb2[1])
                if bomb1[2] * bomb1[2] >= dist_square:
                    children[i].append(j)

        q = deque()
        for i, bList in enumerate(children):
            if len(bList) > 0:
                q.append((i, i)) # bomb_number, firstly_explosed_bomb_number
        
        explosed_bombs = [{i} for i in range(len(bombs))]
        max_explosed = 1

        while q:
            (bomb_num, first_bomb) = q.popleft()
            for next_bomb_num in children[bomb_num]:
                if next_bomb_num not in explosed_bombs[first_bomb]:
                    q.append((next_bomb_num, first_bomb))
            explosed_bombs[first_bomb] = explosed_bombs[first_bomb].union(children[bomb_num])
            max_explosed = max(max_explosed, len(explosed_bombs[first_bomb]))

        return max_explosed
