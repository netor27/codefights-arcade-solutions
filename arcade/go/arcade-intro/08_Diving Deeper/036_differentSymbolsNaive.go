func differentSymbolsNaive(s string) int {
	m := map[int]bool{}
	for _, s := range s {
		m[int(s)] = true
	}

	return len(m)
}
