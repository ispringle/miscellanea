const map = {
  one: '1',
  1: '1',
  two: '2',
  2: '2',
  three: '3',
  3: '3',
  four: '4',
  4: '4',
  five: '5',
  5: '5',
  six: '6',
  6: '6',
  seven: '7',
  7: '7',
  eight: '8',
  8: '8',
  nine: '9',
  9: '9',
  0: '0',
};

const RE_ONE = /\d/g;
const RE_TWO = new RegExp(
  `(?=(${Object.keys(map).reduce(
    (acc, s) => (acc === '' ? s : `${acc}|${s}`),
    '',
  )}))`,
  'g',
);

/**
 * @param {number[]} input
 * @returns number
 */
const sumArr = (input) => input.reduce((acc, x) => acc + x, 0);

/**
 * @param {string} input
 * @param {RegExp} re
 * @returns number[]
 */
const parse = (input, re) => {
  console.log(re);
  return input.split('\n').map((line) => {
    let [first, ...rest] = Array.from(line.matchAll(re), (x) => x[1]);
    if (first === undefined) {
      [first, ...rest] = line.match(re);
    }
    const [last = first] = rest.splice(-1);
    return Number(`${map[first]}${map[last]}`);
  });
};

/**
 * @param {string} inputOne
 * @param {string} inputTwo
 * @returns [any, any]
 */
export default function solver(inputOne, inputTwo) {
  return [sumArr(parse(inputOne, RE_ONE)), sumArr(parse(inputTwo, RE_TWO))];
}
