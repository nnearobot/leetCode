// 200. Number of Islands
// Medium
// Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
// An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
// You may assume all four edges of the grid are all surrounded by water.
package main

import "fmt"

func main() {
	fmt.Println(numIslands([][]byte{
		{'1', '0', '1', '1', '1'},
		{'1', '0', '1', '0', '1'},
		{'1', '1', '1', '0', '1'},
	})) // 1

	fmt.Println(numIslands([][]byte{
		{'1', '1', '1', '1', '0'},
		{'1', '1', '0', '1', '0'},
		{'1', '1', '0', '0', '0'},
		{'0', '0', '0', '0', '0'},
	})) // 1

	fmt.Println(numIslands([][]byte{
		{'1', '1', '0', '0', '0'},
		{'1', '1', '0', '0', '0'},
		{'0', '0', '1', '0', '0'},
		{'0', '0', '0', '1', '1'},
	})) // 3
}

func numIslands(grid [][]byte) int {
	gridmap := make([][]bool, len(grid))
	for i := 0; i < len(grid); i++ {
		gridmap[i] = make([]bool, len(grid[0]))
	}

	var islandQty int

	for i := 0; i < len(grid); i++ {
		for j := 0; j < len(grid[0]); j++ {
			if gridmap[i][j] {
				continue
			}

			if grid[i][j] == byte('0') {
				gridmap[i][j] = true
				continue
			}

			islandQty++
			checkCell(i, j, grid, gridmap)
		}
	}

	return islandQty
}

func checkCell(i, j int, grid [][]byte, gridmap [][]bool) {
	gridmap[i][j] = true

	if i-1 >= 0 && !gridmap[i-1][j] {
		if grid[i-1][j] == byte('0') {
			gridmap[i-1][j] = true
		} else {
			checkCell(i-1, j, grid, gridmap)
		}
	}

	if j+1 < len(grid[0]) && !gridmap[i][j+1] {
		if grid[i][j+1] == byte('0') {
			gridmap[i][j+1] = true
		} else {
			checkCell(i, j+1, grid, gridmap)
		}
	}

	if i+1 < len(grid) && !gridmap[i+1][j] {
		if grid[i+1][j] == byte('0') {
			gridmap[i+1][j] = true
		} else {
			checkCell(i+1, j, grid, gridmap)
		}
	}

	if j-1 >= 0 && !gridmap[i][j-1] {
		if grid[i][j-1] == byte('0') {
			gridmap[i][j-1] = true
		} else {
			checkCell(i, j-1, grid, gridmap)
		}
	}
}
