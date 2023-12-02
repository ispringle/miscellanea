const parse = (input) =>
  input.split('\n').map((game) => ({
    red: Math.max(
      ...game.match(/\d+ red/g).map((s) => Number(s.match(/\d+/)[0])),
    ),
    blue: Math.max(
      ...game.match(/\d+ blue/g).map((s) => Number(s.match(/\d+/)[0])),
    ),
    green: Math.max(
      ...game.match(/\d+ green/g).map((s) => Number(s.match(/\d+/)[0])),
    ),
  }));

const partOne = (input, rules) =>
  input
    .map((max, i) =>
      Object.entries(max).every(([c, n]) => rules[c] >= n) ? i + 1 : 0,
    )
    .reduce((acc, n) => acc + n, 0);

const partTwo = (input) =>
  input
    .map((max) => Object.values(max).reduce((acc, x) => x * acc, 1))
    .reduce((acc, n) => acc + n, 0);

/**
 * @param {string} inputOne
 * @param {string} inputTwo
 * @returns [number, number]
 */
export default function solver(input) {
  const rules = {
    red: 12,
    green: 13,
    blue: 14,
  };

  const parsed = parse(input);
  return [partOne(parsed, rules), partTwo(parsed)];
}
