/**
 * @typedef {[string, object]} Parsed
 */

/**
 * @param {number} a 
 * @param {number} b 
 * @returns number
 */
const gcd = (a, b) => {
  while (b > 0) [a, b] = [b, a % b];
  return a;
};

/**
 * @param {number} a 
 * @param {number} b 
 * @returns number
 */
const lcm = (a, b) => (a * b) / gcd(a, b);

/**
 * @param {string} str 
 * @returns [string, string]
 */
const next = (str) => {
  const [first, ...rest] = [...str];
  return [first, rest.join('') + first];
};

/**
 * @param {string} instructions 
 * @param {object} network 
 * @param {string} location 
 * @param {function(string): boolean} test 
 * @returns 
 */
const stepTo = (instructions, network, location, test) => {
  let steps = 0;
  while (!test(location)) {
    const [nextInst, insts] = next(instructions);
    instructions = insts;
    location = nextInst === 'L' ? network[location][0] : network[location][1];
    steps = steps + 1;
  }
  return steps;
};

/**
 * @param {Parsed} input
 * @returns number
 */
const partOne = (input) => stepTo(...input, 'AAA', (loc) => loc === 'ZZZ');

/**
 * 
 * @param {Parsed} input 
 * @returns number
 */
const partTwo = (input) =>
  Object.keys(input[1])
    .filter((loc) => loc.endsWith('A'))
    .map((loc) => stepTo(...input, loc, (l) => l.endsWith('Z')))
    .reduce((least, next) => lcm(least, next), 1);

/**
 * @param {string} input
 * @returns Parsed
 */
const parse = (input) => {
  const [instructions, network] = input.split('\n\n');
  return [
    instructions,
    network.split('\n').reduce((obj, line) => {
      const [curr, ...next] = line.match(/[A-Z\d]{3}/g);
      return { ...obj, ...{ [curr]: next } };
    }, {}),
  ];
};

/**
 * @param {string} input
 * @returns [any, any]
 */
export default function solver(inputOne, inputTwo) {
  return [partOne(parse(inputOne)), partTwo(parse(inputTwo))];
}
