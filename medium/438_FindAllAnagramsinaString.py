# 438. Find All Anagrams in a String
# Medium
# https://leetcode.com/problems/find-all-anagrams-in-a-string

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []

        k = len(p)
        pMap = {}
        for i in range(k):
            if p[i] not in pMap:
                pMap[p[i]] = 0
            pMap[p[i]] += 1
        size = len(pMap)

        window = {}
        for i in range(k):
            if s[i] not in window:
                window[s[i]] = 0
            window[s[i]] += 1
        
        res = []
        for i in range(0, len(s) - k + 1):
            count = 0
            for l in window:
                if window[l] > 0 and l in pMap and window[l] == pMap[l]:
                    count += 1
                else:
                    break       
            if count == size:
                res.append(i)
            if i < len(s) - k:
                window[s[i]] -= 1
                if window[s[i]] == 0:
                    window.pop(s[i])
                if s[i + k] not in window:
                    window[s[i + k]] = 0
                window[s[i + k]] += 1

        return res