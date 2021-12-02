use aoc_runner_derive::{aoc, aoc_generator};
use crate::utils::intcomp::Puzzle;
use crate::utils::intcomp::Intcomp;

#[aoc_generator(day5)]
pub fn input_generator(input: &str) -> Puzzle {
        input
            .trim().split(',')
            .map(|n| n.parse().unwrap())
            .collect()
}

#[aoc(day5, part1)]
pub fn solve_a(input: &Puzzle) -> isize {
    println!("{:#?}", input);
    let mut intcomp: Intcomp = Intcomp::new(input.to_vec(), 1);
    intcomp.set_input(12, 2);
    intcomp.run();
    intcomp.get_output()
}

#[aoc(day5, part2)]
pub fn solve_b(input: &Puzzle) -> Option<isize> {
    Some(1)
}
