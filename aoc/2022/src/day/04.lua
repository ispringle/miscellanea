local Day = require("src.day.Day")

local range = require("src.utils.range")
require("src.utils.string")
require("src.utils.table")

local function parse(input)
    local parsed = {}
    for _, v in pairs(input) do
        local pairing = string.split(v, ',')
        pairing[1] = string.split(pairing[1], '-')
        pairing[2] = string.split(pairing[2], '-')
        table.insert(parsed, table.map(table.smoosh(pairing[1], pairing[2]), tonumber))
    end
    return parsed
end

local function part_one(input)
    local tally = 0
    for _, v in pairs(input) do
        local x1, x2, y1, y2 = v[1], v[2], v[3], v[4]
        if range.within(x1, x2, y1, y2) then
            tally = tally + 1
        end
    end
    return tally
end

local function part_two(input)
    local tally = 0
    for _, v in pairs(input) do
        local x1, x2, y1, y2 = v[1], v[2], v[3], v[4]
        if range.overlap(x1, x2, y1, y2) then
            tally = tally + 1
        end
    end
    return tally
end

local test_one, test_two = 2, 4
return Day:new(part_one, test_one, parse, part_two, test_two)
