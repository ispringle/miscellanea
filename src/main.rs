use std::fs::File;
use std::io::prelude::*;

mod one;

fn main() {
    let input_file = std::env::args().nth(1).expect("No input file given");
    let mut file = File::open(input_file.clone()).expect("Bad input file");
    let mut contents = String::new();
    file.read_to_string(&mut contents).expect("Could not read file");

    let day: &str = input_file.split("/").last().unwrap();
    match day {
        "1" => one::solve(contents),
        _ => {println!("Solution for day {} does not exist.", day)},
    }
}
