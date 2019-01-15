func alphabeticShift(inputString string) string {
	var result string

	for _, s := range inputString {
		if s == 122 {
			result += "a"
		} else {
			result += string(s + 1)
		}
	}

	return result
}
