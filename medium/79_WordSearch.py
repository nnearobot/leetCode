# 79. Word Search
# medium
# https://leetcode.com/problems/word-search

from collections import deque, Counter
from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        DIRECTIONS = [1, 0, -1, 0, 1]
        m, n = len(board), len(board[0])

        # check if all needed letters exists in the board:
        word_counter = Counter(word)
        board_plain = []
        for row in board:
            board_plain += row
        board_counter = Counter(board_plain)
        print(word_counter)
        print(board_counter)

        for letter, count in word_counter.items():
            if letter not in board_counter or board_counter[letter] < count:
                return False

        word_len = len(word)
        queue = deque()
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    visited = set()
                    visited.add((i, j))
                    queue.append((i, j, 1, visited)) # i, j, current_word_len, visited

        while queue:
            i, j, current_word_len, visited = queue.popleft()
            if current_word_len == word_len:
                return True

            for dir_num in range(4):
                next_i = i + DIRECTIONS[dir_num]
                next_j = j + DIRECTIONS[dir_num + 1]
                if 0 <= next_i < m \
                        and 0 <= next_j < n \
                        and (next_i, next_j) not in visited \
                        and board[next_i][next_j] == word[current_word_len]:
                    visited.add((next_i, next_j))
                    queue.append((next_i, next_j, current_word_len + 1, visited.copy()))
                    visited.remove((next_i, next_j))

        return False
