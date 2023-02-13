"""
122. Best Time to Buy and Sell Stock II
Medium
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii

"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curMin = prices[0]
        total = 0
        for i, price in enumerate(prices):
            if i == 0:
                continue

            if (price > curMin):
                total += price - curMin
                curMin = price
            else:
                curMin = min(curMin, price)
        return total
