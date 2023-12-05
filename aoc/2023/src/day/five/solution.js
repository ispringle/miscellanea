import { chunk, range } from '../utils';

class MapperOne {
  /**
   * @param {string} from
   * @param {string} to
   */
  constructor(from, to) {
    this.from = from;
    this.to = to;
    /** @type [number, number, number][] */
    this.mapped = [];
  }

  /**
   *
   * @param {number} d destination
   * @param {number} s source
   * @param {number} o offset
   */
  add(d, s, o) {
    this.mapped.push([s, s + o, d]);
  }

  /**
   *
   * @param {number} start the starting place for previous value
   */
  destination(start) {
    return this.mapped.reduce((found, [source, max, dest]) => {
      return source <= start && start < max ? dest + (start - source) : found;
    }, start);
  }
}

class MapperTwo extends MapperOne {
  constructor() {
    super();
  }
}

const partOne = ([seeds, seedMaps]) =>
  Math.min(
    ...seeds.map((seed) =>
      seedMaps.reduce((next, map) => map.destination(next), seed),
    ),
  );

const partTwo = ([seeds, seedMaps]) =>
  Math.min(
    ...chunk(seeds, 2).map(([start, length]) =>
      Math.min(
        ...range(length, start).map((seed) =>
          seedMaps.reduce((next, map) => map.destination(next), seed),
        ),
      ),
    ),
  );

const parse = (input, Mapper) => {
  const [s, ...pages] = input.split('\n\n');
  const seeds = s.split(':')[1].trim().split(' ').map(Number);
  const maps = [];
  let curr = null;
  pages.forEach((page) => {
    const [mapHeader, ...rules] = page.split('\n');
    curr = new Mapper(...mapHeader.split('map:')[0].split('-to-'));
    rules.forEach((rule) => curr.add(...rule.split(' ').map(Number)));
    maps.push(curr);
  });
  return [seeds, maps];
};

/**
 * @param {string} input
 * @returns [any, any]
 */
export default function solver(input) {
  return [partOne(parse(input, MapperOne)), partTwo(parse(input, MapperTwo))];
}
