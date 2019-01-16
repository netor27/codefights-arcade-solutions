func extractEachKth(inputArray []int, k int) []int {
	current := 1
	result := []int{}

	for i := range inputArray {
		if current%k != 0 {
			result = append(result, inputArray[i])
		}
		current++
	}

	return result
}
