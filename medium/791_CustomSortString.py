# 791. Custom Sort String
# medium
# https://leetcode.com/problems/custom-sort-string

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        counts = collections.defaultdict(int)
        for letter in s:
            counts[letter] += 1
        res = ""
        for letter in order:
            res += letter * counts[letter]
            counts[letter] = 0
        for letter in counts:
            if counts[letter]:
                res += letter * counts[letter]
        
        return res