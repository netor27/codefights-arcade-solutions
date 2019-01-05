func alternatingSums(a []int) []int {
	isFirstTeam := true
	result := []int{0, 0}

	for _, item := range a {
		if isFirstTeam {
			result[0] += item
		} else {
			result[1] += item
		}
		isFirstTeam = !isFirstTeam
	}

	return result
}
