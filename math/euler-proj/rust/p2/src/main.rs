fn fib_seq_under(max: usize) -> Vec<usize> {
    let mut seq = vec![0,1];
    while seq.last() < Some(&max) {
        let length = seq.len();
        let prev = seq.get(length - 2).unwrap();
        let curr = seq.get(length - 1).unwrap();
        seq.push(prev + curr);
    }
    let length = seq.len();
    seq[0..length - 1].to_vec()
}

fn main() {
    let limit = 4_000_000usize;
    let seq = fib_seq_under(limit);
    let sum = seq.iter()
        .filter(|&n| n % 2 == 0)
        .fold(0, |a, b| a + b);
    println!("{:#?}", sum);
}

