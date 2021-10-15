export function sortByHeight(a: number[]): number[] {
  const filtered = a.filter((val) => val !== -1);
  const sorted = filtered.sort((x, y) => x - y);
  return a.map((val) => (val === -1 ? -1 : sorted.shift())) as number[];
}

export function sortByHeightV2(a: number[]): number[] {
  const s = a.filter((h) => h > 0).sort((x, y) => x - y);
  return a.map((p) => {
    if (p !== -1) {
      return s.shift();
    }
    return -1;
  }) as number[];
}
  
export function sortByHeightV3(a: number[]): number[] {
  const trees: number[] = [];
  let values: number[] = [];
  a.forEach((curr, i) => (curr === -1 ? trees.push(i) : values.push(curr)));
  values = values.sort((x, y) => x - y);
  trees.forEach((val) => values.splice(val, 0, -1));
  return values;
}

function sortByHeightV4(a: number[]): number[] {
  let b = a.slice();
  let pos = [];
  let i = -1;
  
  while ((i = a.indexOf(-1, i+1)) > -1) {
    pos.push(i);
  }

  let rpos = pos.slice();
  while(rpos.length){
    b.splice(rpos.pop(), 1);
  } 
  
  b.sort((a,b)=>a-b);
  while(pos.length) {
    b.splice(pos.shift(), 0, -1);
  }

  return b;
}
