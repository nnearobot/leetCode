// https://app.codesignal.com/challenge/RwtqyziacTBFJ9Tvm

func solution(grid []int, wires [][]int) int {
    var boundariesX = map[int][]int{}
    var boundariesY = map[int][]int{}
    
    for _, data := range wires {
        if data[0] == data[2] {
            for i := data[1]; i < data[3]; i++ {
                boundariesX[data[0]] = append(boundariesX[data[0]], i)
            }
        } else {
            for i := data[0]; i < data[2]; i++ {
                boundariesY[data[1]] = append(boundariesY[data[1]], i)
            }
        }
    }
    
    var qty, row, col int
    
    for x := 0; x < grid[0]; x++ {
        for
    }
    
}
