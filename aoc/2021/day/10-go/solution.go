package main

import (
	"bufio"
	"os"
	"sort"
)

var bracketMap = map[rune]rune{
	')': '(',
	']': '[',
	'}': '{',
	'>': '<',
}

var syntaxTallyMap = map[rune]int{
	')': 3,
	']': 57,
	'}': 1197,
	'>': 25137,
}

var completionTallyMap = map[rune]int{
	'(': 1,
	'[': 2,
	'{': 3,
	'<': 4,
}

func main() {
	file, err := os.Open("input.txt")
	if err != nil {
		panic(err)
	}
	scanner := bufio.NewScanner(file)
	var syntaxTally int
	var completionScores []int

loop:
	for scanner.Scan() {
		line := scanner.Text()
		var stack []rune
		for _, char := range line {
			switch char {
			case '(', '{', '[', '<':
				stack = append(stack, char)
			default:
				previous := stack[len(stack)-1]
				corrupted := previous != bracketMap[char]
				if corrupted {
					syntaxTally = syntaxTally + syntaxTallyMap[char]
					continue loop
				} else {
					stack = stack[:len(stack)-1]
				}
			}
		}
		var tally = 0
		for i := len(stack) - 1; i >= 0; i-- {
			tally = tally * 5
			tally = tally + completionTallyMap[stack[i]]
		}
		completionScores = append(completionScores, tally)
	}
	println("Part One:", syntaxTally)
	sort.Ints(completionScores)
	println("Part Two:", completionScores[len(completionScores)/2])
}
