import { isNumber, rangeFrom } from '../utils';

const symbolNeighbor = (input, startLoc, endX) => {
  let loc = [];
  const yRange = [
    // eslint-disable-next-line no-undef
    ...new Set([
      startLoc[1] === 0 ? startLoc[1] : startLoc[1] - 1,
      startLoc[1],
      startLoc[1] === input.length - 1 ? startLoc[1] : startLoc[1] + 1,
    ]),
  ];

  const xRange = rangeFrom(
    startLoc[0] === 0 ? startLoc[0] : startLoc[0] - 1,
    endX === input[0].length - 1 ? endX : endX + 1,
  );

  yRange.forEach((y) => {
    xRange.forEach((x) => {
      const char = input[y][x];
      if (char !== '.' && !isNumber(char)) {
        loc = [x, y];
      }
    });
  });
  return loc;
};

const solve = (input) => {
  const gears = {};
  input.forEach((line, y) =>
    line.forEach((char, x) => {
      if (char === '*') gears[`${x},${y}`] = [];
    }),
  );

  let num = '';
  let startLoc = [];
  const parts = [];
  input.forEach((line, y) =>
    line.forEach((char, x) => {
      if (isNumber(char)) {
        if (startLoc.length === 0) {
          startLoc = [x, y];
        }
        num = num + char;
      }
      if (num && (!isNumber(char) || x === input[y].length - 1)) {
        const [nX, nY] = symbolNeighbor(input, startLoc, x);
        if (nX) {
          parts.push(Number(num));
          if (input[nY][nX] === '*') gears[`${nX},${nY}`].push(num);
        }
        num = '';
        startLoc = [];
      }
    }),
  );
  return [
    parts.reduce((acc, n) => n + acc, 0),
    Object.values(gears)
      .filter((set) => set.length === 2)
      .reduce((acc, set) => acc + set[0] * set[1], 0),
  ];
};

const parse = (input) =>
  input
    .trim()
    .split('\n')
    .map((line) => line.split(''));

/**
 * @param {string} input
 * @returns [number, number]
 */
export default function solver(input) {
  return solve(parse(input));
}
