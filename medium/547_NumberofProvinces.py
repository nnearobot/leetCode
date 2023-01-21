"""
547. Number of Provinces
Medium
https://leetcode.com/problems/number-of-provinces/description/

"""

class DS:
    def __init__(self, size) -> None:
        self.root = [i for i in range(size)]
        self.rank = [1] * size
        self.rootCount = size
    
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
        self.rootCount -= 1
    
    def connected(self, node1, node2) -> bool:
        return self.find(node1) == self.find(node2)
    
    def getRootCount(self) -> int:
        return self.rootCount

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        ds = DS(len(isConnected))

        for row, cols in enumerate(isConnected):
            for col, val in enumerate(cols):
                if val == 1:
                    ds.union(row, col)
        
        return ds.getRootCount()
        