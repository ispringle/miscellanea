import std/strutils
import std/tables

var network: Table[string, seq[string]]
let input = readFile("input.txt").strip.split("\n")

for line in input:
  let parts = line.split("-")
  let a = parts[0]
  let b = parts[1]
  network.mgetOrPut(a, @[]).add b
  network.mgetOrPut(b, @[]).add a

proc travel(cave: string, visited: seq[string], smallTwice: int): int =
  var sub = 0 
  if cave == "end":
    return 1
  if cave in visited:
    if cave == "start":
      return 0
    if cave[0].isLowerAscii:
      if smallTwice < 1:
        return 0
      else:
       sub = 1 
  var acc = 0
  for nextCave in network[cave]:
    acc += travel(nextCave, visited & cave, smallTwice - sub)
  return acc

echo travel("start", @[], 0)
echo travel("start", @[], 1)
