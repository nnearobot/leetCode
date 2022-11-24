// 1329. Sort the Matrix Diagonally
// A matrix diagonal is a diagonal line of cells starting from some cell in either the topmost row
// or leftmost column and going in the bottom-right direction until reaching the matrix's end.
// For example, the matrix diagonal starting from mat[2][0], where mat is a 6 x 3 matrix,
// includes cells mat[2][0], mat[3][1], and mat[4][2].
//
// Given an m x n matrix mat of integers, sort each matrix diagonal in ascending order and return the resulting matrix.
package main

import (
	"fmt"
	"sort"
)

func main() {
	fmt.Println(diagonalSort([][]int{
		{3, 3, 1, 1},
		{2, 2, 1, 2},
		{1, 1, 1, 2},
	}))
	// [[1,1,1,1],[1,2,2,2],[1,2,3,3]]

	fmt.Println(diagonalSort([][]int{
		{11, 25, 66, 1, 69, 7},
		{23, 55, 17, 45, 15, 52},
		{75, 31, 36, 44, 58, 8},
		{22, 27, 33, 25, 68, 4},
		{84, 28, 14, 11, 5, 50},
	}))
	//[[5,17,4,1,52,7],[11,11,25,45,8,69],[14,23,25,44,58,15],[22,27,31,36,50,66],[84,28,75,33,55,68]]
}

func diagonalSort(mat [][]int) [][]int {
	// if at least one of slice's dimention is less than 2, then this matrix is already diag sorted
	if len(mat) < 2 || len(mat[0]) < 2 {
		return mat
	}

	m := len(mat)
	n := len(mat[0])

	var diagArr = make([]int, 0, m)
	var beginRow, beginCol int = m - 1, 0
	var curRow, curCol int

	// for all diagonals
	for {
		// if current diagonal is the first (left) diagonal of the matrix, it has only 1 item, so it is sorted - go to next diagonal
		if beginRow == m-1 && beginCol == 0 {
			beginRow--
			continue
		}

		curRow = beginRow
		curCol = beginCol

		// select diag items
		diagArr = diagArr[:0]
		for {
			diagArr = append(diagArr, mat[curRow][curCol])
			// if current item is the last item of current diagonal, this diagonal is full
			if curRow == m-1 || curCol == n-1 {
				break
			}

			// go to next item of current diagonal
			curRow++
			curCol++
		}

		// sort diagArr array
		sort.Ints(diagArr)

		// fill diag with sorted items
		curRow = beginRow
		curCol = beginCol
		for i := 0; i < len(diagArr); i++ {
			mat[curRow][curCol] = diagArr[i]
			curRow++
			curCol++
		}

		// go to the next diagonal
		if beginRow > 0 {
			beginRow--
		} else {
			beginCol++
		}

		// if current diagonal is the last (right) diagonal of the matrix, it has only 1 item, so it is sorted - finish processing
		if beginRow == 0 && beginCol == n-1 {
			break
		}
	}

	return mat
}
