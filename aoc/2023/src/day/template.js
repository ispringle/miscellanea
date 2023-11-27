const partOne = (input) => {
  input.split();
  return 'one';
};

const partTwo = (input) => {
  input.split();
  return 'two';
};

export function solver(input) {
  return [partOne(input), partTwo(input)];
}
