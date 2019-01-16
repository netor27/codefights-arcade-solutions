func stringsRearrangement(inputArray []string) bool {
	totalLen := len(inputArray)
	for i := range inputArray {
		if analizeElement(inputArray[i], getSliceWithoutNthElement(inputArray, i), 1, totalLen) {
			return true
		}
	}

	return false
}

func getSliceWithoutNthElement(a []string, n int) []string {
	cp := make([]string, len(a))
	copy(cp, a)
	b := append(cp[:n], cp[n+1:]...)
	return b
}

func analizeElement(item string, array []string, step int, totalLen int) bool {
	if step == totalLen {
		return true
	}

	for i := range array {
		count := 0
		for j := range item {
			if item[j] != array[i][j] {
				count++
			}
		}

		if count == 1 {
			if analizeElement(array[i], getSliceWithoutNthElement(array, i), step+1, totalLen) {
				return true
			}
		}
	}
	return false
}
