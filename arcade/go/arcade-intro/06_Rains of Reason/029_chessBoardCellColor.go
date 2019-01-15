func chessBoardCellColor(cell1 string, cell2 string) bool {
	return isWhiteCell(cell1) == isWhiteCell(cell2)
}

func isWhiteCell(cell string) bool {
	x := cell[0] - 64
	y := cell[1] - 48

	isWhite := x%2 == 0
	if y%2 == 0 {
		isWhite = !isWhite
	}

	return isWhite
}
