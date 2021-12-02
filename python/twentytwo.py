class Solver:
    def __init__(self, input_file):
        self.input = self.parse(input_file)

    def parse(self, input_file):
        return [list(map(int, x.split("\n")[1:]))
                for x in open(input_file).read().split("\n\n")
                if x]

    def part_one(self):
        player, other = self.input
        while player and other:
            p_card, o_card = player[0], other[0]
            player, other = player[1:], other[1:]
            if p_card > o_card:
                player += [p_card, o_card]
            else:
                other += [o_card, p_card]
        return self.score(player if player else other)

    def part_two(self):
        def play(player, other):
            seen = set()
            while player and other:
                state = (tuple(player), tuple(other))
                if state in seen:
                    return True, self.score(player)
                seen.add(state)
                p_card, o_card = player[0], other[0]
                player, other = player[1:], other[1:]
                if len(player) < p_card or len(other) < o_card:
                    if p_card > o_card:
                        player += [p_card, o_card]
                    else:
                        other += [o_card, p_card]
                else:
                    winner, _ = play(player[:p_card], other[:o_card])
                    if winner:
                        player += [p_card, o_card]
                    else:
                        other += [o_card, p_card]
            if player:
                return True, self.score(player)
            else:
                return False, self.score(other)

        player, other = self.input
        return play(player, other)[1]

    def score(self, deck):
        return sum(
            map(
                lambda x: x[0]*x[1],
                list(
                    enumerate(
                        reversed(deck + [0])))))

    def solve(self):
        print(f"Part One: {self.part_one()}")
        s = self.part_two()
        if s is not None:
            print(f"Part Two: {s}")
