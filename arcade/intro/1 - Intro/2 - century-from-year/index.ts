export function centuryFromYear(year: number): number {
    return Math.ceil(year / 100);
}


export function centuryFromYearV2(year: number): number{
    let module = (year % 100 === 0) ? 0 : 1;
    let centuries = Math.floor(year / 100); 
    return module + centuries;
}

console.log(centuryFromYear(1700))
console.log(centuryFromYearV2(1700))