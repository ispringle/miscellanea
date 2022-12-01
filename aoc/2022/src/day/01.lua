local M = {}

local function sum_by_elf(input)
    local elves = {0}
    for _, v in pairs(input) do
        if v == "" then
            table.insert(elves, 0)
        else
            elves[#elves] = elves[#elves] + tonumber(v)
        end
    end
    -- This is to add the last elf to the table
    table.sort(elves)
    return elves
end

local function part_one(elves)
    return elves[#elves]
end

local function part_two(elves)
    return elves[#elves] + elves[#elves - 1] + elves[#elves - 2]
end

M.init = function(input, test_input)
    M.test_input = sum_by_elf(test_input)
    M.input = sum_by_elf(input)
end

M.run = function()
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

M.part_one = function() return part_one(M.input) end
M.part_two = function() return part_two(M.input) end

return M
