// 2316. Count Unreachable Pairs of Nodes in an Undirected Graph
// medium
// https://leetcode.com/problems/number-of-operations-to-make-network-connected/

package main

type UnionFind struct {
	root             []int
	rank             []int
	setVol           map[int]int64
	unreachablePairs int64
}

func DisjointSet(size int) *UnionFind {
	root := make([]int, size)
	rank := make([]int, size)
	setVol := map[int]int64{}
	unreachablePairs := int64((size - 1) * size / 2)
	for i := 0; i < size; i++ {
		root[i] = i
		rank[i] = 1
		setVol[i] = 1
	}
	return &UnionFind{root, rank, setVol, unreachablePairs}
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

	ds.unreachablePairs -= ds.setVol[root1] * ds.setVol[root2]

	if ds.rank[root1] > ds.rank[root2] {
		ds.root[root2] = root1
		ds.setVol[root1] += ds.setVol[root2]
		ds.setVol[root2] = 0
	} else {
		ds.root[root1] = root2
		ds.setVol[root2] += ds.setVol[root1]
		ds.setVol[root1] = 0
	}

	if ds.rank[root1] < ds.rank[root2] {
		ds.rank[root2]++
	}
}

func (ds *UnionFind) getUnreachablePairsCount() int64 {
	return ds.unreachablePairs
}

func countPairs(n int, edges [][]int) int64 {
	ds := DisjointSet(n)
	for _, edge := range edges {
		ds.Union(edge[0], edge[1])
	}

	return ds.getUnreachablePairsCount()
}
