# 119. Pascal's Triangle II
# easy
# https://leetcode.com/problems/pascals-triangle-ii

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res_row = [1]
        for num in range(1, rowIndex + 1):
            row = [1]
            for i in range(num - 1):
                row.append(res_row[i] + res_row[i + 1])
            row.append(1)
            res_row = row
        return res_row