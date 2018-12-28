# Not implemented yet!func isLucky(n int) bool {
	s := fmt.Sprint(n)
	half := len(s) / 2
	firstHalfSum := 0
	secondHalfSum := 0

	for i:=0; i < half; i++ {
			firstHalfSum += int(s[i])
			secondHalfSum += int(s[len(s)-i-1])
	}

	return firstHalfSum == secondHalfSum
}
