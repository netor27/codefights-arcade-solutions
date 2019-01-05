func areSimilar(a []int, b []int) bool {
	if len(a) != len(b) {
		return false
	}

	var diff []int
	numOfErrors := 0
	for i := range a {
		if a[i] != b[i] {
			numOfErrors += 1
			if numOfErrors == 1 {
				diff = append(diff, a[i])
				diff = append(diff, a[i])
			} else if numOfErrors == 2 {
				if diff[0] != b[i] || diff[1] != a[i] {
					return false
				}
			} else {
				return false
			}
		}
	}

	return true
}
