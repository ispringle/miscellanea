import sys


def main(known, with_position):
    wp = "/usr/share/dict/words"
    possible = [x.lower() for x in [x.strip() for x in [*open(wp)] if len(
        x.strip()) == 5] if all(True if known.count(
            c.lower()) <= x.count(c.lower()) else False for c in known)]
    if with_position:
        for n, c in {n: c for n, c in enumerate(with_position)}.items():
            if c.isalpha():
                possible = [x for x in possible if x[n] == c.lower()]
    return possible


if __name__ == "__main__":
    known = sys.argv[1]
    with_position = ""
    if len(sys.argv) == 3:
        with_position = sys.argv[2]
    print(main(known, with_position))
