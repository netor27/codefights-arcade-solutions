func minesweeper(matrix [][]bool) [][]int {
	result := [][]int{}

	for row := 0; row < len(matrix); row++ {
		result = append(result, []int{})
		for col := 0; col < len(matrix[row]); col++ {
			result[row] = append(result[row], countMines(matrix, row, col))
		}
	}

	return result
}

func countMines(matrix [][]bool, row int, col int) int {
	count := 0
	for i := row - 1; i < row+2; i++ {
		for j := col - 1; j < col+2; j++ {
			if i >= 0 && i < len(matrix) && j >= 0 && j < len(matrix[row]) {
				if matrix[i][j] && (row != i || col != j) {
					count++
				}
			}
		}
	}
	return count
}
