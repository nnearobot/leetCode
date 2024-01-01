# 455. Assign Cookies
# easy
# https://leetcode.com/problems/assign-cookies

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        children, sp = 0, 0
        while children < len(g) and sp < len(s):
            if s[sp] >= g[children]:
                children += 1
            sp += 1
        return children