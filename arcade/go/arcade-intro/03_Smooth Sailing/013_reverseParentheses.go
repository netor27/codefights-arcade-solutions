import "strings"

func reverseInParentheses(s string) string {
	var stack []int
	var start, end int
	l := strings.Split(s, "")

	for i, item := range l {
		if item == "(" {
			// we found the start of a sequence, push it to the stack
			stack = append(stack, i)
		} else if item == ")" {
			// we found the end of a sequence, we need to pop the start of this sequence and reverse this
			end = i
			start, stack = stack[len(stack)-1], stack[:len(stack)-1]
			// Add 1 to start, and substract 1 to end, because we don't need to reverse the parenthesis
			reversePartOfArray(start+1, end-1, l)
		}
	}

	var result []string
	for _, item := range l {
		if item != "(" && item != ")" {
			result = append(result, item)
		}
	}

	return strings.Join(result, "")
}

func reversePartOfArray(start int, end int, l []string) {
	for i, j := start, end; i < j; i, j = i+1, j-1 {
		l[i], l[j] = l[j], l[i]
	}
}