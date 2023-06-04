# 1376. Time Needed to Inform All Employees
# Medium
# https://leetcode.com/problems/time-needed-to-inform-all-employees

from collections import deque

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        subordinates = [[] for _ in range(n)]
        for empl_id, manager_id in enumerate(manager):
            if manager_id == -1:
                continue
            subordinates[manager_id].append(empl_id)

        q = deque()
        q.append((headID, 0))
        max_time = 0
        while q:
            (empl_id, prev_time) = q.popleft()
            if len(subordinates[empl_id]) == 0:
                max_time = max(max_time, prev_time)
                continue

            for subordinate in subordinates[empl_id]:
                q.append((subordinate, prev_time + informTime[empl_id]))

        return max_time

