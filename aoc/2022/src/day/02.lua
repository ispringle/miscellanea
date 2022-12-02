local Day = require("src.day.Day")
require("src.utils.string")

local function parse(input)
    local p = {}
    for _, v in ipairs(input) do
        local x = string.split(v, " ")
        table.insert(p, x)
    end
    return p
end

local function part_one(input)
    local scores = {
        A = {
            X = 4,
            Y = 8,
            Z = 3,
        },
        B = {
            X = 1,
            Y = 5,
            Z = 9,
        },
        C = {
            X = 7,
            Y = 2,
            Z = 6,
        },
    }
    local score = 0
    for _, v in pairs(input) do
        local o, p = v[1], v[2]
        score = score + scores[o][p]
    end
    return score
end

local function part_two(input)
    local scores = {
        A = {
            X = 3,
            Y = 4,
            Z = 8,
        },
        B = {
            X = 1,
            Y = 5,
            Z = 9,
        },
        C = {
            X = 2,
            Y = 6,
            Z = 7,
        },
    }
    local score = 0
    for _, v in pairs(input) do
        local o, p = v[1], v[2]
        score = score + scores[o][p]
    end
    return score
end

local test_one, test_two = 15, 12
return Day:new(part_one, test_one, parse, part_two, test_two)
