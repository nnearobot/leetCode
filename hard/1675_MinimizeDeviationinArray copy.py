# 1402. Reducing Dishes
# Hard
# https://leetcode.com/problems/reducing-dishes

class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        n = len(satisfaction)
        satisfaction = sorted(satisfaction)
        
        maxSatisfaction = 0
        satSum = 0
        for i in range(n - 1, -1, -1):
            if satSum + satisfaction[i] < 0:
                break
            satSum += satisfaction[i]
            maxSatisfaction += satSum
        return maxSatisfaction
