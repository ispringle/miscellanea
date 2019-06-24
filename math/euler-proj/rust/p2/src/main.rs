fn fib(max: isize ) -> Vec<isize>  {
    let mut seq: Vec<isize> = Vec::new();
    let mut prev: isize = 1;
    let mut curr: isize = 2;
    let mut next: isize;
    
    seq.push(prev);
    seq.push(curr);

    while curr < max {
        next = curr + prev;
        prev = curr;
        curr = next;
        seq.push(next);
    }

    seq
}

fn get_evens(seq: Vec<isize>) -> Vec<isize> {
    let mut evens: Vec<isize> = Vec::new();
    for n in seq {
        if n % 2 == 0 {
            evens.push(n)
        }
    }
    evens
}

fn main() {
    let seq: Vec<isize> = fib(4_000_000);
    let evens: Vec<isize> = get_evens(seq);
    let summed: isize = evens.iter().sum();
    println!("{}", summed);
}

