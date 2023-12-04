const NUM_RE = /^\d$/;
export const isNumber = (char) => NUM_RE.test(char);

export const range = (length, start = 0) =>
  start === 0
    ? [...Array(length).keys()]
    : [...Array(length).keys()].map((i) => i + start);

export const rangeFrom = (start, end) => range(end - start, start);
 export const sum = array => array.reduce((acc, n) => n + acc)