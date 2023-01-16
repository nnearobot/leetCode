# 2421. Number of Good Paths
# Hard
# https://leetcode.com/problems/number-of-good-paths/description/

class UnionFind:
    def __init__(self, size: int):
        self.root = [i for i in range(size)]
        self.rank = [1] * size

    def find(self, node: int) -> int:
        while node != self.root[node]:
            node = self.root[node]
        return node

    def union(self, node1: int, node2: int):
        root1 = self.find(node1)
        root2 = self.find(node2)
        if root1 == root2:
            return
        if self.rank[root1] > self.rank[root2]:
            self.root[root2] = root1
        elif self.rank[root1] < self.rank[root2]:
            self.root[root1] = root2
        else:
            self.root[root2] = root1
            self.rank[root1] += 1

    def connected(self, node1: int, node2: int) -> int:
        return self.find(node1) == self.find(node2)

class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for s, e in edges:
            adj[s].append(e)
            adj[e].append(s)

        nodesOfVals = defaultdict(list)
        for nodeNum, val in enumerate(vals):
            nodesOfVals[val].append(nodeNum)

        nodesOfValsKeys = list(nodesOfVals.keys())
        nodesOfValsKeys.sort()
        nodesOfVals = {i: nodesOfVals[i] for i in nodesOfValsKeys}
        
        goodPathCount = 0
        uf = UnionFind(len(vals))

        for val in nodesOfVals:
            for currNode in nodesOfVals[val]:
                print("    currNode =", currNode)
                for neighbor in adj.get(currNode, []):
                    if vals[currNode] >= vals[neighbor]:
                        print("        node =", neighbor)
                        uf.union(currNode, neighbor)
            group = {}
            for currNode in nodesOfVals[val]:
                root = uf.find(currNode)
                group[root] = group.get(root, 0) + 1
            for i in group:
                size = group[i]
                goodPathCount += int(size * (size + 1) / 2)
                
        return goodPathCount

