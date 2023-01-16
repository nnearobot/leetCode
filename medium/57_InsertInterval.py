"""
57. Insert Interval
Medium
https://leetcode.com/problems/insert-interval/

"""

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]

        ind1 = -1
        ind2 = len(intervals)
        for ind, i in enumerate(intervals):
            if newInterval[0] > i[1]:
                ind1 = ind
            if ind2 == len(intervals) and newInterval[1] < i[0]:
                ind2 = ind

        res = []
        if ind1 > -1:
            res += intervals[:ind1 + 1]

        if ind1 == len(intervals) - 1 or ind2 == 0:
            res += [newInterval]
        else:
            i1 = newInterval[0] if newInterval[0] <= intervals[ind1 + 1][0] else intervals[ind1 + 1][0]
            i2 = newInterval[1] if newInterval[1] >= intervals[ind2 - 1][1] else intervals[ind2 - 1][1]
            res += [[i1, i2]]

        if ind2 < len(intervals):
            res += intervals[ind2:]

        return res