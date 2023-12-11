# 867. Transpose Matrix
# easy
# https://leetcode.com/problems/transpose-matrix/

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        new_matrix = [[None] * m for _ in range(n)]
        for j in range(n):
            for i in range(m):
                new_matrix[j][i] = matrix[i][j]
        return new_matrix