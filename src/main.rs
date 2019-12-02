extern crate clap;
use clap::{App, Arg};

mod nineteen;
mod utils;

fn main() {
    let matches = App::new("Advent of Code")
        .author("Ian S. Pringle <ian@dapringles.com>")
        .about("Advent of Code Solutions")
        .arg(
            Arg::with_name("year")
                .help("Year of AOC to solve")
                .required(true)
                .index(1),
        )
        .arg(
            Arg::with_name("day")
                .help("Day of AOC to solve")
                .required(true)
                .index(2),
        )
        .get_matches();

    let year: isize = matches
        .value_of("year")
        .unwrap()
        .parse()
        .expect("Expected an integer!");

    let day: isize = matches
        .value_of("day")
        .unwrap()
        .parse()
        .expect("Expected an integer!");

    match year {
        2019 => match day {
            1 => nineteen::one::solve(),
            2 => nineteen::two::solve(),
            _ => println!("Not _currently_ a valid day!")
        },
        _ => println!("Not _currently_ a valid year!")
    }
}
