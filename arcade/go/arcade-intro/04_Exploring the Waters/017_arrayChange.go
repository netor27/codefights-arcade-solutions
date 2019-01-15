func arrayChange(inputArray []int) int {

	numberOfMoves := 0
	currentNumber := inputArray[0]
	for i := 1; i < len(inputArray); i++ {
		if currentNumber >= inputArray[i] {
			numberOfMoves += currentNumber - inputArray[i] + 1
			currentNumber += 1
		} else {
			currentNumber = inputArray[i]
		}
	}

	return numberOfMoves
}
