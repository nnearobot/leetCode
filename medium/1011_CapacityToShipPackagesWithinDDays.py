# 1011. Capacity To Ship Packages Within D Days
# Medium
# https://leetcode.com/problems/capacity-to-ship-packages-within-d-days

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        maxCap = sum(weights)

        if days == 1:
            return sum(weights)
        
        minCap = max(max(weights), math.ceil(maxCap / days))
        print(minCap)

        def canShip(cap) -> bool:
            dayLeft = days
            containerFill = 0
            for weight in weights:
                if weight > cap - containerFill:
                    dayLeft -= 1
                    if dayLeft == 0:
                        return False
                    containerFill = weight
                else:
                    containerFill += weight
            return True

        while maxCap > minCap:
            midCap = minCap + (maxCap - minCap) // 2
            if canShip(midCap):
                maxCap = midCap
            else:
                minCap = midCap + 1
        
        return minCap