# 191. Number of 1 Bits
# Easy
# https://leetcode.com/problems/number-of-1-bits

class Solution:
    def hammingWeight(self, n: int) -> int:
        return sum([int(i) for i in bin(n)[2:]])