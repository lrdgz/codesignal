func checkPalindrome(inputString string) bool {
    if len(inputString) == 1 {
		return true
	}
	if len(inputString)%2 == 0 {
		cut := len(inputString) / 2
		f := inputString[:cut]
		s := inputString[cut:]
		sr := Reverse(s)
		fmt.Println(cut, f, s, sr)
		if f == sr {
			return true
		}
	} else {
		cut := len(inputString) / 2
		f := inputString[:cut]
		s := inputString[cut+1:]
		sr := Reverse(s)
		fmt.Println(cut, f, s, sr)
		if f == sr {
			return true
		}
	}
	return false
}

func Reverse(s string) string {
	runes := []rune(s)
	for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
		runes[i], runes[j] = runes[j], runes[i]
	}
	return string(runes)
}