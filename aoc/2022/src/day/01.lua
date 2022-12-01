local Day = require("src.day.Day")

local function sum_by_elf(input)
    local elves = { 0 }
    for _, v in pairs(input) do
        if v == "" then
            table.insert(elves, 0)
        else
            elves[#elves] = elves[#elves] + tonumber(v)
        end
    end
    table.sort(elves)
    return elves
end

local function part_one(elves)
    return elves[#elves]
end

local function part_two(elves)
    return elves[#elves] + elves[#elves - 1] + elves[#elves - 2]
end

return Day:new(part_one, 24000, sum_by_elf, part_two, 45000)
