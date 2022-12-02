use std::{fs, ops::Index};

fn main() {
    day1()
}

fn read_input_lines(inputFile: &str) -> std::str::Split<char> {
    let contents = fs::read_to_string("input1.txt")
        .expect("Should have been able to read the file");
    return contents.split('\n')
}

fn day1() {
    let mut calories = Vec::new();
    let mut curr_calories: u32 = 0;

    for line in read_input_lines("input1.txt") {
        if line.is_empty() {
            calories.push(curr_calories);
            curr_calories = 0;
            continue;
        }

        let calorie = line.parse::<u32>()
            .expect(line);
        curr_calories += calorie;
    }

    calories.sort();
    let first = calories.pop().unwrap();
    let second = calories.pop().unwrap();
    let third = calories.pop().unwrap();
    let total = first + second + third;
    println!("max is {total}")
}

fn day2() {

}