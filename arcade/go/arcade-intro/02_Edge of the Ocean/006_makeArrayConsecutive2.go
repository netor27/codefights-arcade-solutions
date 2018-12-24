func makeArrayConsecutive2(statues []int) int {
	if len(statues) == 0 {
		return 0
	}

	minValue := statues[0]
	maxValue := statues[0]
	for i := 1; i < len(statues); i++ {
		if statues[i] < minValue {
			minValue = statues[i]
		}

		if statues[i] > maxValue {
			maxValue = statues[i]
		}
	}

	return maxValue - minValue - len(statues) + 1
}
