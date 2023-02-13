"""
1014. Best Sightseeing Pair
Medium
https://leetcode.com/problems/best-sightseeing-pair
"""

class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        cur = res = 0
        for value in values:
            res = max(res, cur + value)
            cur = max(cur, value) - 1
        return res