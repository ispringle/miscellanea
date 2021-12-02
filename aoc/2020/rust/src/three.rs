pub fn solve(input: String) {
    let answer_one = part_one(input.clone());
    println!("Part one: {}", answer_one);
    let answer_two = part_two(input.clone());
    println!("Part one: {}", answer_two);
}

fn part_one(input: String) -> usize {
    let rise: usize = 1;
    let run: usize = 3;
    count_trees(run, rise, &input)

}

fn part_two(input: String) -> usize {
    [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
        .iter()
        .map(|(x, y)| count_trees(*x, *y, &input))
        .product()
}

fn count_trees(x: usize, y: usize, map: &str) -> usize {
    map.lines()
        .step_by(y)
        .enumerate()
        .filter(|(step, line)| line.as_bytes()[(*step * x) % line.len()] == b'#')
        .count()
}
