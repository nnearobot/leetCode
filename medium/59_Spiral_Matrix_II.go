# 59. Spiral Matrix II
# medium
# https://leetcode.com/problems/spiral-matrix-ii

func generateMatrix(n int) [][]int {
    res := make([][]int, n)
    for i := 0; i < n; i++ {
        res[i] = make([]int, n)
    }
    i, j := 0, 0
    horiz := true
    d := 1 // direction: +1 or -1
    for num := 1; num <= n*n; num++ {
        res[i][j] = num
        if horiz {
            if j + d >= n || j + d < 0 || res[i][j + d] > 0 {
                horiz = false
                i += d
            } else {
                j += d
            }
        } else {
            if i + d >= n || i + d < 0 || res[i + d][j] > 0 {
                horiz = true
                d *= -1
                j += d
            } else {
                i += d
            }
        }
    }

    return res
}
