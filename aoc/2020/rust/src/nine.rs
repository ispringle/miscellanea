use itertools::Itertools;

pub fn solve(input: String) {
    let data = parse(input);
    let answer_one = part_one(&data);
    println!("Part one: {}", answer_one);
    let answer_two = part_two(data, answer_one);
    println!("Part two: {}", answer_two);
}

fn parse(input: String) -> Vec<usize> {
    input.lines()
        .map(|l| l.parse().unwrap())
        .collect()
}

fn part_one(data: &Vec<usize>) -> usize {
    data.windows(26).find(
        |w| w[0..25].iter()
            .permutations(2)
            .all(|x| x[0] + x[1] != w[25])
        )
        .map(|x| x[25])
        .unwrap()
}

fn part_two(data: Vec<usize>, target: usize) -> usize {
    let aos: Vec<usize> = data.iter().scan(0, |acc, &x| {
        *acc = *acc + x;
        Some(*acc)
    }).collect();
    let mut lo = 0;
    let mut hi = 1;
    while aos[hi] - aos[lo] != target {
        if aos[hi] - aos[lo] < target {
            hi += 1;
            if hi >= aos.len() {
                panic!("upper bound exceeds array size");
            }
        } else {
            lo += 1;
        }
    }
    data[lo..hi].iter().min().unwrap() + data[lo..hi].iter().max().unwrap()
}
