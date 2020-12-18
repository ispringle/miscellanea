extern crate num_bigint;
extern crate num_traits;

use std::{process,env};
use std::time;

use num_bigint::BigUint;
use num_traits::{Zero, One};

fn main() {
    let args: Vec<String> = env::args().collect();
    match args.len() {
        1 => {
            println!("No arguments provided. What position in the fibonacci sequence?");
        },
        2 => {
            match args[1].parse() {
                Ok(num) => run_fibs(num),
                Err(_) => {
                    eprintln!("Error: Argument is not an integer!");
                    process::exit(1);
            }
            };
        },
        _ => {
            println!("This program only accepets a single argument");
            process::exit(1);
        }
    };
}

fn run_fibs(n: usize) {
    //Time pard's fib
    let start = time::Instant::now();
    let ans = fib(n);
    let elapsed = start.elapsed();
    let ms = ((elapsed.as_secs() as f64) + (elapsed.subsec_nanos() as f64 / 1_000_000_000.0)) * 1000.0;
    //println!("Pard's fib:\nAnswer: {}\nTime: {}ms\n", ans, ms);
    println!("{}", ans);

}

//Pard's memo fib
fn fib(n: usize) -> BigUint {
    fn fibm(n: usize, prev: BigUint, curr: BigUint) -> BigUint {
        if n <= 0 {
            prev
        } else {
            fibm(n - 1, &prev + curr, prev)
        }
    }

    match n {
        0 => Zero::zero(),
        1 => One::one(),
        _ => fibm(n, Zero::zero(), One::one())
    }
}

//Pard's folding fib
fn fold_fib(n: u128) -> u128 {
    *(2..n).fold(
        vec![1u128, 1], |mut data, _| {
            data.push(data[data.len() - 2] + data[data.len() - 1]);
            data
    })
    .last()
    .unwrap()
}
