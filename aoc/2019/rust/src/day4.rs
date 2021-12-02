use aoc_runner_derive::{aoc, aoc_generator};

fn incremental(number: &isize) -> bool {
    let mut last: u32 = 0;
    let digits: Vec<u32> = number
                                .to_string()
                                .chars()
                                .map(|c|c.to_digit(10).unwrap())
                                .collect();
    for digit in digits {
        if digit >= last {
            last = digit;
        } else {
            return false
        }
    }
    true
}
fn all_incremental(range: std::ops::Range<isize>) -> Vec<isize> {
    range.into_iter().filter(incremental).collect()
}

fn same_neighbor(number: &isize) -> bool {
    let digits: Vec<u32> = number
                                .to_string()
                                .chars()
                                .map(|c|c.to_digit(10).unwrap())
                                .collect();
    let mut iter_digits = digits.iter();
    let mut last: u32 = *iter_digits.next().unwrap();
    for digit in iter_digits {
        if *digit == last {
            return true
        } else {
            last = *digit;
        }
    }
    false
}

fn same_small_neighbor(number: &isize) -> bool {
    let digits: Vec<u32> = number
                                .to_string()
                                .chars()
                                .map(|c|c.to_digit(10).unwrap())
                                .collect();
    for digit in 0..digits.len()-1 {
        if digits[digit] == digits[digit + 1] &&
            !(digit > 0 && digits[digit-1] == digits[digit] 
              || digit < 4 && digits[digit+2] == digits[digit]) {
                return true
            }
    }
    false
}

#[aoc_generator(day4)]
pub fn input_generator(input: &str) -> std::ops::Range<isize> {
    let range: Vec<isize> = input.split('-').map(|x| x.parse().unwrap()).collect();
    (range[0]..range[1])
}

#[aoc(day4, part1)]
pub fn solve_a(input: &std::ops::Range<isize>) -> usize {
    let mut valids = all_incremental(input.clone());
    valids = valids.into_iter().filter(same_neighbor).collect();
    valids.len()
}

#[aoc(day4, part2)]
pub fn solve_b(input: &std::ops::Range<isize>) -> usize {
    let mut valids = all_incremental(input.clone());
    valids = valids.into_iter().filter(same_small_neighbor).collect();
    valids.len()
}

