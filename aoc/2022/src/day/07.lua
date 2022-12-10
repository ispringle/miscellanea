local Day = require("src.day.Day")

require('src.utils.string')
local table_utils = require('src.utils.table')

local function show_tree(tree)
    for k, v in pairs(tree) do
        if type(v) == "table" then
            print(k .. ":")
            show_tree(v)
        else print(" - " .. k .. ": " .. v)
        end
    end
end

local function parse(input)
    local dirs, stack = {}, {}
    for _, v in pairs(input) do
        if v == "$ cd .." then
            table.remove(stack, #stack)
        elseif string.match(v, "^$ cd (%g+)") then
            table.insert(stack, string.match(v, "^$ cd (%g+)"))
        elseif string.match(v, "^%d") then
            local pwd = ""
            for _, dir in pairs(stack) do
                if dir == "/" then
                    pwd = dir
                else
                    pwd = pwd .. "/" .. dir
                end
                dirs[pwd] = (dirs[pwd] or 0) + tonumber(string.match(v, "^(%d+)"))
            end
        end
    end
    return dirs
end

local function part_one(input)
    local tally = 0
    for _, v in pairs(input) do
        if v <= 100000 then
            tally = tally + v
        end
    end
    return tally
end

local function part_two(input)
    local space_needed = 30000000 - (70000000 - input["/"])
    local min = math.maxinteger
    for _, v in pairs(input) do
        if v >= space_needed then
            min = math.min(min, v)
        end
    end
    return min
end

local test_one, test_two = 95437, 24933642
return Day:new(part_one, test_one, parse, part_two, test_two)
