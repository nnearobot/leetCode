# 1232. Check If It Is a Straight Line
# Easy
# https://leetcode.com/problems/check-if-it-is-a-straight-line

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        prevTg = None
        basePoint = coordinates[0]
        for i in range(1, len(coordinates)):
            point = coordinates[i]
            if point[0] == basePoint[0]:
                tg = math.inf
            else:
                tg = (point[1] - basePoint[1]) / (point[0] - basePoint[0])
            if prevTg is None:
                prevTg = tg
            elif tg != prevTg:
                return False
        return True
