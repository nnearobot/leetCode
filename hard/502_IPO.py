# 502. IPO
# Hard
# https://leetcode.com/problems/ipo

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n = len(profits)
        if k > n:
            return sum(profits) + w

        projects = list(zip(capital, profits))
        projects.sort()

        q = []
        project = 0
        totalCap = w
        for i in range(k):
            while project < n and projects[project][0] <= totalCap:
                heappush(q, -projects[project][1])
                project += 1
            if not q:
                break
            totalCap += -heappop(q)

        return totalCap