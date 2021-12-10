use std::fs::File;
use std::io::Read;

fn neightbors(index: usize, width: usize, mapping: &Vec<u32>) -> Vec<usize> {
    let i: i32 = index as i32;
    let w: i32 = width as i32;
    let l: i32 = mapping.len() as i32 - 1;
    let top: usize = if i - w >= 0 { index - width } else { index };
    let nxt: usize = if (i + 1) % w != 0 { index + 1 } else { index };
    let bot: usize = if i + w <= l { index + width } else { index };
    let pre: usize = if i % w != 0 { index - 1 } else { index };
    vec![top, nxt, bot, pre]
}

fn lowest(mapping: &Vec<u32>, width: usize) -> Vec<usize> {
    let mut low_points: Vec<usize> = Vec::new();
    let length = mapping.len() - 1;
    for i in 0..length {
        let ns: Vec<usize> = neightbors(i, width, &mapping);
        let cmp: Vec<bool> = ns
            .iter()
            .map(|n| &mapping[*n] > &mapping[i] || *n == i)
            .collect();
        let lowest: bool = cmp.iter().all(|x| *x);
        if lowest {
            low_points.push(i);
        }
    }
    low_points
}

fn part_one(mapping: &Vec<u32>, width: usize) -> u32 {
    lowest(mapping, width)
        .iter()
        .fold(0, |acc, i| acc + mapping[*i as usize] + 1)
}

fn count(index: usize, width: usize, mut mapping: &mut Vec<u32>) -> u32 {
    match mapping[index] {
        9 => 0,
        _ => {
            mapping[index] = 9;
            1 + neightbors(index, width, mapping)
                .iter()
                .map(|n| count(*n, width, &mut mapping))
                .sum::<u32>()
        }
    }
}

fn part_two(mut mapping: &mut Vec<u32>, width: usize) -> u32 {
    let mut basins: Vec<u32> = lowest(mapping, width)
        .iter()
        .map(|i| count(*i, width, &mut mapping))
        .collect();
    basins.sort();
    let top: Vec<&u32> = basins.iter().rev().take(3).collect();
    let mut ans: u32 = 1;
    for x in top {
        ans = ans * x;
    }
    ans
}

fn main() {
    let mut file = File::open("input.txt").expect("Bad input file");
    let mut contents = String::new();
    file.read_to_string(&mut contents)
        .expect("Could not read file");
    let width: usize = contents.find('\n').unwrap();
    let mut mapping: Vec<u32> = contents
        .chars()
        .filter_map(|c| match c {
            '\n' => None,
            _ => Some(c.to_digit(10).unwrap()),
        })
        .collect();
    let p1 = part_one(&mapping, width);
    println!("Part One: {}", p1);
    let p2 = part_two(&mut mapping, width);
    println!("Part Two: {}", p2);
}
