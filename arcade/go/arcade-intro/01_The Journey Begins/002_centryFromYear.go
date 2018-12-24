func centuryFromYear(year int) int {
	x := year / 100
	if year%100 == 0 {
		return x
	}

	return x + 1
}
