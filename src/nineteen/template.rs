use std::fs::File;
use std::io::BufReader;
use std::io::prelude::*;

fn import_data(file_path: String) -> Vec<isize> {
    let file = File::open(file_path).unwrap();
    let reader = BufReader::new(file);
    let puzzle: Vec<isize> = reader
                                .split(',')
                                .map(|n| n.unwrap().parse().unwrap())
                                .collect();
    puzzle
}

fn solve_a() {
}

fn solve_b() {
}

pub fn solve() {
    let puzzle = import_data("./data/01".to_string());
    println!("Part A answer: {}", solve_a(puzzle.clone()));
    println!("Part B answer: {}", solve_b(puzzle));
}
