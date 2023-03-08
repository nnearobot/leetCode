# 875. Koko Eating Bananas
# Medium
# https://leetcode.com/problems/koko-eating-bananas

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        minPile = 1
        maxPile = max(piles)
        while maxPile > minPile:
            testCount = minPile + (maxPile - minPile) // 2
            testH = 0
            for curPileCount in piles:
                testH += 1 if curPileCount < testCount else math.ceil(curPileCount / testCount)
            if testH > h:
                minPile = testCount + 1
            else:
                maxPile = testCount

        return minPile