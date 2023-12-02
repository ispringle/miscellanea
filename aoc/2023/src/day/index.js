import {
  puzzleInput as dayOnePuzzleInput,
  solver as dayOneSolver,
  testInputs as dayOneTestInputs,
} from './one';

import {
  solver as dayTwoSolver,
  testInputs as dayTwoTestInputs,
  puzzleInput as dayTwoPuzzleInput,
} from './two';

export default {
  one: {
    puzzleInput: dayOnePuzzleInput,
    solve: dayOneSolver,
    testInputs: dayOneTestInputs,
  },
  two: {
    testInputs: dayTwoTestInputs,
    puzzleInput: dayTwoPuzzleInput,
    solve: dayTwoSolver,
  },
};
