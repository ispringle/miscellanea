import { chunk, interleave, product, range } from '../utils';
const solve = (input) =>
  product(
    ...input.map(
      ([time, record]) =>
        range(time + 1)
          .map((ms) => (time - ms) * ms)
          .filter((x) => x > record).length,
    ),
  );

const parseOne = (input) =>
  chunk(
    interleave(
      ...input.split('\n').map((line) =>
        line
          .split(':')[1]
          .trim()
          .split(' ')
          .filter((x) => x !== '')
          .map((x) => Number(x.trim())),
      ),
    ),
    2,
  );

const parseTwo = (input) =>
  input.split('\n').map((line) =>
    line
      .split(':')[1]
      .trim()
      .split(' ')
      .reduce((acc, s) => acc + s, '')
  ).map(Number);

/**
 * @param {string} inputOne
 * @param {string} inputTwo
 * @returns [any, any]
 */
export default function solver(input) {
  return [solve(parseOne(input)), solve([parseTwo(input)])];
}
