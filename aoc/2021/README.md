# Advent of Code 2021
## The Polyglot of Code

| Day | Lang            | Stars |
|-----|-----------------|-------|
| 1   |[Racket][0]      | ⭐ ⭐ |
| 2   |[Retro][1]       | ⭐ ⭐ |
| 3   |[J][2]           | ⭐ ⭐ |
| 4   |[Python][7] (TBD)| ⭐ ⭐ |
| 5   |[Python][7] (TBD)| ⭐ ⭐ |
| 6   |[Crystal][5]     | ⭐ ⭐ |
| 7   |[R][6]           | ⭐ ⭐ |
| 8   |[Python][7]      | ⭐ ⭐ |
| 9   |[Rust][8]        | ⭐ ⭐ |
| 10  |[Go][9]          | ⭐ ⭐ |
| 11  |[JavaScript][10] | ⭐ ⭐ |
| 12  |[Nim][11]        | ⭐ ⭐ |
| 13  |[Python][7] (TBD)| ⭐ ⭐ |
| 14  |[Python][7] (TBD)| ⭐ ⭐ |
| 15  |[C][14]          | ⭐ ⭐ |
| 16  |                 |       |
| 17  |                 |       |

### Day 1

Once I got into being Lispy, this was a breeze! Took me a while to write a
`zip` though, was thinking too hard. Part two seemed much easier, but part two
was just part one... I thought about writing some functions to make my code a
bit cleaner and reuse stuff, but I sort of like the aesthetic of a
deeeeeeeeeeeeeply nested lisp algo, so I just yanked.

### Day 2

This was hard, but fun. Hard because Forth lang. Fun because stack-ang :p! I
reached for Retro for two reasons originally, one because it has a lot of
built-ins that were easily accessible (like `file:for-each-line` and
quotations) and second becasue of the `reorder` word -- which I ended up not
using because I eventually got the answer with shuffling. Something else that's
cool about Retro is it has a built-in literate programming tool that lets you
write markdown and it will extract the code from it.

### Day 3

Never again. Bad docs + unreadable code does not an enjoyable experience make.

### Day 4

Python, just getting it done. I'll revisit this with a different language. Hard
to find time on the weekend.

### Day 5

Python, just getting it done. I'll revisit this with a different language. Hard
to find time on the weekend.

### Day 6

Crystal isn't so bad. I spent most of my time thinkin about the challenge.
Whenever AOC has a challenge with a obscenely large number of iterations you
know there is a simple solution, just gotta look past the obvious and naive
one. In this case, we just keep track of the total number of fish at each age.
Every day we rotate the 0th fish to the end, since that's how many new fish
they'll make. Then we add the last element (newly minted fish) to the 6th
element, original fish with reset timers.

### Day 7

I do not like R. It is deceptive. You think it's Python and then it isn't. Indices start at 1, functions take a wide variety of varying input types. Running a file/script is not easy and the output is dumb. I can't figure out the dataframe notation and I am not sure what a dataframe v. list v. w/e `c()` produces is. Anywho... R's shortcomings did mean the solution was fairly small. Since R is a mathemtical language it operates on vectors and vector-like objects very easily. Throw a function a vector and it just does the thing on every element in the vector. This made today's solution iterator-free, which is cool...

### Day 8

I think I'm giving up on the polyglot thing. Over the weekend I decided to just
use Python to bang out a quick solution and frankly it was more fun than using
J the day before. I'll probably still use _some_ other langs, figuring out the
language each day is taking more time than the problem set. Like, I don't mean
learning the language or reading docs. I mean the languishing over the language
_to_ use takes more time than the entire solution have the time. Plus, I want
to use things like Vlang, Rust, Go, JavaScript, and some previously used
languages, and I don't want to worry about pulling in a language too soon. So
for the rest of this challenge I am going to do two things 1) not worry about
  what I use to solve the problem and 2) try to avoid just taking the easy
  route and writing Python. I used Python today, but I was bored of the terse
  and unreadable stuff, so I wrote some OOPython.


[0]: https://racket-lang.org/
[1]: http://retroforth.org/
[2]: https://www.jsoftware.com/#/
[5]: https://crystal-lang.org/
[6]: https://www.r-project.org/
[7]: https://www.python.org/
[8]: https://www.rust-lang.org/
[9]: https://go.dev/
[10]: https://www.javascript.com/
[11]: https://nim-lang.org/
[12]: 
[13]: 
[14]: http://www.open-std.org/jtc1/sc22/wg14/
