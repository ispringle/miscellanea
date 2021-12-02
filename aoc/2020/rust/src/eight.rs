type Num = i32;

#[derive(Clone, Copy, Debug)]
enum Op {
    Acc(Num),
    Jmp(Num),
    Nop(Num),
}

pub fn solve(input: String) {
    let program = parse(input);
    let answer_one = part_one(program.clone());
    println!("Part one: {}", answer_one);
    let answer_two = part_two(program);
    println!("Part two: {}", answer_two);
}

fn parse(input: String) -> Vec<Op> {
    input.lines()
        .map(|l| {
            let x: Vec<&str> = l.split(" ").collect();
            match x[0] {
                "acc" => Op::Acc(x[1].parse::<i32>().unwrap()),
                "jmp" => Op::Jmp(x[1].parse::<i32>().unwrap()),
                "nop" => Op::Nop(x[1].parse::<i32>().unwrap()),
                _ => unreachable!(),
            }
        })
        .collect()
}

fn part_one(program: Vec<Op>) -> i32 {
    run(program).0
}

fn part_two(program: Vec<Op>) -> i32 {
    let mut result: (i32, bool) = (0, false);
    for i in (0..program.len()).rev() {
        let mut new_program = program.clone();
        match new_program[i] {
            Op::Acc(_) => (),
            Op::Jmp(x) => new_program[i] = Op::Nop(x),
            Op::Nop(x) => new_program[i] = Op::Jmp(x),
        }
        result = run(new_program);
        match result.1 {
            true => break,
            false => continue,
        }
    }
    result.0
}

fn run(program: Vec<Op>) -> (i32, bool) {
    let mut accumulator: i32 = 0;
    let mut index: usize = 0;
    let mut visited = vec!(false; program.len());
    loop {
        if index == program.len() {
            return (accumulator, true)
        } else if visited[index] {
            return (accumulator, false);
        } else {
            visited[index] = true;
        }
        match program[index] {
            Op::Acc(x) => accumulator += x,
            Op::Jmp(x) => index = (index as Num + x) as usize - 1,
            Op::Nop(_) => (),
        }
        index += 1;
    }
}
