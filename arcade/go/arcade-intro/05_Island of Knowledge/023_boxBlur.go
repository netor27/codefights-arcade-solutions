func boxBlur(image [][]int) [][]int {
	result := [][]int{}
	for row := 1; row < len(image)-1; row++ {
		result = append(result, []int{})
		for col := 1; col < len(image[row])-1; col++ {
			result[row-1] = append(result[row-1], getBoxAverage(image, row, col))
		}
	}
	return result
}

func getBoxAverage(image [][]int, row int, col int) int {
	sum := 0
	for i := row - 1; i < row+2; i++ {
		for j := col - 1; j < col+2; j++ {
			sum += image[i][j]
		}
	}
	return sum / 9
}
