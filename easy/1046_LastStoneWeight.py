# 1046. Last Stone Weight
# Easy
# https://leetcode.com/problems/last-stone-weight/

import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-i for i in stones]
        heapq.heapify(stones)
        while True:
            y = heapq.heappop(stones) if len(stones) > 0 else None
            x = heapq.heappop(stones) if len(stones) > 0 else None
            if not y or not x:
                break
            if x == y:
                continue
            heapq.heappush(stones, y - x)
        
        return -y if y != None else 0