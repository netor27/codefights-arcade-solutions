func evenDigitsOnly(n int) bool {
	current := n
	for current > 0 {
		if current%2 != 0 {
			return false
		}
		current = current / 10
	}

	return true
}
