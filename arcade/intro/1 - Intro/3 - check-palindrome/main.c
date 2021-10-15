bool checkPalindrome(char * s) {
    char *q = s + strlen(s) - 1;

    while (q > s) {
        if (*q-- != *s++)
            return false;
    }
    return true;
}
