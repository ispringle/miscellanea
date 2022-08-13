#[macro_use]
extern crate rocket;

use rand::seq::SliceRandom;
use rocket::State;
use serde::Deserialize;
use std::fs::File;
use std::io::Read;

#[derive(Deserialize, Debug)]
struct Words {
    adjectives: Vec<String>,
    nouns: Vec<String>,
}

#[get("/")]
fn your_face(words: &State<Words>) -> String {
    let adjective = words.adjectives.choose(&mut rand::thread_rng()).unwrap();
    let noun = words.nouns.choose(&mut rand::thread_rng()).unwrap();
    let conjunction = match &adjective.chars().next() {
        Some('a' | 'e' | 'i' | 'o' | 'u') => "an",
        Some(_) => "a",
        &None => "a",
    };

    format!("Your face is {} {} {}!", conjunction, adjective, noun)
}

#[launch]
fn rocket() -> _ {
    let mut file = File::open("data/word-data.json").expect("JSON not formatted properly!");
    let mut data = String::new();
    file.read_to_string(&mut data).unwrap();
    let words: Words = serde_json::from_str(&data).unwrap();
    rocket::build().manage(words).mount("/", routes![your_face])
}
