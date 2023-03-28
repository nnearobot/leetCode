# 2360. Longest Cycle in a Graph
# medium
# https://leetcode.com/problems/longest-cycle-in-a-graph/


class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        while True:
            cycles = [-1 for _ in range(len(edges))]
            for i, child in enumerate(edges):
                if child > -1 and edges[child] > -1:
                    cycles[child] = edges[child]
            if cycles.count(-1) == edges.count(-1):
                break
            edges = cycles

        taken = [False for i in range(len(edges))]
        q = []
        for i, cycle in enumerate(cycles):
            if cycle > -1:
                q.append([i, i, 1])
                taken[i] = True
                break

        longestCycleLen = -1
        while len(q) > 0:
            curNode, firstNode, cycleLen = q.pop(0)
            childNode = edges[curNode]
            taken[childNode] = True
            if edges[childNode] > -1:
                if childNode == firstNode:
                    longestCycleLen = max(longestCycleLen, cycleLen)
                else:
                    q.append([childNode, firstNode, cycleLen + 1])
            if len(q) == 0:
                for i, cycle in enumerate(cycles):
                    if cycle> -1 and not taken[i]:
                        q.append([i, i, 1])
                        taken[i] = True
                        break

        return longestCycleLen