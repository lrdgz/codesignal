fn check_palindrom(input_string: String) -> bool {
    // return input_string.chars().rev().collect::<String>() == input_string;
    let input_chars: Vec<char> = input_string.chars().collect();
    let length = input_string.len();
    // println!("length is:{}", length);
    for i in 0..length/2 {
        // println!("Inside if {} - {}", input_chars[i], input_chars[length-i-1]);
        if input_chars[i] != input_chars[length-i-1] {
            return false;
        }
    }
    return true;
}

fn main() {
    // println!("Inside main program");
    println!("{}", check_palindrom(String::from("aabcbaa")));
}
