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


M.init = function (input)
 M.elves = split_by_elf(input)
end

M.part_one = function () return part_one(M.elves) end
M.part_two = function () return part_two(M.elves) end

return M