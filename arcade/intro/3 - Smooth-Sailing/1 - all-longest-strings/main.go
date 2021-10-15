package main

func allLongestStrings(inputArray []string) []string {
	maxLength := 0
	var longestStrings []string

	for _, str := range inputArray {
		if len(str) > maxLength {
			maxLength = len(str)
			longestStrings = []string{}
		}
		if len(str) == maxLength {
			longestStrings = append(longestStrings, str)
		}
	}

	return longestStrings
}

func main() {
	words := []string{"aba", "aa", "ad", "vcd", "aba"}
	allLongestStrings(words)
}