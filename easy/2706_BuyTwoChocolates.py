# 2706. Buy Two Chocolates
# easy
# https://leetcode.com/problems/buy-two-chocolates

class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        min_sum = prices[0] + prices[1]
        return money - min_sum if min_sum <= money else money