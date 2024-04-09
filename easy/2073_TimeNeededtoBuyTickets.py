# 2073. Time Needed to Buy Tickets
# easy
# https://leetcode.com/problems/time-needed-to-buy-tickets/

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        k_need = tickets[k]
        if k_need == 1:
            return k + 1
        res = 0
        for i, count in enumerate(tickets):
            need = k_need if i <= k else k_need - 1
            res += count if count < need else need
        
        return res