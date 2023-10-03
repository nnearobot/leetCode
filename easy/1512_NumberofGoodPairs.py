# 1512. Number of Good Pairs
# easy
# https://leetcode.com/problems/number-of-good-pairs

from collections import defaultdict

class Solution:
    def __init__(self) -> None:
        self.memo = defaultdict(int)
        
    def factorial(self, n):
        if n < 3:
            return n
        if not n in self.memo:
            self.memo[n] = 1
            for i in range(2, n + 1):
                self.memo[n] *= i

        return self.memo[n]
        

    def numIdenticalPairs(self, nums: List[int]) -> int:
        hashMap = defaultdict(int)
        for i, num in enumerate(nums):
            hashMap[num] += 1

        res = 0
        for i in hashMap:
            count = hashMap[i]
            if count < 2:
                continue
            elif count == 2:
                res += 1
            else:
                res += self.factorial(count) // (self.factorial(count - 2) * 2)
        return res

        
