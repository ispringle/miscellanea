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
    loop.push(next)
  }
  if (arraysMatch(start, next)) {
    return loop;
  }
  return [];
};

/**
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

const partTwo = (input) => {
  return input;
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
export default function solver(input) {
  const parsed = parse(input);
  const loop = findLoop(parsed);
  console.log(loop)
  return [Math.ceil(loop.length / 2), partTwo(parsed)];
}
