func avoidObstacles(inputArray []int) int {
	// create a set of the obstacles and the hightest element
	max := 0
	obstacles := map[int]bool{}

	for _, i := range inputArray {
		if i > max {
			max = i
		}

		obstacles[i] = true
	}

	for i := 2; i < max+1; i++ {
		fmt.Printf("Checking jumping %v spaces\n", i)
		foundObstacle := false
		for j := 0; j <= max; j += i {
			_, hit := obstacles[j]
			if hit {
				foundObstacle = true
				break
			}
		}
		if !foundObstacle {
			return i
		}
	}

	return max + 1
}
