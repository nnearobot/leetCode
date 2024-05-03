# 165. Compare Version Numbers
# medium
# https://leetcode.com/problems/compare-version-numbers

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        i1, i2 = 0, 0
        j1, j2 = 0, 0
        n1, n2 = len(version1), len(version2)
        while j1 <= n1:
            if j1 == n1 or version1[j1] == ".":
                v1 = int(version1[i1:j1])
                v2 = 0
                while j2 <= n2:
                    if j2 == n2 or version2[j2] == ".":
                        v2 = int(version2[i2:j2])
                        break
                    j2 += 1
                if v1 < v2:
                    return -1
                if v1 > v2:
                    return 1
                j2 += 1
                i2 = j2
                i1 = j1 + 1
            j1 += 1
        v1 = 0
        while j2 <= n2:
            if j2 == n2 or version2[j2] == ".":
                v2 = int(version2[i2:j2])
                if v1 < v2:
                    return -1
                if v1 > v1:
                    return 1
                i2 = j2 + 1
            j2 += 1
        return 0
