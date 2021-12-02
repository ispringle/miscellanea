# aoc
Advent of Code

## Install

1. `pip install -r requirements.txt`
1. `export AOC_SESSION="my_AOC_session"` or create a file named
"SECRET" with the session id inside of it. Then run
`source set_auth`

## Usage

To init a new day run `./new year day`. This will create a new dir named year/day
and copy the `*.py` files from template into this dir.

Answer go into year/day/Solution.py. The function `solve` should return a tuple with either
solution `a` or solutions `a` and `b`.

To solve, run `main.py` followed by the year and day. The solution will be printed to stdout
and also sent to aoc for submission.
