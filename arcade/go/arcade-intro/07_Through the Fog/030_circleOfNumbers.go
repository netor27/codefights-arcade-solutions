func circleOfNumbers(n int, firstNumber int) int {
	mid := n / 2
	return (firstNumber + mid) % n
}
