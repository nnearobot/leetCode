# 1637. Widest Vertical Area Between Two Points Containing No Points
# medium
# https://leetcode.com/problems/widest-vertical-area-between-two-points-containing-no-points/

class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        sorted_points = sorted(points, key=lambda x: x[0])

        prev_x = sorted_points[0][0]
        width = 0
        for point in sorted_points:
            width = max(width, point[0] - prev_x)
            prev_x = point[0]
        
        return width
        