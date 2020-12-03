use regex::Regex;

lazy_static! {
    static ref PATTERN: Regex = Regex::new(r"(\d+)-(\d+) (\w): (\w*)").unwrap();
}

pub fn solve(input: String) {
    let input = parse(input);
    let answer_one = part_one(input.clone());
    println!("Part one: {}", answer_one);
    // let answer_two = part_two(input.clone());
    // println!("Part one: {}", answer_two);
}

fn parse(input: String) -> Vec<Option<(usize, usize, char, String)>> {
    input.lines().map(|l| parser(l)).collect()
}

fn parser(line: &str) -> Option<(usize, usize, char, String)> {
    let result = PATTERN.captures(line)?;
    Some((
            result.get(1)?.as_str().parse().ok()?,
            result.get(2)?.as_str().parse().ok()?,
            result.get(3)?.as_str().chars().next()?,
            result.get(4)?.as_str().to_string(),
    ))

}

fn part_one(input: Vec<Option<(usize, usize, char, String)>>) -> usize {
    input.iter()
        .filter(|i| {
            let (m, x, ch, p) = i.as_ref().unwrap();
            (m..=x).contains(&&(*p).chars().filter(|c| c == ch).count())
        })
        .count()
}

fn part_two(input: Vec<Option<(usize, usize, char, String)>>) -> usize {
    todo!()
}
