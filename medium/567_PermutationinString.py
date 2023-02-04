# 567. Permutation in String
# Medium
# https://leetcode.com/problems/permutation-in-string

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        k = len(s1)
        sMap = {}
        for i in range(k):
            if s1[i] not in sMap:
                sMap[s1[i]] = 0
            sMap[s1[i]] += 1
        size = len(sMap)

        window = {}
        for i in range(k):
            if s2[i] not in window:
                window[s2[i]] = 0
            window[s2[i]] += 1
        
        for i in range(0, len(s2) - k + 1):
            count = 0
            for l in window:
                if window[l] > 0 and l in sMap and window[l] == sMap[l]:
                    count += 1
                else:
                    break       
            if count == size:
                return True
            if i < len(s2) - k:
                window[s2[i]] -= 1
                if window[s2[i]] == 0:
                    window.pop(s2[i])
                if s2[i + k] not in window:
                    window[s2[i + k]] = 0
                window[s2[i + k]] += 1

        return False