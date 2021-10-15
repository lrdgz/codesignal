export function checkPalindrome(inputString: string): boolean {
    for (let i = 0, j = inputString.length - 1; i <= j; i++, j--) {
      if (inputString[i] !== inputString[j]) return false;
    }
    return true;
}
  
export function checkPalindromeV2(inputString: string): boolean {
    return inputString == inputString.split('').reverse().join('');
}

export function checkPalindromeV3(inputString: string): boolean {
  let re = /[\W_]/g;
  let lowRegStr = inputString.toLowerCase().replace(re, '');
  let reverseStr = lowRegStr.split('').reverse().join(''); 
  return reverseStr === lowRegStr;
}
