use itertools::Itertools;


pub fn solve(input: String) {
    let answer_one = part_one(input.clone());
    println!("Part one: {}", answer_one);
}

fn part_one(input: String) -> usize {
    input.split("\n\n")
        .map(|x|
            x.replace("\n", "")
                .chars()
                .unique().collect::<String>()
                .len())
        .sum()
}

fn part_two(input: String) -> usize {
    todo!()
}
