use aoc_runner_derive::{aoc, aoc_generator};
use crate::utils::intcomp::Puzzle;
use crate::utils::intcomp::Intcomp;

#[aoc_generator(day2)]
pub fn input_generator(input: &str) -> Puzzle {
        input
            .trim().split(',')
            .map(|n| n.parse().unwrap())
            .collect()
}

#[aoc(day2, part1)]
pub fn solve_a(input: &Puzzle) -> isize {
    let mut intcomp: Intcomp = Intcomp::new(input.to_vec(), None);
    intcomp.set_input(12, 2);
    intcomp.run();
    intcomp.get_loc(0)
}

#[aoc(day2, part2)]
pub fn solve_b(input: &Puzzle) -> Option<isize> {
    for noun in 0..100 {
        for verb in 0..100 {
            let mut intcomp: Intcomp = Intcomp::new(input.clone(), None);
            intcomp.set_input(noun, verb);
            intcomp.run();
            if intcomp.get_loc(0) == 19690720 {
                return Some(noun * 100 + verb)
            }
        }
    }
    None
}
