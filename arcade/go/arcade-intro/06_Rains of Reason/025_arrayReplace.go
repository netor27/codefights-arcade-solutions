func arrayReplace(inputArray []int, elemToReplace int, substitutionElem int) []int {
	for i := range inputArray {
		if inputArray[i] == elemToReplace {
			inputArray[i] = substitutionElem
		}
	}

	return inputArray
}
