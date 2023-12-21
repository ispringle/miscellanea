import { arraysMatch, squareNeighbors } from '../utils';

/**
 * @typedef {[string[], number, number]} Parsed map, length, width
 */

const follow = (arr, prevCoords, [x, y]) => {
  if (arr[y][x] === '|') {
    return arraysMatch(prevCoords, [x, y - 1]) ? [x, y + 1] : [x, y - 1];
  } else if (arr[y][x] === '-') {
    return arraysMatch(prevCoords, [x - 1, y]) ? [x + 1, y] : [x - 1, y];
  } else if (arr[y][x] === 'L') {
    return arraysMatch(prevCoords, [x + 1, y]) ? [x, y - 1] : [x + 1, y];
  } else if (arr[y][x] === 'J') {
    return arraysMatch(prevCoords, [x - 1, y]) ? [x, y - 1] : [x - 1, y];
  } else if (arr[y][x] === '7') {
    return arraysMatch(prevCoords, [x - 1, y]) ? [x, y + 1] : [x - 1, y];
  } else if (arr[y][x] === 'F') {
    return arraysMatch(prevCoords, [x + 1, y]) ? [x, y + 1] : [x + 1, y];
  } else if (arr[y][x] === '.') {
    return [x, y];
  } else if (arr[y][x] === 'S') {
    return [x, y];
  }
};

const route = (grid, prev, next) => {
  const start = prev;
  let loop = [next];
  while (!arraysMatch(start, next) && !arraysMatch(prev, next)) {
    [prev, next] = [next, follow(grid, prev, next)];
    loop.push(next);
  }
  if (arraysMatch(start, next)) {
    return loop;
  }
  return [];
};

/**
 * Get 2D cross product
 * @param {[number, number]} a
 * @param {[number, number]} b
 * @returns number
 */
const cross = (a, b) => a[0] * b[1] - a[1] * b[0];

/**
 * Get area of polygon via shoelace formula
 * @param {[number, number][]} matrix
 * @returns number
 */
const area = (matrix) =>
  Math.abs(matrix.reduce(
    (acc, _, i) =>
      i < matrix.length - 1 ? acc + cross(matrix[i], matrix[i + 1]) : acc,
    0,
  ) / 2);

/**
 * Follows all possible paths, only two (out of a max of four) will return to
 * start, as soon as we find any path that returns to start we can "break",
 * which we do in a reduce by just returning the already calculated path.
 * @param {Parsed} input
 * @returns any
 */
const findLoop = (input) => {
  const start = input.reduce(
    (loc, line, i) =>
      line.includes('S') ? [line.findIndex((char) => char === 'S'), i] : loc,
    [],
  );
  return squareNeighbors(input, start)
    .filter(([x, y]) => input[y][x] !== '.')
    .reduce(
      (loop, coord) => (loop.length === 0 ? route(input, start, coord) : loop),
      [],
    );
};

/**
 * @param {string} input
 * @returns Parsed
 */
const parse = (input) => input.split('\n').map((line) => [...line]);

/**
 * @param {string} input
 * @returns [any, any]
 */
export default function solver(input, inputTwo) {
  const loop = findLoop(parse(inputTwo));
  const loopLength = Math.ceil(loop.length / 2);
  const loopArea = area(loop);
  const innerTiles = Math.floor(loopArea) - loopLength + 1
  return [loopLength, innerTiles];
}
