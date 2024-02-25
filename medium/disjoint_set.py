class DisjointSet:
    def __init__(self, size: int):
        self.root = [i for i in range(size)]
        self.rank = [0] * size
        self.setCount = size

    def find(self, node: int) -> int:
        if self.root[node] != node:
            self.root[node] = self.find(self.root[node])
        return self.root[node]

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
            self.rank[root1] += 1
            self.root[root2] = root1
        self.setCount -= 1
    
    def getSetCount(self) -> int:
        return self.setCount



def makeDS(edges: List[List[int]]) -> int:
    n = len(edges)
    ds = DisjointSet(n)
    for edge in edges:
        ds.union(edge[0], edge[1])

    setCount = ds.getSetCount()
    return setCount
