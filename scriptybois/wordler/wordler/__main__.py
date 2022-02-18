import sys


def update_known_letters(new_ks, known_letters={}, guessed=""):
    for c in new_ks.lower():
        if guessed:
            t = known_letters.get(c, [0, []])
            positions = [pos for pos, char in enumerate(guessed) if char == c]
            for pos in positions:
                t[1].append(pos)
            known_letters[c] = t
        if c.isalpha() and new_ks.count(c) >= known_letters.get(c, [0, []])[0]:
            t = known_letters.get(c, [0, []])
            t[0] = new_ks.count(c)
            known_letters[c] = t
    return known_letters


def update_known_positions(position_string, known_positions={}):
    for n, c in {n: c for n, c in enumerate(position_string)}.items():
        if c.isalpha():
            known_positions[n] = c.lower()
    return known_positions


def rank(possible, unguessed):
    return sorted(possible, key=lambda w: sum(
        1 if x in unguessed else 0 for x in w))


def repl(possible):
    unguessed = "abcdefghijklmnopqrstuvwxyz"
    known_letters, known_positions, guess_number, guess = {}, {}, 0, "adieu"
    while guess_number < 6:
        accepted = False
        while not accepted:
            print(f"Try {guess}")
            new_knowns = input("Yellow letters: ")
            accepted = False if new_knowns.lower() == "refresh" else True
            if not accepted:
                possible = [x for x in possible if x != guess]
        unguessed = [x for x in unguessed if x not in guess]
        new_with_position = input("Green letters (ex: '-a--e'): ")
        known_letters = update_known_letters(new_knowns, known_letters, guess)
        known_positions = update_known_positions(
            new_with_position, known_positions)
        possible = matches(possible, known_letters, known_positions)
        guess = rank(possible, unguessed)[-1]
        guess_number += 1


def matches(possible, known_letters, known_positions={}):
    for char, t in known_letters.items():
        possible = [x for x in possible if t[0] <= x.count(char)]
        for pos in t[1]:
            possible = [x for x in possible if x[pos] != char]
    for idx, char in known_positions.items():
        if char.isalpha():
            possible = [x for x in possible if x[idx] == char]
    return possible


def main(known_letters, known_positions):
    wp = "words.txt"
    possible = [x.strip().lower() for x in [*open(wp)] if len(x.strip()) == 5]
    if known_letters or known_positions:
        return matches(possible,
                       update_known_letters(known_letters),
                       update_known_positions(known_positions))
    intro_string = (
        "Sometimes words in the dictionary used by Wordler aren't words in "
        "the dictionary used by a Wordle implementation. When a word is in "
        "both our dictionary and thiers it is refered to as 'accepted'. "
        "If the word is not 'accepted', when prompted for YELLOW letters "
        "instead type REFRESH, to get a new word.")
    print(intro_string)
    return repl(possible)


if __name__ == "__main__":
    known_letters = ""
    if len(sys.argv) >= 2:
        known_letters = sys.argv[1]
    known_positions = ""
    if len(sys.argv) >= 3:
        known_positions = sys.argv[2]
    result = main(known_letters, known_positions)
    if result:
        for word in sorted(set(result)):
            print(word)
