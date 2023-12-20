const NUM_RE = /^\d$/;

/**
 * @param {string} char
 * @returns boolean
 */
export const isNumber = (char) => NUM_RE.test(char);

/**
 * @param {number} length
 * @param {number} start
 * @returns number[]
 */
export const range = (length, start = 0) =>
  start === 0
    ? [...Array(length).keys()]
    : [...Array(length).keys()].map((i) => i + start);

/**
 * @param {number} start
 * @param {number} end
 * @returns number[]
 */
export const rangeFrom = (start, end) => range(end - start, start);

/**
 * @param {number[]} array
 * @returns number
 */
export const sum = (array) => array.reduce((acc, n) => n + acc);

/**
 * @template {T}
 *
 * @param {T[]} array
 * @returns [T][]
 */
export const chunk = (array, size = 1) => {
  let chunked = [];
  for (let i = 0; i < array.length; i = i + size) {
    chunked.push(array.slice(i, i + size));
  }
  return chunked;
};

/**
 * 
 * @param {array} arrOne 
 * @param {array} arrTwo 
 * @returns array
 */
export const interleave = (arrOne, arrTwo) =>
  arrOne.map((x, i) => [x, arrTwo[i]]).reduce((a, b) => a.concat(b));

/**
 * 
 * @param  {...number} ints 
 * @returns number
 */
export const product = (...ints) => ints.reduce((acc, x) => acc * x, 1);

/**
 * @param {[][]} arr
 * @param {[x:  number, y: number]} coord
 * @returns any[]
 */
export const squareNeighbors = (arr, [x, y]) =>
  [
    y > 0 ? [x, y - 1] : [],
    x > 0 ? [x - 1, y] : [],
    x < arr[0].length - 1 ? [x + 1, y] : [],
    y < arr.length - 1 ? [x, y + 1] : [],
  ].filter((coord) => coord.length !== 0);

/**
 * @param {[][]} arr 
 * @param {[x:  number, y: number]} coord 
 * @returns any[]
 */
export const neighbors = (arr, [x, y]) =>
  [
    ...(y > 0
      ? [
          [x, y - 1],
          x > 0 ? [x - 1, y - 1] : [],
          x < arr[0].length - 1 ? [x + 1, y - 1] : [],
        ]
      : []),
    ...[x > 0 ? [x - 1, y] : [], x < arr[0].length - 1 ? [x + 1, y] : []],
    ...(y < arr.length
      ? [
          [x, y + 1],
          x > 0 ? [x - 1, y + 1] : [],
          x < arr[0].length - 1 ? [x + 1, y + 1] : [],
        ]
      : []),
  ].flatMap(([x, y]) => (x === undefined ? [] : arr[y][x]));

/**
 *
 * @param {[]} a
 * @param {[]} b
 * @returns boolean
 */
export const arraysMatch = (a, b) =>
  a.length === b.length && a.every((el, i) => el === b[i]);