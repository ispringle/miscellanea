use std::fs;
use crate::utils::intcomp::Intcomp;
use crate::utils::intcomp::Puzzle;

fn import_data(file_path: String) -> Puzzle {
    fs::read_to_string(file_path).unwrap()
        .trim().split(',')
        .map(|n| n.parse().unwrap())
        .collect()
}

fn solve_a(puzzle: Puzzle) -> isize {
    let mut intcomp: Intcomp = Intcomp::new(puzzle);
    intcomp.set_input(12, 2);
    intcomp.run();
    intcomp.get_loc(0)
}

fn solve_b(puzzle: Puzzle) -> Option<isize> {
    for noun in 0..100 {
        for verb in 0..100 {
            let mut intcomp: Intcomp = Intcomp::new(puzzle.clone());
            intcomp.set_input(noun, verb);
            intcomp.run();
            if intcomp.get_loc(0) == 19690720 {
                return Some(noun * 100 + verb)
            }
        }
    }
    None
}

pub fn solve() {
    let puzzle: Puzzle = import_data("./data/02".to_string());
    println!("Part A answer: {}", solve_a(puzzle.clone()));
    println!("Part B answer: {}", solve_b(puzzle).unwrap());
}
