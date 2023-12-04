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

import {
  solver as dayThreeSolver,
  testInputs as dayThreeTestInputs,
  puzzleInput as dayThreePuzzleInput,
} from './three';

import {
  solver as dayFourSolver,
  testInputs as dayFourTestInputs,
  puzzleInput as dayFourPuzzleInput,
} from './four';

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
  three: {
    testInputs: dayThreeTestInputs,
    puzzleInput: dayThreePuzzleInput,
    solve: dayThreeSolver,
  },
  four: {
    testInputs: dayFourTestInputs,
    puzzleInput: dayFourPuzzleInput,
    solve: dayFourSolver,
  },
};
