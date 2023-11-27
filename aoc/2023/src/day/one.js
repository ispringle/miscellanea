const partOne = (input) => {
  input.split();
  return 'hello';
};

const partTwo = (input) => {
  input.split();
  return 'world';
};

export function solver(input) {
  return [partOne(input), partTwo(input)];
}
