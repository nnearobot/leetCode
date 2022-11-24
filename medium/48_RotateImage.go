// 48. Rotate Image
// Medium
// You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
// You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
// DO NOT allocate another 2D matrix and do the rotation.
package main

import "fmt"

func main() {
	matrix := [][]int{{1, 2, 3}, {4, 5, 6}, {7, 8, 9}}
	rotate(matrix)
	fmt.Println(matrix) // [[7,4,1],[8,5,2],[9,6,3]]

	matrix = [][]int{{5, 1, 9, 11}, {2, 4, 8, 10}, {13, 3, 6, 7}, {15, 14, 12, 16}}
	rotate(matrix)
	fmt.Println(matrix) // [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
}

func rotate(matrix [][]int) {
	var i, j, tmp int
	n := len(matrix)

	for lvl := 0; lvl < n/2; lvl++ {
		i, j = lvl, lvl

		for s := 0; s < n-2*lvl-1; s++ {
			tmp = matrix[i][j]
			matrix[i][j] = matrix[n-1-j][i]
			matrix[n-1-j][i] = matrix[n-1-i][n-1-j]
			matrix[n-1-i][n-1-j] = matrix[j][n-1-i]
			matrix[j][n-1-i] = tmp
			j++
		}
	}
}

// 2x2: levels = 1; squares: 1
// 3x3: levels = 1; squares: 2
// 4x4: levels = 2; squares: 3, 1
// 5x5: levels = 2; squares: 4, 2
// 6x6: levels = 3; squares: 5, 3, 1
// 7x7: levels = 3; squares: 6, 4, 2

// n = 4

// 00; 01; 02; 03;
// 10; 11; 12; 13;
// 20; 21; 22; 23;
// 30; 31; 32; 33;

// 30; 20; 10; 00;
// 31; 21; 11; 01;
// 32; 22; 12; 02;
// 33; 23; 13; 03;

// i1j1 => ij
// 00 => 03; 01 => 13; 02 => 23; 03 => 33;
// 10 => 02; 11 => 12; 12 => 22; 13 => 32;
// 20 => 01; 21 => 11; 22 => 21; 23 => 31;
// 30 => 00; 31 => 10; 32 => 20; 33 => 30;

// i1 + j = 3 => i1 = 3 - j = n - 1 - j;
// j1 = i.
