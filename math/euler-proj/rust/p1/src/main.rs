fn main() {
    let mut multiples: Vec<i32> = Vec::new();
    for n in 3..1000 {
        if n % 3 == 0 {
            multiples.push(n);
        }
        else if n % 5 == 0 {
            multiples.push(n);
        }
    }
    let sum: i32 = multiples.iter().sum();
    println!("{}", sum);
}
