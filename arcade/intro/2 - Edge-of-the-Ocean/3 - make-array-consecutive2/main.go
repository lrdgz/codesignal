package main

import (
	"math"
)

func makeArrayConsecutive2(statues []int) int {
	max, min := math.MinInt32, math.MaxInt32
	for _, statue := range statues {
		if statue > max {
			max = statue
		}
		if statue < min {
			min = statue
		}
	}
	return max - min + 1 - len(statues)
}