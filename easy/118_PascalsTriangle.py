# 118. Pascal's Triangle
# easy
# https://leetcode.com/problems/pascals-triangle/

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        for num in range(1, numRows):
            row = [1]
            for i in range(num - 1):
                row.append(res[num - 1][i] + res[num - 1][i + 1])
            row.append(1)
            res.append(row)
        return res