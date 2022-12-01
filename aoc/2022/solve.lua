local args = {...}
local day = args[1]
if string.len(day) < 2 then 
    day = "0" .. day
end

local file_utils = require('src.utils.file')

local solver = require("src.day." .. day)

-- local input = file_utils.lines_from_file("input/" .. day .. ".test.txt")
local input = file_utils.lines_from_file("input/" .. day .. ".txt")

solver.init(input)
local p1 = solver.part_one()
local p2 = solver.part_two()
print("Day One: " .. p1)
print("Day Two: " .. p2)