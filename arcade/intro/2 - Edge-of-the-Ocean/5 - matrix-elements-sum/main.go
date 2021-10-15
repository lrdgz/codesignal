package main

func matrixElementsSum(matrix [][]int) int {
	cost := 0

	for i := 0; i < len(matrix); i++ {
		for j := 0; j < len(matrix[i]); j++ {
			if i == 0 {
				cost += matrix[i][j]
				continue
			}
			if matrix[i-1][j] == 0 {
				matrix[i][j] = 0
				continue
			}
			if matrix[i][j] > 0 {
				cost += matrix[i][j]
				continue
			}
		}
	}

	return cost
}

func main() {
	hotel := [][]int{
		{0, 1, 1, 2},
		{0, 5, 0, 0},
		{2, 0, 3, 3},
	}
	// Should return 9
	matrixElementsSum(hotel)
}