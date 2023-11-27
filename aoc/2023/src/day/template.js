const partOne = (input) => {
  input.split();
  return 'one';
};

const partTwo = (input) => {
  input.split();
  return 'two';
};

export default function dayOneSolver(input) {
  return [partOne(input), partTwo(input)];
}
