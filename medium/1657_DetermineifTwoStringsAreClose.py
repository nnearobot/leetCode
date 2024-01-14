# 1657. Determine if Two Strings Are Close
# meduim
# https://leetcode.com/problems/determine-if-two-strings-are-close

from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        c1 = Counter(word1)
        c2 = Counter(word2)
        return len(Counter(c1.keys()) - Counter(c2.keys())) == 0 and len(Counter(c1.values()) - Counter(c2.values())) == 0
