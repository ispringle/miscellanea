local Day = require("src.day.Day")

require('src.utils.string')
require('src.utils.table')

local function parse(input)
  local directions = {}
  for i, v in ipairs(input) do
    local d = string.split(v, " ")
    directions[i] = { dir = d[1], count = tonumber(d[2])}
  end
  return directions
end

local function sign(n)
  if n == 0 then return 0
  elseif n > 0 then return 1
  elseif n < 0 then return -1 end
end

local function adjacent(a, b)
  return math.abs(a.x - b.x) <= 1 and math.abs(a.y - b.y) <= 1
end

local function update(knots, move, visited)
  local tally = 1
  for _ = 1, move.count do
    if move.dir == "U" then
      knots[1].y = knots[1].y + 1
    elseif move.dir == "D" then
      knots[1].y = knots[1].y - 1
    elseif move.dir == "L" then
      knots[1].x = knots[1].x - 1
    elseif move.dir == "R" then
      knots[1].x = knots[1].x + 1
    end
    for i = 1, #knots - 1 do
      if not adjacent(knots[i], knots[i + 1]) then
        local diffx, diffy = sign(knots[i].x - knots[i + 1].x), sign(knots[i].y - knots[i + 1].y)
        knots[i + 1].x, knots[i + 1].y = knots[i + 1].x + diffx, knots[i + 1].y + diffy
        if i == #knots - 1 then
          tally = tally + 1
          visited[knots[i + 1].x .. "," .. knots[i + 1].y ] = 1
        end
      end
    end
  end
  return { knots = knots, visited = visited }
end

local function part_one(moves)
  local head, tail, visited = {x = 0, y = 0}, {x = 0, y = 0}, {['0,0'] = 1}
  for _, move in pairs(moves) do
    local new = update({head, tail}, move, visited)
    head, tail, visited = new.knots[1], new.knots[2], new.visited
  end
  return table.sum(visited)
end

local function part_two(moves)
  local knots, visited = {}, {['0,0'] = 1}
  for _ = 1, 10 do
    table.insert(knots, {x = 0, y = 0})
  end
  for _, move in pairs(moves) do
    local new = update( knots, move, visited)
    knots, visited = new.knots, new.visited
  end
  print(table.sum(visited))
  return table.sum(visited)
end

local test_one, test_two = 13, 36
return Day:new(part_one, test_one, parse, part_two, test_two)
