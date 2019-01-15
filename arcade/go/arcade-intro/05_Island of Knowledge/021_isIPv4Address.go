import "strings"

func isIPv4Address(inputString string) bool {
	splitted := strings.Split(inputString, ".")
	if len(splitted) != 4 {
		return false
	}

	for _, s := range splitted {
		i, err := strconv.Atoi(s)
		if err != nil {
			return false
		}
		if i < 0 || i > 255 {
			return false
		}
	}

	return true
}
