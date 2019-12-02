use std::fs::File;
use std::io::BufReader;
use std::io::prelude::*;

fn import_data(file_path: String) -> Vec<isize> {
    let file = File::open(file_path).unwrap();
    let reader = BufReader::new(file);
    let masses: Vec<isize> = reader
                                .lines()
                                .map(|n| n.unwrap().parse().unwrap())
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

fn solve_a(massed: Vec<isize>) -> isize {
    massed.iter().sum()
}

fn solve_b(massed: Vec<isize>) -> isize {
    let masses_with_fuel: Vec<isize> = massed.iter()
                                        .map(|n| calc_fuel_for_fuel(*n, calc_fuel(*n)))
                                        .collect();
    masses_with_fuel.iter().sum()
}

pub fn solve() {
    let masses = import_data("./data/01".to_string());
    let massed: Vec<isize> = masses.iter().map(|n| calc_fuel(*n)).collect();
    println!("Part A answer: {}", solve_a(massed.clone()));
    println!("Part B answer: {}", solve_b(massed));
}
