# 74. Search a 2D Matrix
# Medium
# https://leetcode.com/problems/search-a-2d-matrix

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if target < matrix[0][0] or target > matrix[len(matrix) - 1][len(matrix[0]) - 1]:
            return False

        s = 0
        e = len(matrix) - 1
        while e > s:
            m = math.ceil((e + s) / 2)
            if target < matrix[m][0]:
                e = m - 1
            else:
                s = m
        row = e
        s = 0
        e = len(matrix[row]) - 1
        while e > s:
            m = math.ceil((e + s) / 2)
            if target < matrix[row][m]:
                e = m - 1
            else:
                s = m

        return matrix[row][s] == target