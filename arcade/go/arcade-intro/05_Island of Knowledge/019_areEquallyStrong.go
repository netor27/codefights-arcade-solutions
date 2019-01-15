func areEquallyStrong(yourLeft int, yourRight int, friendsLeft int, friendsRight int) bool {
	if (yourLeft == friendsLeft && yourRight == friendsRight) || (yourLeft == friendsRight && yourRight == friendsLeft) {
		return true
	}

	return false
}
