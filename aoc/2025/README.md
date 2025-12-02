# Advent of Code 2025

Common Lisp solutions for Advent of Code 2025.

## Running Solutions

### With SBCL installed locally

```bash
./run.lisp <day>
# or
sbcl --script run.lisp <day>

# Examples:
./run.lisp 1   # Run day 1
./run.lisp 2   # Run day 2
```

### With Docker

Build:

```bash
docker build -t aoc2025 .
```

Run any day:

```bash
docker run --rm aoc2025 1   # Run day 1
docker run --rm aoc2025 2   # Run day 2
```

### With Docker Compose

```bash
docker compose run --rm aoc 1   # Run day 1
docker compose run --rm aoc 2   # Run day 2
```

## Structure

```
2025/
├── run.lisp        # Runner script (Lisp)
├── utils.lisp      # Shared utilities
├── Dockerfile      # Docker container with SBCL
├── day1/
│   ├── day1.lisp   # Solution
│   ├── day1.txt    # Puzzle input
│   └── day1-test.txt
├── day2/
│   └── ...
└── ...
```

