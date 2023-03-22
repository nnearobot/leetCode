// 2492. Minimum Score of a Path Between Two Cities
// medium
// https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/

package main

type UnionFind struct {
	root []int
	rank []int
}

func DisjointSet(size int) *UnionFind {
	root := make([]int, size)
	rank := make([]int, size)
	for i := 0; i < size; i++ {
		root[i] = i
		rank[i] = 1
	}
	return &UnionFind{root, rank}
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
}

func minScore(n int, roads [][]int) int {
	ds := DisjointSet(n + 1)
	minScore := 0
	for _, road := range roads {
		ds.Union(road[0], road[1])
		if road[2] > minScore {
			minScore = road[2]
		}
	}

	root1 := ds.Find(1)

	for _, road := range roads {
		if root1 == ds.Find(road[0]) {
			if road[2] < minScore {
				minScore = road[2]
			}
		}
	}

	return minScore
}
