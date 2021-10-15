package main

import "fmt"

func shapeArea(n int) int {
	return n*n + ((n - 1) * (n - 1))
}

func main() {
	fmt.Println(shapeArea(1))
	fmt.Println(shapeArea(2))
	fmt.Println(shapeArea(3))
	fmt.Println(shapeArea(4))
}