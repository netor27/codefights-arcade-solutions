func commonCharacterCount(s1 string, s2 string) int {

	var code [26]int

	base := 97
	count := 0

	for _, s := range s1 {
		code[int(s)-base]++
	}

	for _, s := range s2 {
		if code[int(s)-base] > 0 {
			count++
			code[int(s)-base]--
		}
	}

	return count
}
