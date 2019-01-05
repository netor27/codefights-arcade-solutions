import "sort"

func sortByHeight(a []int) []int {
	var people []int
	var result []int

	for _, item := range a {
		if item != -1 {
			people = append(people, item)
		}
	}

	sort.Ints(people)
	currentIndex := 0
	for _, item := range a {
		if item == -1 {
			result = append(result, -1)
		} else {
			result = append(result, people[currentIndex])
			currentIndex++
		}
	}

	return result
}
