# 1971. Find if Path Exists in Graph
# Easy
# https://leetcode.com/problems/find-if-path-exists-in-graph/description/

class DS:
    def __init__(self, size) -> None:
        self.root = [i for i in range(size)]
        self.rank = [1] * size
    
    def find(self, node) -> int:
        if node == self.root[node]:
            return node
        self.root[node] = self.find(self.root[node])
        return self.root[node]

    def union(self, node1, node2) -> None:
        root1 = self.find(node1)
        root2 = self.find(node2)
        if root1 == root2:
            return
        if self.rank[root1] > self.rank[root2]:
            self.root[root2] = root1
        elif self.rank[root1] < self.rank[root2]:
            self.root[root1] = root2
        else:
            self.root[root1] = root2
            self.rank[root2] += 1
    
    def connected(self, node1, node2) -> bool:
        return self.find(node1) == self.find(node2)

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if n == 1:
            return True

        ds = DS(n)
        for edge in edges:
            ds.union(edge[0], edge[1])
        return ds.connected(source, destination)
