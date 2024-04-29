# 159. Longest Substring with At Most Two Distinct Characters
# medium
# https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/

class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        n = len(s)
        if n < 3:
            return n
        p1, p2 = 0, 2
        min_chars = 2
        while p2 < n:
            if s[p2] != s[p2 - 1]:
                for i in range(p2 - 2, p1 - 1, -1):
                    if s[i] != s[p2 - 1] and s[i] != s[p2]:
                        p1 = i + 1
                        break
            min_chars = max(min_chars, p2 - p1 + 1)
            p2 += 1
        return min_chars
