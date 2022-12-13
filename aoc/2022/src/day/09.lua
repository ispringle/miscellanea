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

local function update(move, data)
  for _ = 1, move.count do
    if move.dir == "U" then
      data.head.x = data.head.x + 1
    elseif move.dir == "D" then
      data.head.x = data.head.x - 1
    elseif move.dir == "L" then
      data.head.y = data.head.y + 1
    elseif move.dir == "R" then
      data.head.y = data.head.y - 1
    end
  end
  return data
end

local function updatet(t, h)
  local diffx = h.x - t.x
  local diffy = h.y - t.y
  if math.abs(diffx) > 1 then
    t.x = t.x + (diffx - 1)
    math.abs
  end
end

local function part_one(moves)
  local data = { head = {x = 0, y = 0}, tail = {x = 0, y = 0}, visited = {['0,0'] = 1}}
  for _, move in pairs(moves) do
    data = update(move, data)
  end
  return table.sum(data.visited)
end

local function part_two(input)
    return 0
end

local test_one, test_two = 13, 0
return Day:new(part_one, test_one, parse, part_two, test_two)
