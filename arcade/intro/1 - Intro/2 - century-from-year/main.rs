fn century_from_year(year: i32) -> i32 {
    if year % 100 == 0 {
        return year / 100;
    }
    (year / 100) + 1
}

fn main() {
    println!("2004 is in the {}st century", century_from_year(2004));
}