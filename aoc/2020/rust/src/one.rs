use itertools::Itertools;

pub fn solve(input: String) {
    let input: Vec<u32> = parse(input);
    let answer_one = part_one(input.clone());
    println!("Part one: {}", answer_one);
    let answer_two = part_two(input.clone());
    println!("Part one: {}", answer_two);
}

fn parse(input: String) -> Vec<u32> {
    input.lines().map(|n| n.parse::<u32>().unwrap()).collect()
}

fn part_one(input: Vec<u32>) -> u32 {
    *input.iter().permutations(2)
        .map(|v| {if v[0] + v[1] == 2020 { v[0] * v[1] } else { 0 }})
        .filter(|n| *n != 0)
        .collect::<Vec<u32>>()
        .first()
        .unwrap()
}

fn part_two(input: Vec<u32>) -> u32 {
    *input.iter().permutations(3)
        .map(|v| {if v[0] + v[1] + v[2] == 2020 { v[0] * v[1] * v[2] } else { 0 }})
        .filter(|n| *n != 0)
        .collect::<Vec<u32>>()
        .first()
        .unwrap()
}
