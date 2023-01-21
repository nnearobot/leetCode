"""
261. Graph Valid Tree
Medium
https://leetcode.com/problems/graph-valid-tree/description/

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

    def union(self, node1, node2) -> bool:
        root1 = self.find(node1)
        root2 = self.find(node2)
        if root1 == root2:
            return False
        if self.rank[root1] > self.rank[root2]:
            self.root[root2] = root1
        elif self.rank[root1] < self.rank[root2]:
            self.root[root1] = root2
        else:
            self.root[root1] = root2
            self.rank[root2] += 1
        self.rootCount -= 1
        return True
    
    def connected(self, node1, node2) -> bool:
        return self.find(node1) == self.find(node2)
    
    def getRootCount(self) -> int:
        return self.rootCount


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        ds = DS(n)

        for edge in edges:
            connected = ds.union(edge[0], edge[1])
            if not connected:
                return False
        
        return True if ds.getRootCount() == 1 else False

