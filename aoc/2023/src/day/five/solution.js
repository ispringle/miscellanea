import { chunk, range } from '../utils/index.js';

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
    ...chunk(seeds, 2).map(([start, length]) =>
      Math.min(
        ...range(length, start).map((seed) =>
          seedMaps.reduce((next, map) => destination(next, map), seed),
        ),
      ),
    ),
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
