# 387. First Unique Character in a String
# easy
# https://leetcode.com/problems/first-unique-character-in-a-string

class Solution:
    def firstUniqChar(self, s: str) -> int:
        letter_map = {}
        for i, l in enumerate(s):
            if l in letter_map:
                letter_map[l] = -1
            else:
                letter_map[l] = i
        res = -1
        for l in letter_map:
            if letter_map[l] == -1:
                continue
            res = letter_map[l] if res == -1 else min(res, letter_map[l])
        return res