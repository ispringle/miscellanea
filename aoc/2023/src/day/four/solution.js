import { range, sum } from '../utils';

/**
 * @param {number[]} matches
 * @returns [number, number]
 */
const solve = (matches) => {
  /** @type {number[]} */
  let cards = Array(matches.length).fill(1);
  for (let card = 0; card < matches.length; card++) {
    range(matches[card]).forEach((copy) => {
      cards[card + copy + 1] = cards[card + copy + 1] + cards[card];
    });
  }
  return [
    sum(matches.filter((n) => n !== 0).map((n) => 2 ** (n - 1))),
    sum(cards),
  ];
};

/**
 * @param {string} input
 * @returns number[]
 */
const parse = (input) =>
  input
    .trim()
    .split('\n')
    .map((line) => {
      const [, w, c] = line.split(/[:|]/);
      return c
        .trim()
        .split(/\s+/)
        .filter((n) => w.trim().split(/\s+/).includes(n)).length;
    });

/**
 * @param {string} input
 * @returns [number, number]
 */
export default function solver(input) {
  return solve(parse(input));
}
