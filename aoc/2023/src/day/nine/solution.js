import { sum } from '../utils';

/**
 * @typedef {number[][]} Parsed
 */

/**
 * @param {number[]} seq
 * @returns number[]
 */
const findDiffs = (seq) => {
  const diffs = [];
  for (let i = 0; i < seq.length - 1; i++) {
    diffs.push(seq[i + 1] - seq[i]);
  }
  return diffs;
};

/**
 * @param {number[]} original
 * @param {number[][]} reductions
 * @returns number[][]
 */
const reduceToZero = (reductions) =>
  reductions.at(-1).every((n) => n === 0)
    ? reductions
    : reduceToZero([...reductions, findDiffs(reductions.at(-1))]);

/**
 * @param {Parsed} input
 * @returns any
 */
const partOne = (input) =>
  sum(
    input
      .map((seq) => reduceToZero([seq]))
      .map((group) => group.reverse().reduce((next, seq) => seq.at(-1) + next, 0)),
  );

const partTwo = (input) =>
  sum(
    input
      .map((seq) => reduceToZero([seq]))
      .map((group) => group.reverse().reduce((next, seq) => seq[0] - next, 0)),
  );

/**
 * @param {string} input
 * @returns Parsed
 */
const parse = (input) =>
  input.split('\n').map((line) => line.split(' ').map((n) => Number(n)));

/**
 * @param {string} input
 * @returns [any, any]
 */
export default function solver(input) {
  const parsed = parse(input);
  console.log(partOne(parsed));
  return [partOne(parsed), partTwo(parsed)];
}
