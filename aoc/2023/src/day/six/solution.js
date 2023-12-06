import { chunk, interleave, product } from '../utils';

const f = (t, r) => Math.sqrt(t ** 2 - 4 * r)

const solve = (input) =>
  product(
    ...input.map(
      ([time, record]) =>
        Math.ceil((time + f(time, record)) / 2) -
        Math.floor((time - f(time, record)) / 2) -
        1,
    ),
  );

const parseOne = (input) =>
  chunk(
    interleave(
      ...input.split('\n').map((line) =>
        line
          .split(':')[1]
          .split(' ')
          .flatMap((x) => (x === '' ? [] : [Number(x.trim())])),
      ),
    ),
    2,
  );

const parseTwo = (input) =>
  input
    .split('\n')
    .map((line) =>
      line
        .split(':')[1]
        .split(' ')
        .reduce((acc, s) => acc + s, ''),
    )
    .map(Number);

/**
 * @param {string} inputOne
 * @param {string} inputTwo
 * @returns [any, any]
 */
export default function solver(input) {
  return [solve(parseOne(input)), solve([parseTwo(input)])];
}
