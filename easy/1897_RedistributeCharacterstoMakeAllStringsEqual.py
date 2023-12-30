# 1897. Redistribute Characters to Make All Strings Equal
# easy
# https://leetcode.com/problems/redistribute-characters-to-make-all-strings-equal

import collections

class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        letterMap = collections.defaultdict(int)
        n = len(words)
        for word in words:
            for letter in word:
                letterMap[letter] += 1
        for letterCount in letterMap.values():
            if letterCount % n > 0:
                return False
        return True
        