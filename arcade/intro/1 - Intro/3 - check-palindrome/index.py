def checkPalindrome(inputString):
    erg = inputString[::-1]
    palindrome = False 
    if inputString == erg:
        palindrome = True 
        return bool(palindrome)
    else:
        palindrome = False 
        return bool(palindrome)