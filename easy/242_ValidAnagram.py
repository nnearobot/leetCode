# 242. Valid Anagram
# easy
# https://leetcode.com/problems/valid-anagram/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_map = collections.defaultdict(int)
        for char_item in s:
            char_map[char_item] += 1
        for char_item in t:
            if char_item not in char_map or char_map[char_item] == 0:
                return False
            char_map[char_item] -= 1
        return sum(char_map.values()) == 0
