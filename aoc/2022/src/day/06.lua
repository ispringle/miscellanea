local Day = require("src.day.Day")

local string_utils = require("src.utils.string")
require("src.utils.table")

local function parse(input)
    -- Parse the input
    return input[1]
end

local function find_uniq_substring_of_size(str, size)
    -- Returns the index of the uniq substring's first character
    local step = size - 1
    for i = 1, #str - step do
        local packet = str:sub(i, i + step)
        local counter = string_utils.counter(packet)
        if table.len(counter) == size then
            return i + step
        end
    end
    return nil
end

local function part_one(input)
    return find_uniq_substring_of_size(input, 4)
end

local function part_two(input)
    return find_uniq_substring_of_size(input, 14)
end

local test_one, test_two = 7, 19
return Day:new(part_one, test_one, parse, part_two, test_two)
