func growingPlant(upSpeed int, downSpeed int, desiredHeight int) int {
	currentHeight := upSpeed
	count := 1

	for currentHeight < desiredHeight {
		currentHeight -= downSpeed
		currentHeight += upSpeed
		count += 1
	}

	return count
}
