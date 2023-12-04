const partOne = (input) =>
  Object.values(input)
    .map(
      ([{ winners, numbers }]) =>
        numbers
          .filter((n) => winners.includes(n))
          .reduce((acc, _n) => (acc === 0 ? 1 : acc * 2), 0), // eslint-disable-line no-unused-vars
    )
    .reduce((acc, x) => acc + x, 0);

const partTwo = (input) => {
  Object.entries(input).forEach(([cardNumber, cards]) =>
    cards.forEach(({ winners, numbers }) => {
      let inc = Number(cardNumber);
      numbers
        .filter((n) => winners.includes(n))
        .forEach(() => {
          inc++;
          const copy = input[inc][0];
          input[inc].push(copy);
        });
    }),
  );
  return Object.values(input).reduce((acc, cards) => cards.length + acc, 0);
};

const parse = (input) =>
  input
    .trim()
    .split('\n')
    .reduce(
      (acc, card, i) => ({
        ...acc,
        ...{
          [i + 1]: [
            {
              winners: card
                .split(':')[1]
                .trim()
                .split('|')[0]
                .trim()
                .split(' ')
                .filter((x) => x !== '')
                .map((x) => Number(x)),
              numbers: card
                .split(':')[1]
                .trim()
                .split('|')[1]
                .trim()
                .split(' ')
                .filter((x) => x !== '')
                .map((x) => Number(x)),
            },
          ],
        },
      }),
      {},
    );

/**
 * @param {string} inputOne
 * @returns [any, any]
 */
export default function solver(input) {
  const parsed = parse(input);
  return [partOne(parsed), partTwo(parsed)];
}
