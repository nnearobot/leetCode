"""
120. Triangle
Medium
https://leetcode.com/problems/triangle
"""
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = triangle.copy()
        dp[0][0] = triangle[0][0]
        res = triangle[0][0]
        for row in range(1, n):
            if row == n - 1:
                res = math.inf
            for i in range(len(triangle[row])):
                left = triangle[row - 1][i - 1] if i > 0 else math.inf
                right = triangle[row - 1][i] if i < len(triangle[row - 1]) else math.inf
                dp[row][i] = int(min(left, right)) + triangle[row][i]
                if row == n - 1:
                    res = min(res, dp[row][i])

        return res