func longestDigitsPrefix(inputString string) string {
	zeroRune := int("0"[0])
	nineRune := int("9"[0])

	prefix := ""

	for _, s := range inputString {
		if int(s) >= zeroRune && int(s) <= nineRune {
			prefix += string(s)
		} else {
			break
		}
	}

	return prefix
}
