/**
 * @typedef {[string[], number, number]} Parsed map, length, width
 */

/**
 *
 * @param {[]} a
 * @param {[]} b
 * @returns boolean
 */
const arraysMatch = (a, b) =>
  a.length === b.length && a.every((el, i) => el === b[i]);

/**
 * @param {[][]} arr
 * @param {[x:  number, y: number]} coord
 * @returns any[]
 */
const neighbors = (arr, [x, y]) =>
  [
    y > 0 ? [x, y - 1] : [],
    x > 0 ? [x - 1, y] : [],
    x < arr[0].length - 1 ? [x + 1, y] : [],
    y < arr.length - 1 ? [x, y + 1] : [],
  ].filter((coord) => coord.length !== 0);

const follow = (arr, prevCoords, path) => {
  const [x, y] = path.at(-1)
  console.log(path)
  let next = [];
  if (arr[y][x] === '|') {
    next = arraysMatch(prevCoords, [x, y - 1]) ? [x, y + 1] : [x, y - 1];
  } else if (arr[y][x] === '-') {
    next = arraysMatch(prevCoords, [x - 1, y]) ? [x + 1, y] : [x - 1, y];
  } else if (arr[y][x] === 'L') {
    next = arraysMatch(prevCoords, [x + 1, y]) ? [x, y - 1] : [x + 1, y];
  } else if (arr[y][x] === 'J') {
    next = arraysMatch(prevCoords, [x - 1, y]) ? [x, y - 1] : [x - 1, y];
  } else if (arr[y][x] === '7') {
    next = arraysMatch(prevCoords, [x - 1, y]) ? [x, y + 1] : [x - 1, y];
  } else if (arr[y][x] === 'F') {
    next = arraysMatch(prevCoords, [x + 1, y]) ? [x, y + 1] : [x + 1, y];
  } else if (arr[y][x] === '.') {
    return [];
  } else if (arr[y][x] === 'S') {
    return path;
  }
  return follow(arr, [x, y], [...path, next]);
};

const printMap = (arr, path) => {
  const m = arr.map((line, y) =>
    line.map((char, x) =>
      path.map((coord) => coord.toString()).includes(`${x},${y}`) ? char : ' ',
    ),
  );
  console.log(m);
};

/**
 * @param {Parsed} input
 * @returns any
 */
const partOne = (input) => {
  const start = input.reduce(
    (loc, line, i) =>
      line.includes('S') ? [line.findIndex((char) => char === 'S'), i] : loc,
    [],
  );
  const x = neighbors(input, start)
    .filter(([x, y]) => input[y][x] !== '.')
    .reduce((path, coord) => path.length === 0 ? follow(input, start, [coord]) : path, []);
  x.forEach((path) => printMap(input, path));
  return input;
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
  return [partOne(parsed), partTwo(parsed)];
}
