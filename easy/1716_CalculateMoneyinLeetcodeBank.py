# 1716. Calculate Money in Leetcode Bank
# easy
# https://leetcode.com/problems/calculate-money-in-leetcode-bank

class Solution:
    def totalMoney(self, n: int) -> int:
        weeks = n // 7
        days = n % 7
        return 28 * weeks + 7 * ((weeks - 1) * weeks) // 2 + ((days + 1) * days) // 2 + days * weeks