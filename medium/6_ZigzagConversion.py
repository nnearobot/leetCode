"""
6. Zigzag Conversion
Medium
https://leetcode.com/problems/zigzag-conversion/

"""
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        matrix = [[] for i in range(numRows)]
        
        down = True
        row = 0
        for l in s:
            matrix[row].append(l)
            row += 1 if down else -1
            if row == numRows - 1 or row == 0:
                down = not down
        res = ""
        for row in matrix:
            res += "".join(row)
        return res