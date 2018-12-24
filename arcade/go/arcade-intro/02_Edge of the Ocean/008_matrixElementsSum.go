func matrixElementsSum(matrix [][]int) int {
	total := 0
	columns := len(matrix[0])
	rows := len(matrix)

	for y := 0; y < columns; y++ {
		for x := 0; x < rows; x++ {
			if matrix[x][y] == 0 {
				break
			}

			total = total + matrix[x][y]
		}
	}

	return total
}
