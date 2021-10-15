export function commonCharacterCount(s1: string, s2: string): number {
    const str1 = [...s1];
    const str2 = [...s2];
    return str1.reduce((acc, char) => {
      const i = str2.findIndex((c) => char === c);
      if (i >= 0) {
        acc++;
        delete str2[i];
      }
      return acc;
    }, 0);
  }
  
export function commonCharacterCountV2(s1: string, s2: string): number {
    for (let i = 0; i < s1.length; i++) {
      s2 = s2.replace(s1[i], '!');
    }
    return s2.replace(/[^!]/g, '').length;
}

export function commonCharacterCountV3(s1, s2) {
    let count = 0;
    s1 = s1.split('');
    s2 = s2.split('');
    
    s1.forEach(e => {
      if (s2.includes(e)) {
        count++;
        s2.splice(s2.indexOf(e), 1);
      }
    });
    
    return count;
}
