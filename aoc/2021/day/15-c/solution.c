#include <limits.h>
#include <stdio.h>

#define MIN(a, b) (((a) < (b)) ? (a) : (b))
#define SIZE 500

int const TILE_COUNT = 5;

int risks[SIZE][SIZE] = {[0 ... SIZE - 1] = {[0 ... SIZE - 1] = INT_MAX - 10}};
int map[SIZE][SIZE];

int main(void) {
  int chr, risk, cost, continueMaybe, x = 0, y = 0, width = 0;

  // Parse input, creating a risks-map
  while ((chr = getchar()) != EOF) {
    if ('0' <= chr && chr <= '9') {
      map[y][x] = chr - '0';
      x++;
      continue;
    }
    width = x;
    y++;
    x = 0;
  }
  int height = y;

  // Expand map
  for (y = 0; y < height * TILE_COUNT; y++) {
    for (x = 0; x < width * TILE_COUNT; x++) {
      map[y][x] = map[y % height][x % width] + x / width + y / height;
      map[y][x] -= 1;
      map[y][x] %= 9;
      map[y][x] += 1;
    }
  }

  risks[0][0] = 0;

  // Calculate risks
  do {
    continueMaybe = 0;
    for (y = 0; y < height * TILE_COUNT; y++) {
      for (x = 0; x < width * TILE_COUNT; x++) {
        risk = risks[y][x];
        cost = map[y][x];
        if (x) {
          risk = MIN(risk, risks[y][x - 1] + cost);
        }
        if (y) {
          risk = MIN(risk, risks[y - 1][x] + cost);
        }
        if (x < width - 1) {
          risk = MIN(risk, risks[y][x + 1] + cost);
        }
        if (y < height - 1) {
          risk = MIN(risk, risks[y + 1][x] + cost);
        }
        if (risks[y][x] != risk) {
          risks[y][x] = risk;
          continueMaybe = 1;
        }
      }
    }
  } while (continueMaybe);

  printf("Part One: %d\tPart Two: %d\n", risks[height - 1][width - 1],
         risks[height * 5 - 1][width * 5 - 1]);
  return 0;
}
