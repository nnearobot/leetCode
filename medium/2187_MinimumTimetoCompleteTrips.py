"""
2187. Minimum Time to Complete Trips
Medium
https://leetcode.com/problems/minimum-time-to-complete-trips

"""
class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        s = 1
        e = max(time) * totalTrips
        res = 0
        while e > s:
            timeCount = s + (e - s) // 2
            tripCount = 0
            for i in time:
                tripCount += timeCount // i
            if tripCount >= totalTrips:
                e = timeCount
            else:
                s = timeCount + 1
        return s