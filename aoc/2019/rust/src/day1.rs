use aoc_runner_derive::{aoc, aoc_generator};

#[aoc_generator(day1)]
pub fn input_generator(input: &str) -> Vec<isize> {
    let masses: Vec<isize> = input
                                .lines()
                                .map(|n| n.parse().unwrap())
                                .collect();
    masses
}

fn calc_fuel(mass: isize) -> isize {
    mass / 3 - 2
}

fn calc_fuel_for_fuel(total_mass: isize, fuel_mass: isize) -> isize {
    if fuel_mass > 0 {
        return calc_fuel_for_fuel(total_mass + fuel_mass, calc_fuel(fuel_mass))
    } else {
        return total_mass
    }
}

#[aoc(day1, part1)]
pub fn solve_a(input: &Vec<isize>) -> isize {
    let massed: Vec<isize> = input.iter().map(|n| calc_fuel(*n)).collect();
    massed.iter().sum()
}

#[aoc(day1, part2)]
pub fn solve_b(input: &Vec<isize>) -> isize {
    let massed: Vec<isize> = input.iter().map(|n| calc_fuel(*n)).collect();
    let masses_with_fuel: Vec<isize> = massed.iter()
                                        .map(|n| calc_fuel_for_fuel(*n, calc_fuel(*n)))
                                        .collect();
    masses_with_fuel.iter().sum()
}
