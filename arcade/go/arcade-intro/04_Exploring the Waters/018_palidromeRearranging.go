func palindromeRearranging(inputString string) bool {
	var charsCount [256]int

	for _, s := range inputString {
		charsCount[s] += 1
	}

	foundOdd := false
	for _, i := range charsCount {
		if i%2 != 0 {
			if foundOdd {
				return false
			}
			foundOdd = true
		}
	}

	return true
}
