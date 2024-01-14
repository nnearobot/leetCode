# 1704. Determine if String Halves Are Alike
# easy
# https://leetcode.com/problems/determine-if-string-halves-are-alike/

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
        a = b = 0
        n = len(s)
        for i in range(n // 2):
            a += 1 if s[i] in vowels else 0
            b += 1 if s[n - i - 1]  in vowels else 0
        return a == b