# 1582. Special Positions in a Binary Matrix
# easy
# https://leetcode.com/problems/special-positions-in-a-binary-matrix/

class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        spec_number = 0
        m = len(mat)
        for i, row in enumerate(mat):
            specNum = -1
            for j, cell in enumerate(row):
                if cell == 1:
                    if specNum == -1:
                        specNum = j
                    else:
                        specNum = -1
                        break
            if specNum > -1:
                spec_number += 1
                for k in range(m):
                    if k == i:
                        continue
                    if mat[k][specNum] == 1:
                        spec_number -= 1
                        break
        return spec_number