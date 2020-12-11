OCCUPIED, EMPTY, FLOOR = '#L.'


class Solver:
    def __init__(self, input_file):
        self.input = self.parse(input_file)

    def count_neighbors(self, x, y, grid):
        coord, w = self.idx(x, y), self.width
        min_x = False if x > 0 else True
        max_x = False if x < w - 1 else True
        min_y = False if y > 0 else True
        max_y = False if y < self.height - 1 else True
        neighbors = 0

        if not min_x:
            # Left
            neighbors += 1 if grid[coord-1] == OCCUPIED else 0
        if not max_x:
            # Right
            neighbors += 1 if grid[coord+1] == OCCUPIED else 0
        if not max_y:
            # Down one
            neighbors += 1 if grid[coord+w] == OCCUPIED else 0
            if not min_x:
                # Down one, left one
                neighbors += 1 if grid[coord-1+w] == OCCUPIED else 0
            if not max_x:
                # Down one, right one
                neighbors += 1 if grid[coord+1+w] == OCCUPIED else 0
        if not min_y:
            # Up one
            neighbors += 1 if grid[coord-w] == OCCUPIED else 0
            if not min_x:
                # Up one, left one
                neighbors += 1 if grid[coord-1-w] == OCCUPIED else 0
            if not max_x:
                # Up one, right one
                neighbors += 1 if grid[coord+1-w] == OCCUPIED else 0
        return neighbors

    def count_visible(self, x, y, grid):
        visible = 0
        w, h = self.width, self.height
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                if (dx, dy) == (0, 0):
                    continue
                cx = x + dx
                cy = y + dy
                while 0 <= cx < w and 0 <= cy < h:
                    square = grid[self.idx(cx, cy)]
                    if square == FLOOR:
                        cx += dx
                        cy += dy
                    else:
                        break
                if 0 <= cx < w and 0 <= cy < h:
                    square = grid[self.idx(cx, cy)]
                    visible += 1 if square == OCCUPIED else 0
        return visible

    def idx(self, x, y):
        return y * self.width + x

    def parse(self, input_file):
        data = open(input_file).read()
        self.width = data.find("\n")
        self.height = data.count("\n")
        return [x for y in data for x in y.replace("\n", "")]

    def part_one(self):
        grid = self.input[:]
        while True:
            prior = grid[:]
            # self.print_grid(grid)
            for y in range(self.height):
                for x in range(self.width):
                    square = grid[self.idx(x, y)]
                    if square == FLOOR:
                        continue
                    n = self.count_neighbors(x, y, prior)
                    if square == EMPTY and n == 0:
                        grid[self.idx(x, y)] = OCCUPIED
                    if square == OCCUPIED and n >= 4:
                        grid[self.idx(x, y)] = EMPTY
            if grid == prior:
                break
        return grid.count(OCCUPIED)

    def part_two(self):
        grid = self.input[:]
        while True:
            prior = grid[:]
            for y in range(self.height):
                for x in range(self.width):
                    square = grid[self.idx(x, y)]
                    if square == FLOOR:
                        continue
                    n = self.count_visible(x, y, prior)
                    if square == EMPTY and n == 0:
                        grid[self.idx(x, y)] = OCCUPIED
                    if square == OCCUPIED and n >= 5:
                        grid[self.idx(x, y)] = EMPTY
            if grid == prior:
                break
        return grid.count(OCCUPIED)

    def print_grid(self, grid):
        w = self.width
        for h in range(self.height):
            print(''.join(grid[h*w:(h+1)*w]))
        print()

    def solve(self):
        print(f"Part One: {self.part_one()}")
        s = self.part_two()
        if s is not None:
            print(f"Part Two: {s}")
