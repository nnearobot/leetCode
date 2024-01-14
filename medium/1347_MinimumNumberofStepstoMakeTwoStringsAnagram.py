# 1347. Minimum Number of Steps to Make Two Strings Anagram
# medium
# https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        letterMap = collections.defaultdict(int)
        for letter in s:
            letterMap[letter] += 1
        res = 0
        for letter in t:
            if letter in letterMap and letterMap[letter] > 0:
                letterMap[letter] -= 1
            else:
                res += 1
        return res
  