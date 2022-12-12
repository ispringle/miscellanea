local Day = require("src.day.Day")

local function parse(input)
    local grid = {}
    for n, v in pairs(input) do
        grid[n] = {}
        for i = 1, #v do
            grid[n][i] = tonumber(v:sub(i, i))
        end
    end
    return grid
end

local function part_one(trees)
    local tally = 0
    for y, row in pairs(trees) do
        for x, tree in pairs(row) do
                local visible_from = 4
                for ly = y - 1, 1, -1 do
                    if trees[ly][x] >= tree then
                        visible_from = visible_from - 1
                        break
                    end
                end
                for ly = y + 1, #trees do
                    if trees[ly][x] >= tree then
                        visible_from = visible_from - 1
                        break
                    end
                end
                for lx = x - 1, 1, -1 do
                    if trees[y][lx] >= tree then
                        visible_from = visible_from - 1
                        break
                    end
                end
                for lx = x + 1, #row do
                    if trees[y][lx] >= tree then
                        visible_from = visible_from - 1
                        break
                    end
                end
                tally = tally + (visible_from > 0 and 1 or 0)
        end
    end
    return tally
end

local function part_two(trees)
    local max_scenic = 0
    for y, row in pairs(trees) do
        for x, tree in pairs(row) do
                local north, south, east, west = 0, 0, 0, 0
                for ly = y - 1, 1, -1 do
                    north = north + 1
                    if trees[ly][x] >= tree then break end
                end
                for ly = y + 1, #trees do
                    south = south + 1
                    if trees[ly][x] >= tree then break end
                end
                for lx = x - 1, 1, -1 do
                    east = east + 1
                    if trees[y][lx] >= tree then break end end
                for lx = x + 1, #row do
                    west = west + 1
                    if trees[y][lx] >= tree then break end end
                max_scenic = math.max(max_scenic, north * south * east * west)
        end
    end
    return max_scenic
end

local test_one, test_two = 21, 8
return Day:new(part_one, test_one, parse, part_two, test_two)
