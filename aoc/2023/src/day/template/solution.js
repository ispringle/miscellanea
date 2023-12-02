const partOne = (input) => {
  input.split();
  return 'one';
};

const partTwo = (input) => {
  input.split();
  return 'two';
};

/**
 * @param {string} inputOne
 * @param {string} inputTwo
 * @returns [any, any]
 */
export default function solver(inputOne, inputTwo) {
  return [partOne(inputOne), partTwo(inputTwo)];
}
