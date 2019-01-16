func knapsackLight(value1 int, weight1 int, value2 int, weight2 int, maxW int) int {
	// if we can grab both, sum the values
	if weight1+weight2 <= maxW {
		return value1 + value2
	}

	// if we can choose, return the one with the highest value
	if weight1 <= maxW && weight2 <= maxW {
		if value1 > value2 {
			return value1
		}
		return value2
	}

	// if we cannot choose, return the one we can carry
	if weight1 <= maxW {
		return value1
	}
	if weight2 <= maxW {
		return value2
	}

	// we cannot carry either, return 0
	return 0
}
