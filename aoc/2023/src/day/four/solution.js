import { range, sum } from '../utils';

const solve = (matches) => {
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
 * @param {string} inputOne
 * @returns [any, any]
 */
export default function solver(input) {
  return solve(parse(input));
}
