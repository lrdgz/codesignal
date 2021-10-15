bool checkPalindrome(std::string inputString) {
int i;
      int length = inputString.length();

      for (i = 0; i < length; ++i)
            if (inputString.at(i) != inputString.at(length - i - 1)) return false;

      return true;
}