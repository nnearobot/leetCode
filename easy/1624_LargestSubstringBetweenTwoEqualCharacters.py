# 1624. Largest Substring Between Two Equal Characters
# easy
# https://leetcode.com/problems/largest-substring-between-two-equal-characters

class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        res = -1
        letterMap = {}
        for i, letter in enumerate(s):
            if letter not in letterMap:
                letterMap[letter] = [i, -1]
            else:
                letterMap[letter][1] = i
                dist = i - letterMap[letter][0] - 1
                res = max(res, dist)
        return res