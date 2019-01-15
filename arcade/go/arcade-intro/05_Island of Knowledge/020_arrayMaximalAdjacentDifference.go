func arrayMaximalAdjacentDifference(inputArray []int) int {
	maxDif := 0
	for i := 0; i < len(inputArray)-1; i++ {
		dif := inputArray[i] - inputArray[i+1]
		if dif < 0 {
			dif = -dif
		}

		if dif > maxDif {
			maxDif = dif
		}
	}

	return maxDif
}
