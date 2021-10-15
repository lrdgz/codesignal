func centuryFromYear(year int) int {
    yearStr := strconv.Itoa(year)
	for len(yearStr) < 4 {
		yearStr = "0" + yearStr
	}
	fmt.Println(yearStr[:2], yearStr[2:])
	f, _ := strconv.Atoi(yearStr[:2])
	s, _ := strconv.Atoi(yearStr[2:])
	if s > 0 {
		return f + 1
	}
	return f
}
