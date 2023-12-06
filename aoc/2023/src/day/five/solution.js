import { chunk } from '../utils/index.js';

/**
 *
 * @param {number} start the starting place for previous value
 * @param {[number, number, number][]} map array of maps
 * @returns number
 */
const destination = (start, map) => {
  return map.reduce((found, [source, max, dest]) => {
    return source <= start && start < max ? dest + (start - source) : found;
  }, start);
};

const partOne = ([seeds, seedMaps]) =>
  Math.min(
    ...seeds.map((seed) =>
      seedMaps.reduce((next, map) => destination(next, map), seed),
    ),
  );

const partTwo = ([seeds, seedMaps]) =>
  Math.min(
    ...chunk(seeds, 2).flatMap(([begin, len]) => {
      let ranges = Array([begin, begin + len]);
      let res = [];
      seedMaps.forEach((map) => {
        while (ranges.length !== 0) {
          let [start, end] = ranges.pop();
          let found = false;
          for (const [source, max, dest] of map) {
            const diff = dest - source;
            if (max <= start || end <= source) {
              continue;
            }
            if (start < source) {
              ranges.push([start, source]);
              start = source;
            }
            if (max < end) {
              ranges.push([max, end]);
              end = max;
            }
            res.push([start + diff, end + diff]);
            found = true;
            break;
          }
          if (!found) {
            res.push([start, end]);
          }
        }
        ranges = res;
        res = [];
      });
      return ranges.map((range) => range[0]);
    }),
  );

const parse = (input) => {
  const [s, ...pages] = input.split('\n\n');
  const seeds = s.split(':')[1].trim().split(' ').map(Number);
  const maps = [];
  pages.forEach((page) => {
    // eslint-disable-next-line no-unused-vars
    const [mapHeader, ...rules] = page.split('\n');
    maps.push(
      rules.map((rule) => {
        const [dest, source, offset] = rule.split(' ').map(Number);
        return [source, source + offset, dest];
      }),
    );
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
