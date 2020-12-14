class Solver:
    def __init__(self, input_file):
        self.input = self.parse(input_file)

    def bits(self, value, mask_len):
        return bin(value)[2:].zfill(mask_len)

    def parse(self, input_file):
        def _parse(line):
            a, b = line.strip().split(" = ")
            if a == "mask":
                return a, b
            else:
                return int(a[4:-1]), b
        return list(map(_parse, open(input_file).readlines()))

    def part_one(self):
        memory = {}
        for instruction, value in self.input:
            if instruction == "mask":
                mask = value
                continue
            value = self.bits(int(value), len(mask))
            value = int(
                ''.join(v if m == 'X' else m for v, m in zip(value, mask)),
                2)
            memory[instruction] = value
        return sum(memory.values())

    # there was to be a more succinct way of doing this
    def part_two(self):
        memory = {}
        for instruction, value in self.input:
            if instruction == 'mask':
                mask = value
                continue
            address = self.bits(instruction, len(mask))
            address_template = ''
            for mask_bit, address_bit in zip(mask, address):
                if mask_bit == "0":
                    address_template += address_bit
                elif mask_bit == "1":
                    address_template += "1"
                else:
                    address_template += "{}"
            floating_length = mask.count('X')
            for f in range(2 ** floating_length):
                address = address_template.format(
                    *self.bits(f, floating_length))
                address = int(address, 2)
                memory[address] = int(value)
        return sum(memory.values())

    def solve(self):
        print(f"Part One: {self.part_one()}")
        s = self.part_two()
        if s is not None:
            print(f"Part Two: {s}")
