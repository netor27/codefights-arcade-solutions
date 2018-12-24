func almostIncreasingSequence(sequence []int) bool {
	j := analizeArray(sequence)
	if j == -1 {
		return true
	}

	b := make([]int, len(sequence))
	copy(b, sequence)
	if analizeArray(append(b[:j], b[j+1:]...)) == -1 {
		return true
	}

	b = make([]int, len(sequence))
	copy(b, sequence)
	if analizeArray(append(b[:j+1], b[j+2:]...)) == -1 {
		return true
	}

	return false
}

func analizeArray(array []int) int {
	// Returns the first index of a pair of elements where the earlier element
	// is not less than the later elements. If no such pair exists, return -1.'''
	for i := 0; i < len(array)-1; i++ {
		if array[i] >= array[i+1] {
			return i
		}
	}
	return -1
}
