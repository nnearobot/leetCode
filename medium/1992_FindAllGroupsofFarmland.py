# 1992. Find All Groups of Farmland
# medium
# https://leetcode.com/problems/find-all-groups-of-farmland

class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        res = []
        m, n = len(land), len(land[0])
        for i in range(m):
            for j in range(n):
                if not land[i][j]:
                    continue
                if i < m - 1 and land[i + 1][j] == 1:
                    continue
                if j < n - 1 and land[i][j + 1] == 1:
                    continue
                ii, jj = i, j
                while ii > 0 and land[ii - 1][jj] == 1:
                    ii -= 1
                while jj > 0 and land[ii][jj - 1] == 1:
                    jj -= 1
                res.append([ii, jj, i, j])
        return res