import { chunk, interleave, product } from '../utils';

/**
 * Hello dumber, future self, this is how this works, no need to thank me.
 * Sincerely Your smarter, past self.
 *
 * `total-time` is the combination of `button-pressed-time` and `travel-time`.
 * time = button-pressed-time + travel-time
 *
 * For each unit of time the button is pressed, the boat will travel
 * one more unit of distance per unit of time:
 * distance = (total-time - button-pressed-time) * button-pressed-time
 *
 * This can be rewritten as:
 * distance = total-time * button-pressed-time - button-pressed-time^2
 *
 * `distance` and `total-time` are knowns, so we need to determine the
 * range of `button-pressed-time` that is greater than the given record.
 * But this still means iterating. So to get a single formula that will
 * give us our bounds we need to get our `button-pressed-time` on the
 * left side of the equation:
 * 0 = button-pressed-time^2 - total-time * button-pressed-time + distance
 *
 * And then to get the `button-pressed-time alone:
 * button-pressed-time = (total-time +/- √(total-time^2 - 4 * distance)) / 2
 *
 * There are two boundings so we need to do a one `+` and one `-` of this equation
 * and then get the difference of the two. These numbers might have decimals, so we
 * floor/ceil them and then add one. I don't know why I'm adding one, but when
 * I didn't it was off by one. I think it might be that distance is the record to
 * beat, so really we're looking for `distance+1` but when I had tried using
 * that in the equation is gave me a very wrong number, so this is good enough!
 */

/**
 * @param {number} t total time of race
 * @param {number} r previous distance record
 * @returns number
 */

/**
 * 
 * @param {number} t total time of race
 * @param {number} r distance record
 * @returns number
 */
const f = (t, r) => Math.sqrt(t ** 2 - 4 * r);

/**
 *
 * @param {[number, number][]} input
 * @returns number
 */
const solve = (input) =>
  product(
    ...input.map(
      ([time, record]) =>
        Math.ceil((time + f(time, record)) / 2) -
        Math.floor((time - f(time, record)) / 2) -
        1,
    ),
  );

/**
 * @param {string} input
 * @returns [number, number][]
 */
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

/**
 * @param {string} input
 * @returns [number, number]
 */
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
 * @param {string} input
 * @returns [number, number]
 */
export default function solver(input) {
  return [solve(parseOne(input)), solve([parseTwo(input)])];
}
