use aoc_runner_derive::{aoc, aoc_generator};
use std::collections::HashSet;

type Coord = Vec<(isize, isize)>;
type Coords = (Coord, Coord);

fn coord_generator(direction: &str) -> impl Iterator<Item = (isize, isize)> {
    let (cardinality, distance) = match direction.chars().next() {
        Some(c) => direction.split_at(c.len_utf8()),
        None => direction.split_at(0),
    };
    let distance: usize = distance.parse().unwrap();
    let direction = match cardinality {
        "U" => (0, 1),
        "D" => (0, -1),
        "L" => (1, 0),
        "R" => (-1, 0),
        _ => (0, 0),
    };
    std::iter::repeat(direction).take(distance)
}

fn parse_line(line: &str) -> Coord {
    line.split(',')
        .flat_map(coord_generator)
        .scan((0, 0), |coord, dist| {
            coord.0 += dist.0;
            coord.1 += dist.1;
            Some(coord.clone())
             })
    .collect()
}

fn distance(coord: &(isize, isize)) -> usize {
    coord.0.abs() as usize + coord.1.abs() as usize
}

#[aoc_generator(day3)]
pub fn input_generator(input: &str) -> Coords {
    let mut lines = input.lines();
    (parse_line(lines.next().unwrap()), parse_line(lines.next().unwrap()))
}

#[aoc(day3, part1)]
pub fn solve_a(input: &Coords) -> usize {
    let circuit_a: HashSet<_> = input.0.iter().cloned().collect();
    let circuit_b: HashSet<_> = input.1.iter().cloned().collect();
    let intersections = circuit_a.intersection(&circuit_b);
    let nearest = intersections.map(distance).min();
    nearest.unwrap()
}

#[aoc(day3, part2)]
pub fn solve_b(input: &Coords) -> usize {
    let circuit_a: HashSet<_> = input.0.iter().cloned().collect();
    let circuit_b: HashSet<_> = input.1.iter().cloned().collect();
    let intersections = circuit_a.intersection(&circuit_b);
    let (circuit_a, circuit_b) = input;
    let quickest = intersections
                    .map(|coord|
                         circuit_a.iter().position(|x| x == coord).unwrap() +
                         circuit_b.iter().position(|x| x == coord).unwrap() + 2)
                    .min()
                    .unwrap();
    quickest
}

