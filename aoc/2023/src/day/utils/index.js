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
 export const sum = array => array.reduce((acc, n) => n + acc)