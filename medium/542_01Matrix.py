# 542. 01 Matrix
# Medium
# https://leetcode.com/problems/01-matrix

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        n = len(mat)
        m = len(mat[0])
        MAX_DIST = n + m + 1
        res = [[MAX_DIST for _ in range(m)] for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    res[i][j] = 0
                else:
                    top = res[i - 1][j] if i > 0 else MAX_DIST
                    left = res[i][j - 1] if j > 0 else MAX_DIST 
                    res[i][j] = min(res[i][j], top + 1, left + 1)

        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                bottom = res[i + 1][j] if i < n - 1 else MAX_DIST
                right = res[i][j + 1] if j < m - 1 else MAX_DIST 
                res[i][j] = min(res[i][j], bottom + 1, right + 1)
        
        return res