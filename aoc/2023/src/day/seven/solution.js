/**
 * The idea here is to take every hand, score it by the number of occurences of
 * a card, take the best possible score for each hand (if wilds are in the
 * hand), and then sort. The best hand will be at the top (`reverse`) and then
 * we can reduce this array of sorted hands to tally up the score.
 * 
 * @typedef {string} Hand
 * @typedef {number} Bid
 * @typedef {[Hand, Bid]} HandSet
 * @typedef {HandSet[]} Parsed
 */

/**
 * Count the number of times `char` occurs in `str`
 * This returns a func, so that it can be used with
 * `.map()` and iterate over chars in an array.
 * @param {string} str
 * @returns function(char: sting): number
 */
const occurences =
  (str) =>
  /**
   * @function
   * @param {string} char
   * @returns number
   */
  (char) =>
    str.match(new RegExp(`${char}`, 'g') || []).length;

/**
 * Returns all possible hand scores, considering wild cards
 * @param {string} hand
 * @returns [number, number, number, number, number]
 */
const possible = (hand) =>
  [...hand]
    .map((card) => {
      const variant = hand.replaceAll('0', card);
      return [...variant].map(occurences(variant)).sort().reverse();
    })
    .sort();

/**
 * @param {Parsed} input
 * @returns number
 */
const solve = (input) =>
  input
    .map(([hand, bid]) => [possible(hand).pop(), hand, bid])
    .sort()
    .reduce((acc, hand, index) => acc + hand[2] * (index + 1), 0);

/**
 * @param {string} input
 * @returns Parsed
 */
const parse = (input, mapping) =>
  input.split('\n').map((line) => {
    const [hand, bid] = line.split(' ');
    return [hand.replace(/[AKQJT]/g, (c) => mapping[c]), Number(bid)];
  });

/**
 * @param {string} input
 * @returns [any, any]
 */
export default function solver(input) {
  const mapping = {
    T: 'A',
    J: 'B',
    Q: 'C',
    K: 'D',
    A: 'E',
  };
  const one = solve(parse(input, mapping));
  mapping['J'] = 0;
  return [one, solve(parse(input, mapping))];
}
