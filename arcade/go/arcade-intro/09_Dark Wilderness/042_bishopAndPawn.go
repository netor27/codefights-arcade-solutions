func bishopAndPawn(bishop string, pawn string) bool {
	x1 := int(bishop[0])
	y1 := int(bishop[1])
	x2 := int(pawn[0])
	y2 := int(pawn[1])
	return abs(y1-y2) == abs(x1-x2)
}

func abs(i int) int {
	if i < 0 {
		return -i
	}
	return i
}
