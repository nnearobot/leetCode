# 576. Out of Boundary Paths
# medium
# https://leetcode.com/problems/out-of-boundary-paths/

class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        MOD = 10**9 + 7
        memo = [[[-1 for _ in range(maxMove + 1)] for _ in range(n)] for _ in range(m)]

        def backtrack(moveCount: int, curRow: int, curCol: int) -> int:
            nonlocal m, n, maxMove, memo

            if curRow < 0 or curRow >= m or curCol < 0 or curCol >= n:
                if moveCount <= maxMove:
                    return 1
                return 0
            
            if moveCount > maxMove:
                return 0

            if memo[curRow][curCol][moveCount] > -1:
                return memo[curRow][curCol][moveCount]
            
            destinations = [(1, 0),(-1, 0),(0, 1),(0, -1)]
            pathCount = 0
            for (i, j) in destinations:
                pathCount += backtrack(moveCount + 1, curRow + i, curCol + j) % MOD

            memo[curRow][curCol][moveCount] = pathCount % MOD

            return memo[curRow][curCol][moveCount]
                
        return backtrack(0, startRow, startColumn)