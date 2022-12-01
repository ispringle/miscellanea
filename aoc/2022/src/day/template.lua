local M = {}

-- local table_utils = require('src.utils.table')

local function part_one(input)
    return nil
end

local function part_two(input)
    return nil
end


M.init = function (input, test_input)
 M.test_input = split_by_elf(test_input)
 M.input = input
 -- Do any general input parsing here:
end

M.run = function () 
    local expect_one, expect_two = nil, nil
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