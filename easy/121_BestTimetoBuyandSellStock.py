# 121. Best Time to Buy and Sell Stock
# Easy
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cur = prices[0]
        res = 0
        for i, price in enumerate(prices):
            if i == 0:
                continue
            res = max(res, price - cur)
            cur = min(cur, price)
        return res