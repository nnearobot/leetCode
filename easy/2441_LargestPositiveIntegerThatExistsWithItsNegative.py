# 2441. Largest Positive Integer That Exists With Its Negative
# easy
# https://leetcode.com/problems/largest-positive-integer-that-exists-with-its-negative/

class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        num_set = set()
        k = -1
        for num in nums:
            if 0 - num in num_set:
                k = max(k, abs(num))
            num_set.add(num)
        return k
