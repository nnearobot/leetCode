# 1496. Path Crossing
# easy
# https://leetcode.com/problems/path-crossing/

class Solution:
    def isPathCrossing(self, path: str) -> bool:
        vectors = {
            "N": (0, 1),
            "S": (0, -1),
            "E": (1, 0),
            "W": (-1, 0)
        }
        points = set()
        current_point = (0, 0)
        for direction in path:
            points.add(current_point)
            current_point = (current_point[0] + vectors[direction][0], current_point[1] + vectors[direction][1])
            if current_point in points:
                return True
        return False
