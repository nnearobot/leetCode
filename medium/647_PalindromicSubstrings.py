# 647. Palindromic Substrings
# medium
# https://leetcode.com/problems/palindromic-substrings/

class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        n = len(s)
        for i in range(n):
            for j in range(i + 1):
                if i + j < n and s[i - j] == s[i + j]:
                    res += 1
                else:
                    break
            if i == 0:
                continue
            for j in range(i):
                if i + j < n and s[i - j - 1] == s[i + j]:
                    res += 1
                else:
                    break
        return res