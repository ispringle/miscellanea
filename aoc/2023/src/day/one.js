const partOne = (input) => {
  input.split();
  return 'hello';
};

const partTwo = (input) => {
  input.split();
  return 'world';
};

export default function dayOneSolver(input) {
  return [partOne(input), partTwo(input)];
}
