func allLongestStrings(inputArray []string) []string {
	var result []string

	if len(inputArray) == 0 {
		return result
	}

	maxLength := -1
	for _, s := range inputArray {
		if len(s) == maxLength {
			result = append(result, s)
		} else if len(s) > maxLength {
			result = []string{s}
			maxLength = len(s)
		}
	}

	return result
}
