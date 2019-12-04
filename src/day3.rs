use aoc_runner_derive::{aoc, aoc_generator};
use std::collections::HashSet;

type Path = Vec<(String)>;
type Paths = Vec<Path>;
type Coord = (isize, isize);
type Coords = HashSet<Coord>;

#[derive(Debug)]
struct Circuit {
    coords: Coords,
}

impl Circuit {
    fn new(path: Path) -> Circuit {
        let mut x: isize = 0;
        let mut y: isize = 0;
        let mut coords: Coords = HashSet::new();
        for direction in path {
            let (cardinality, moves) = match direction.chars().next() {
                Some(c) => direction.split_at(c.len_utf8()),
                None => direction.split_at(0),
            };
            let distance: isize = moves.parse().unwrap();
            match cardinality {
                "U" => {
                    let new_coords = move_east((x, y), distance);
                    for coord in new_coords {
                        coords.insert(coord);
                    }
                    y += distance;
                },
                "D" => {
                    let new_coords = move_east((x, y), distance);
                    for coord in new_coords {
                        coords.insert(coord);
                    }
                    y -= distance;
                },
                "L" => {
                    let new_coords = move_east((x, y), distance);
                    for coord in new_coords {
                        coords.insert(coord);
                    }
                    x -= distance;
                },
                "R" => {
                    let new_coords = move_east((x, y), distance);
                    for coord in new_coords {
                        coords.insert(coord);
                    }
                    x += distance;
                },
                _ => ()
            }
        }

        // The following are locally scoped functions needed only for
        // the creation of the initial coordinates. Since this is the
        // `new()` method I am putting these here instead of inside
        // of the Cicruit impl
        fn move_north(start: Coord, distance: isize) -> Coords {
            let x = start.0;
            let y = start.1;
            let coords: Coords = (y..y+distance).map(|ny| (x, ny)).collect();
            coords
        }

        fn move_south(start: Coord, distance: isize) -> Coords {
            let x = start.0;
            let y = start.1;
            let coords: Coords = (y..y-distance).map(|ny| (x, ny)).collect();
            coords
        }

        fn move_west(start: Coord, distance: isize) -> Coords {
            let x = start.0;
            let y = start.1;
            let coords: Coords = (x..x-distance).map(|nx| (nx, y)).collect();
            coords
        }

        fn move_east(start: Coord, distance: isize) -> Coords {
            let x = start.0;
            let y = start.1;
            let coords: Coords = (x..x+distance).map(|nx| (nx, y)).collect();
            coords
        }

        Circuit { coords: coords }
    }

    //fn intersections_with(&self, circuit_b: &Circuit) -> HashSet<(isize, isize)> {
    fn intersections_with(&self, circuit_b: &Circuit) -> Vec<(isize, isize)> {
        let mut intersections = Vec::new();
        for coord in self.coords.intersection(&circuit_b.coords) {
            intersections.push(*coord);
        }
        intersections
    }
}

fn distance(a: (isize, isize), b: (isize, isize)) -> isize {
    (a.0 - b.0).abs() + (a.1 - b.1).abs()
}

#[aoc_generator(day3)]
pub fn input_generator(input: &str) -> Paths {
    input
        .lines()
        .map(|l|
             l.split(',')
             .map(|d| d.to_string())
             .collect())
        .collect()
}

#[aoc(day3, part1)]
pub fn solve_a(input: &Paths) -> isize {
    let path_a: Path = input[0].clone();
    let path_b: Path = input[1].clone();
    let circuit_a: Circuit = Circuit::new(path_a);
    let circuit_b: Circuit = Circuit::new(path_b);
    let intersections = circuit_a.intersections_with(&circuit_b);
    let nearest = intersections.iter()
        .map(|coord| distance((0,0), *coord))
        .collect::<isize>()
        .sort()
        .reverse()[0];
    nearest
}

#[aoc(day3, part2)]
pub fn solve_b(input: &Paths) -> isize {
    1
}
