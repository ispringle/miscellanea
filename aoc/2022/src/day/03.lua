local Day = require("src.day.Day")
require("src.utils.table")

local function get_priority(c)
    if string.match(c, "%u") then
        -- Char is upper case
        return string.byte(c) - string.byte("&")
    else
        -- Char is lower case
        return string.byte(c) - string.byte("`")
    end
end

local function intersection(a, b)
    local common = {}
    for _, x in pairs(a) do
        for _, y in pairs(b) do
            if x == y then
                table.insert(common, x)
                break
            end
        end
    end
    return common
end

local function get_common(t)
    local common = nil
    for _, v in pairs(t) do
        if not common then
            common = intersection(v, v)
        else
            common = intersection(common, v)
        end
    end
    return common
end

local function parse(input)
    local bags = {}
    for _, v in pairs(input) do
        local p1, p2 = {}, {}
        for i = 1, #v do
            if i - 1 < #v / 2 then
                table.insert(p1, v:sub(i, i))
            else
                table.insert(p2, v:sub(i, i))
            end
        end
        table.insert(bags, { p1, p2 })
    end
    return bags
end

local function part_one(bags)
    local tally = 0
    for _, bag in pairs(bags) do
        local common = get_common(bag)
        tally = tally + get_priority(common[1])
    end
    return tally
end

local function part_two(input)
    local tally = 0
    for i = 1, #input, 3 do
        local elf_a = table.smoosh(input[i][1], input[i][2])
        local elf_b = table.smoosh(input[i+1][1], input[i+1][2])
        local elf_c = table.smoosh(input[i+2][1], input[i+2][2])
        local common = get_common({elf_a, elf_b, elf_c})
        tally = tally + get_priority(common[1])
    end
    return tally
end

local test_one, test_two = 157, 70
return Day:new(part_one, test_one, parse, part_two, test_two)
