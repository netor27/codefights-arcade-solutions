func arrayMaxConsecutiveSum(inputArray []int, k int) int {
	currentMax := 0

	if k >= len(inputArray) {
		return 0
	}

	sum := 0
	previous := 0
	for i := range inputArray {
		if i > k-1 {
			sum -= inputArray[previous]
			previous++
		}

		sum += inputArray[i]
		if sum > currentMax {
			currentMax = sum
		}
	}
	return currentMax
}
