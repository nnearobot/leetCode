package main

type UnionFind struct {
    root     []int
    rank     []int
    setCount int
}

func DisjointSet(size int) *UnionFind {
    root := make([]int, size)
    rank := make([]int, size)
    for i := 0; i < size; i++ {
        root[i] = i
        rank[i] = 1
    }
    return &UnionFind{root, rank, size}
}

func (ds *UnionFind) Find(node int) int {
    if node != ds.root[node] {
        ds.root[node] = ds.Find(ds.root[node])
    }
    return ds.root[node]
}

func (ds *UnionFind) Union(node1, node2 int) {
    root1 := ds.Find(node1)
    root2 := ds.Find(node2)
    if root1 == root2 {
        return
    }
    if ds.rank[root1] > ds.rank[root2] {
        ds.root[root2] = root1
    } else if ds.rank[root1] < ds.rank[root2] {
        ds.root[root1] = root2
    } else {
        ds.root[root1] = root2
        ds.rank[root2]++
    }
    ds.setCount--
}

func (ds *UnionFind) getSetCount() int {
    return ds.setCount
}

func makeDS(edges [][]int) int {
    n := len(edges)
    ds := DisjointSet(n)
    for _, edge := range edges {
        ds.Union(edge[0], edge[1])
    }

    return ds.getSetCount()
}
