func digitDegree(n int) int {
	degree := 0
	sum := n
	for sum >= 10 {
		s := strconv.Itoa(sum)
		sum = 0
		for _, r := range s {
			i := int(r - '0')
			sum += i
		}
		degree++
		fmt.Println(sum)
	}

	return degree
}
