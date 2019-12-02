pub type Puzzle = Vec<isize>;

pub struct Intcomp {
    intcode: Vec<isize>,
    curr_pos: usize,
    curr_optcode: isize,
}

impl Intcomp {
    pub fn new(intcode: Vec<isize>) -> Intcomp {
        Intcomp{
            intcode: intcode.clone(),
            curr_pos: 0,
            curr_optcode: intcode[0]
        }
    }

    pub fn set_input(&mut self, noun: isize, verb: isize) {
        self.intcode[1] = noun;
        self.intcode[2] = verb;
    }

    pub fn get_loc(&self, loc: usize) -> isize {
        self.intcode[loc]
    }

    pub fn run(&mut self) {
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
