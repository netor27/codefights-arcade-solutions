func depositProfit(deposit int, rate int, threshold int) int {
	balance := float64(deposit)
	years := 0
	maxValue := float64(threshold)

	for balance < maxValue {
		years++
		balance += (float64(rate) / 100.0) * balance
		fmt.Print(balance, "\n")
	}

	return years
}
