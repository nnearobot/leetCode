# 11. Container With Most Water
# Medium
# https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        vol = 0
        for i in range(len(height) - 1):
            for j in range(len(height) - 1, i, -1):
                h = min(height[i], height[j])
                s = h * (j - i)
                vol = max(vol, s)
        return vol
