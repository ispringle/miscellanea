# wordler

A Wordle solver

## Usage

`python wordler "known letters" "known positions"`

The *known letters* are just any (yellow and green) letters that you know exist
in the solution. It can be quoted but as long as it's aone string it doesn't
need to be quoted. Additionally, if a letter has a known position it _can_ be
ommitted here, but it doesn't need to be.

The letters with a *known position* are the the green letters. This is also a
string, the letters go where they ought to and the blanks can be any non-letter
character you wish. For example, assuming we know that 'h' is the second
character in the word, either of the following are valid inputs:
- `-h---`
- `" h   "`

You may even ommit the trailing unknowns thusly:

- `-h`
- `" h"`

As you notice, if you use a space than you must _quote_ it.
