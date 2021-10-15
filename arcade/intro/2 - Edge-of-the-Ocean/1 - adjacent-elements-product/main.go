package main

import (
	"fmt"
	"math"
)

func adjacentElementsProduct(inputArray []int) int {
    max := inputArray[0] * inputArray[1]
    
    for i := 1; i < len(inputArray)-1; i++ {
        if max < inputArray[i] * inputArray[i+1] {
            max = inputArray[i] * inputArray[i+1]
        }
    }
    
    return max
}

func adjacentElementsProductV2(inputArray []int) int {
	max := math.MinInt32
	for idx := 1; idx < len(inputArray); idx++ {
		product := inputArray[idx-1] * inputArray[idx]
		if product > max {
			max = product
		}
	}
	return max
}

func main() {
	slice := []int{3, 6, -2, -5, 7, 3}
	result := adjacentElementsProduct(slice)
	fmt.Println(result)
	fmt.Println("-----------------------------")
    result2 := adjacentElementsProductV2(slice)
	fmt.Println(result2)
}