# 344. Reverse String
# Easy
# https://leetcode.com/problems/reverse-string

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        tmp = ""
        n = len(s)
        for i in range(0, n // 2):
            tmp = s[i]
            s[i] = s[n - 1 - i]
            s[n - 1 - i] = tmp