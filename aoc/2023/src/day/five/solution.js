import { chunk } from '../utils/index.js';

/**
 *
 * @param {number} start the starting place for previous value
 * @param {[number, number, number][]} map array of maps
 * @returns number
 */
const destination = (start, map) => {
  return map.reduce((found, [dest, source, offset]) => {
    return source <= start && start < source + offset
      ? dest + (start - source)
      : found;
  }, start);
};

const partOne = ([seeds, seedMaps]) =>
  Math.min(
    ...seeds.map((seed) =>
      seedMaps.reduce((next, map) => destination(next, map), seed),
    ),
  );

const partTwo = ([seeds, seedMaps]) => {
  const locations = [];
  chunk(seeds, 2).forEach(([begin, len]) => {
    let ranges = Array([begin, begin + len]);
    let res = [];
    seedMaps.forEach((map) => {
      while (ranges.length !== 0) {
        let [startRange, endRange] = ranges.pop();
        let found = false;
        for (const [target, startMap, r] of map) {
          const endMap = startMap + r;
          const offset = target - startMap;
          if (endMap <= startRange || endRange <= startMap) {
            continue;
          }
          if (startRange < startMap) {
            ranges.push([startRange, startMap]);
            startRange = startMap;
          }
          if (endMap < endRange) {
            ranges.push([endMap, endRange]);
            endRange = endMap;
          }
          res.push([startRange + offset, endRange + offset]);
          found = true;
          break;
        }
        if (!found) {
          res.push([startRange, endRange]);
        }
      }
      ranges = res;
      res = [];
    });
    locations.push(...ranges.map(range => range[0]));
  });
  return Math.min(...locations)
};

const parse = (input) => {
  const [s, ...pages] = input.split('\n\n');
  const seeds = s.split(':')[1].trim().split(' ').map(Number);
  const maps = [];
  pages.forEach((page) => {
    // eslint-disable-next-line no-unused-vars
    const [mapHeader, ...rules] = page.split('\n');
    maps.push(rules.map((rule) => rule.split(' ').map(Number)));
  });
  return [seeds, maps];
};

/**
 * @param {string} input
 * @returns [any, any]
 */
export default function solver(input) {
  return [partOne(parse(input)), partTwo(parse(input))];
}
