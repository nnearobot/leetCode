# 1523. Count Odd Numbers in an Interval Range
# Easy
# https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/

import math
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return math.ceil(high / 2) - low // 2