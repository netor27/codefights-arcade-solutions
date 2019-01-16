func firstDigit(inputString string) string {
	zeroCharValue := 48
	nineCharValue := 57

	for i := range inputString {
		if int(inputString[i]) >= zeroCharValue && int(inputString[i]) <= nineCharValue {
			return string(inputString[i])
		}
	}

	return "-"
}
