func variableName(name string) bool {
	if len(name) <= 0 {
		return false
	}

	// check if first char is a number
	if name[0] >= 48 && name[0] <= 57 {
		return false
	}

	for _, s := range name {
		if s != 95 && !(s >= 65 && s <= 90) && !(s >= 97 && s <= 122) && !(s >= 48 && s <= 57) {
			return false
		}
	}
	return true
}
