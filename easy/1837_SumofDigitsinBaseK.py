# 1837. Sum of Digits in Base K
# Easy
# https://leetcode.com/problems/sum-of-digits-in-base-k/

class Solution:
    def sumBase(self, n: int, k: int) -> int:
        if n == 0:
            return 0
        res = 0
        while n:
            rem = n % k
            n //= k
            res += rem
        return res