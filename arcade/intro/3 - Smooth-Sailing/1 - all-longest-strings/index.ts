export function allLongestStrings(inputArray: string[]): string[] {
    let longest: string[] = [];
    let maxLen = 0;
    for (let i = 0; i < inputArray.length; i++) {
      const currLen = inputArray[i].length;
      if (maxLen < currLen) {
        longest = [inputArray[i]];
        maxLen = currLen;
      } else if (maxLen === currLen) {
        longest.push(inputArray[i]);
      }
    }
    return longest;
}
  
export function allLongestStringsV2(inputArray: string[]): string[] {
    const maxSize = Math.max(...inputArray.map((x) => x.length));
    return inputArray.filter((x) => x.length === maxSize);
}

export function allLongestStringsV3(inputArray: string[]): string[] {
    return inputArray.reduce((r, s, i) => {
        if (!i || r[0].length < s.length) {
            return [s];
        }
        if (r[0].length === s.length) {
            r.push(s);
        }
        return r;
    }, []);
}