# 10. Regular Expression Matching
# hard
# https://leetcode.com/problems/regular-expression-matching/description/

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not p:
            return not s

        is_match = len(s) > 0 and (p[0] == s[0] or p[0] == '.')
        if len(p) >= 2 and p[1] == '*':
            return (is_match and self.isMatch(s[1:], p) or self.isMatch(s, p[2:]))
        else:
            return is_match and self.isMatch(s[1:], p[1:])
