local M = {}

local table_utils = require('src.utils.table')

local function split_by_elf(input)
    local elves, elf = {}, {}
    for _, v in pairs(input) do
        if v == "" then
            table.insert(elves, elf)
            elf = {}
        else
            table.insert(elf, tonumber(v))
        end
    end
    -- This is to add the last elf to the table
    table.insert(elves, elf)
    return elves
end

local function part_one(elves)
    local most, curr = 0, 0
    for _, elf in pairs(elves) do
        for _, cal in pairs(elf) do
            curr = cal + curr
        end
        if curr > most then
            most = curr
        end
        curr = 0
    end
    return most
end

local function part_two(elves)
    local most, curr = {0,0,0}, 0
    for _, elf in pairs(elves) do
        for _, cal in pairs(elf) do
            curr = cal + curr
        end
        local most = table_utils.remove_lowest_maybe(most, curr)
        curr = 0
    end
    return table_utils.table_sum(most)
end


M.init = function (input, test_input)
 M.test_input = split_by_elf(test_input)
 M.input = split_by_elf(input)
end

M.run = function () 
    local expect_one, expect_two = 24000, 45000
    local results = {}

    if part_one(M.test_input) == expect_one then
        results[1] = part_one(M.input)
    else
        results[1] = "Test failed!"
    end

    if part_two(M.test_input) == expect_two then
        results[2] = part_two(M.input)
    else
        results[2] = "Test failed!"
    end

    return results
end

M.part_one = function () return part_one(M.input) end
M.part_two = function () return part_two(M.input) end

return M