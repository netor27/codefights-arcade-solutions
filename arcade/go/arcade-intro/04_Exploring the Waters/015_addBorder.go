import "strings"

func addBorder(picture []string) []string {
	if len(picture) == 0 {
		return []string{"*"}
	}

	width := len(picture[0]) + 2

	var result []string
	result = append(result, strings.Repeat("*", width))
	for _, row := range picture {
		result = append(result, "*"+row+"*")
	}
	result = append(result, strings.Repeat("*", width))
	return result
}
