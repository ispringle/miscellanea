let SPF = 2;
let flashes = 0;
let flashesAtOneHundred = 0;
let flashesPerStep = 0;
let loopDone = false;
let grid = [];

const reset = () => {
  flashes = 0;
  flashesAtOneHundred = 0;
  flashesPerStep = 0;
  loopDone = false;
  grid = [];
}

const Cell = {
  level: 0,
  flashed: false,
}

const speed = increment => {
  const p = document.getElementById("spf");
  SPF = SPF + increment
  p.innerText = SPF;
}

const openFile = () => {
  const [file] = document.querySelector('input[type=file]').files;
  const reader = new FileReader()
  reader.addEventListener("load", () => {
    loop(reader.result);
  })
  if (file) {
    reader.readAsText(file);
  }
}

const killAllChildren = el => {
  while (el.lastChild) {
    el.removeChild(el.lastChild);
  }
}

const makeValidator = (l, w) => ([x, y]) => {
  return y >= 0 && x >= 0 && y < l && x < w
}

const neighbors = (x, y, validator) => {
  return [
    [x - 1, y - 1],
    [x, y - 1],
    [x + 1, y - 1],
    [x - 1, y],
    [x + 1, y],
    [x - 1, y + 1],
    [x, y + 1],
    [x + 1, y + 1],
  ].filter(validator);
}

const display = (step) => {
  const gridEl = document.getElementById("grid")
  killAllChildren(gridEl);
  grid.forEach(row => {
    let rowEl = document.createElement("div");
    rowEl.classList += "row";
    row.forEach(({ level }) => {
      let spanEl = document.createElement("span");
      spanEl.classList += "cell n" + level;
      spanEl.innerText = (level < 10) ? level : "_";
      rowEl.appendChild(spanEl);
    })
    gridEl.appendChild(rowEl);
  })
  const divEl = document.createElement("div")
  divEl.classList += "row";
  divEl.id += "final";
  const stepEl = document.createElement("p")
  stepEl.classList += "step";
  stepEl.innerText = step;
  const flashesEl = document.createElement("p");
  flashesEl.innerText = "Flashes: " + flashes;
  const flashesPerStepEl = document.createElement("p");
  flashesPerStepEl.innerText = "Flashes this step: " + flashesPerStep;
  divEl.appendChild(stepEl)
  divEl.appendChild(flashesEl)
  if (flashesAtOneHundred !== 0) {
    const partOneEl = document.createElement("p");
    partOneEl.innerText = "Part One:" + flashesAtOneHundred
    divEl.appendChild(partOneEl)
  }
  if (loopDone) {
    const partTwoEl = document.createElement("p");
    partTwoEl.innerText = "Part Two:" + step
    divEl.appendChild(partTwoEl)
  }
  gridEl.appendChild(divEl);
}

const step = () => {
  grid = grid.map(row => row.map(cell => { cell.flashed = false; return cell }))
  for (let y = 0; y < grid.length; y++) {
    for (let x = 0; x < grid[y].length; x++) {
      incCell(x, y, grid);
    }
  }
}

const incCell = (x, y) => {
  const validator = makeValidator(grid.length, grid[0].length);
  if (grid[y][x].level === 9) {
    flashes += 1;
    flashesPerStep += 1;
    grid[y][x].flashed = true;
    grid[y][x].level = 0;
    neighbors(x, y, validator).forEach(([nx, ny]) => {
      incCell(nx, ny);
    });
  } else {
    if (!grid[y][x].flashed) {
      grid[y][x].level += 1;
    }
  }
}
const sleep = seconds => new Promise(r => setTimeout(r, seconds * 1000));

async function loop(text) {
  reset();
  grid = text.trim().split("\n").map(
    row => Array.from((row)).map(c => {
      let cell = Object.create(Cell);
      cell.level = +c;
      return cell;
    }));

  let stepCount = 0;
  display(stepCount);
  await sleep(SPF);
  while (flashesPerStep < grid.length * grid[0].length) {
    flashesPerStep = 0;
    stepCount += 1;
    step();
    if (stepCount === 100) {
      flashesAtOneHundred = flashes;
    }
    display(stepCount);
    await sleep(SPF);
  }
  loopDone = true;
  display(stepCount);
}
