# 1578. Minimum Time to Make Rope Colorful
# medium
# https://leetcode.com/problems/minimum-time-to-make-rope-colorful

class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        prev_point = 0
        batch_time = 0
        batch_max_time = 0
        total_time = 0
        n = len(colors)
        for i in range(n + 1):
            if i == n or colors[i] != colors[prev_point]:
                if i - prev_point > 1:
                    total_time += batch_time - batch_max_time
                batch_max_time = neededTime[i] if i < n else 0
                batch_time = batch_max_time
                prev_point = i
            else:
                batch_time += neededTime[i]
                batch_max_time = max(batch_max_time, neededTime[i])
        return total_time
