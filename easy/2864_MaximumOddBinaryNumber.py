# 2864. Maximum Odd Binary Number
# easy
# https://leetcode.com/problems/maximum-odd-binary-number/

class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        ones = s.count('1')
        n = len(s)
        return '1' * (ones - 1) + '0' * (n - ones) + '1'