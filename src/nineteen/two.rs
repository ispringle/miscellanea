use std::fs;

type Puzzle = Vec<isize>;

struct Intcomp {
    intcode: Vec<isize>,
    curr_pos: usize,
    curr_optcode: isize,
}

impl Intcomp {
    fn new(intcode: Vec<isize>) -> Intcomp {
        Intcomp{
            intcode: intcode.clone(),
            curr_pos: 0,
            curr_optcode: intcode[0]
        }
    }

    fn set_input(&mut self, noun: isize, verb: isize) {
        self.intcode[1] = noun;
        self.intcode[2] = verb;
    }

    fn get_loc(&self, loc: usize) -> isize {
        self.intcode[loc]
    }

    fn run(&mut self) {
        loop {
            match self.curr_optcode {
                1 => self._add(),
                2 => self._multiply(),
                99 => return,
                _ => ()
            }
            self.curr_pos += 4;
            self.curr_optcode = self.intcode[self.curr_pos];
        }
    }

    fn _add(&mut self) {
        let loc_x = self.intcode[self.curr_pos + 1] as usize;
        let loc_y = self.intcode[self.curr_pos + 2] as usize;
        let loc_z = self.intcode[self.curr_pos + 3] as usize;
        self.intcode[loc_z] = self.intcode[loc_x] + self.intcode[loc_y];
    }

    fn _multiply(&mut self) {
        let loc_x = self.intcode[self.curr_pos + 1] as usize;
        let loc_y = self.intcode[self.curr_pos + 2] as usize;
        let loc_z = self.intcode[self.curr_pos + 3] as usize;
        self.intcode[loc_z] = self.intcode[loc_x] * self.intcode[loc_y];
    }

}


fn import_data(file_path: String) -> Puzzle {
    fs::read_to_string(file_path).unwrap()
        .trim().split(',')
        .map(|n| n.parse().unwrap())
        .collect()
}

fn solve_a(puzzle: Puzzle) -> isize {
    let mut intcomp: Intcomp = Intcomp::new(puzzle);
    intcomp.set_input(12, 2);
    intcomp.run();
    intcomp.get_loc(0)
}

fn solve_b(puzzle: Puzzle) -> Option<isize> {
    for noun in 0..100 {
        for verb in 0..100 {
            let mut intcomp: Intcomp = Intcomp::new(puzzle.clone());
            intcomp.set_input(noun, verb);
            intcomp.run();
            if intcomp.get_loc(0) == 19690720 {
                return Some(noun * 100 + verb)
            }
        }
    }
    None
}

pub fn solve() {
    let puzzle: Puzzle = import_data("./data/02".to_string());
    println!("Part A answer: {}", solve_a(puzzle.clone()));
    println!("Part B answer: {}", solve_b(puzzle).unwrap());
}
