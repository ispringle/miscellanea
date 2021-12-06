# Advent of Code 2021
## The Polyglot of Code

| Day | Lang            | Stars |
|-----|-----------------|-------|
| 1   |[Racket][0]      | ⭐ ⭐ |
| 2   |[Retro][1]       | ⭐ ⭐ |
| 3   |[J][2]           | ⭐ ⭐ |
| 4   |[Python][3] (TBD)| ⭐ ⭐ |
| 5   |[Python][3] (TBD)| ⭐ ⭐ |
| 6   |[Crystal][5]     | ⭐ ⭐ |

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

[0]: https://racket-lang.org/
[1]: http://retroforth.org/
[2]: https://www.jsoftware.com/#/
[3]: https://www.python.org/
[4]: https://crystal-lang.org/
