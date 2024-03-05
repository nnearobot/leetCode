# 1750. Minimum Length of String After Deleting Similar Ends
# medium
# https://leetcode.com/problems/minimum-length-of-string-after-deleting-similar-ends

class Solution:
    def minimumLength(self, s: str) -> int:
        left = 0
        n = len(s)
        right = n - 1
        while left < right:
            if s[left] != s[right]:
                return right - left + 1
            i = left
            while i < n and s[i] == s[left]:
                i += 1
            if i > right:
                return 0
            left = i
            i = right
            while s[i] == s[right]:
                i -= 1
            right = i
          
        return right - left + 1
