# 48. Rotate Image
# medium
# https://leetcode.com/problems/rotate-image

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        n = len(matrix)
        for i in range(n // 2):
            r1, c1 = i, i
            r2, c2 = n - i - 1, i
            r3, c3 = n - i - 1, n - i - 1
            r4, c4 = i, n - i - 1

            for j in range(i, n - i - 1):
                matrix[r1][c1], matrix[r2][c2], matrix[r3][c3], matrix[r4][c4] = \
                matrix[r2][c2], matrix[r3][c3], matrix[r4][c4], matrix[r1][c1]
                c1 += 1
                r2 -= 1
                c3 -= 1
                r4 += 1