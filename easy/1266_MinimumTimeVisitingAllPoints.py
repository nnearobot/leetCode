# 1266. Minimum Time Visiting All Points
# easy
# https://leetcode.com/problems/minimum-time-visiting-all-points/

class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        total_path = 0
        for i in range(1, len(points)):
            point1 = points[i - 1]
            point2 = points[i]
            if point1[0] == point2[0] and point1[1] == point2[1]:
                continue
            dx = abs(point1[0] - point2[0])
            dy = abs(point1[1] - point2[1])
            if dx == dy:
                s = dx
            else:
                diag = min(dx, dy)
                straight = dx - diag if dx > dy else dy - diag
                s = straight + diag
            total_path += s
        return total_path
