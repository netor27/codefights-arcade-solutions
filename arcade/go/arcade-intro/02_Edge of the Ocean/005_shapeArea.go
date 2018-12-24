import (
	"math"
)

func shapeArea(n int) int {
	x := float64(n)
	return int(math.Pow(x, 2) + math.Pow(x-1, 2))
}
