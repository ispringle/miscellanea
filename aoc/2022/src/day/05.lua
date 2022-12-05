local Day = require("src.day.Day")

require("src.utils.string")
require("src.utils.table")

local function parse(input)
    local stacks = (#input[1] // 4) + 1
    -- local crates, instructions = table.newwith({}, stacks), {}
    local crates, instructions = table.newwith("", stacks), {}
    local cargo_section = true
    for _, v in pairs(input) do
        if v:sub(2, 2) == '1' or v == "" then
            -- Either the cargo column count or blank line
            cargo_section = false
        else
            if cargo_section then
                -- Cargo stack arrangement
                local column = 1
                for i = 2, stacks * 4, 4 do
                    -- table.insert(crates[column], v:sub(i, i))
                    crates[column] = string.gsub(
                        string.append(crates[column], v:sub(i, i)),
                        "%s+",
                        "")
                    column = column + 1
                end
            else
                -- Instructions
                local count, ints = 1, {}
                for v in string.gmatch(v, "%d+") do
                    table.insert(ints, tonumber(v))
                end
                table.insert(instructions, ints)
            end
        end
    end
    return { crates = crates, instructions = instructions }
end

local function part_one(input)
    local crates, instructions = table.copy(input["crates"]),
        table.copy(input["instructions"])
    for _, next in pairs(instructions) do
        local count, from, to = next[1], next[2], next[3]
        for _ = 1, count do
            local yoinked = string.yoink(crates[from], 1)
            local to_move = yoinked[1]
            crates[from] = yoinked[2]
            crates[to] = string.prepend(crates[to], to_move)
        end
    end
    local result = ""
    for _, v in pairs(crates) do
        result = string.append(result, v:sub(1, 1))
    end
    return result
end

local function part_two(input)
    local crates, instructions = input["crates"], input["instructions"]
    for _, next in pairs(instructions) do
        local count, from, to = next[1], next[2], next[3]
        local yoinked = string.yoink(crates[from], count)
        local to_move = yoinked[1]
        crates[from] = yoinked[2]
        crates[to] = string.prepend(crates[to], to_move)
    end
    local result = ""
    for _, v in pairs(crates) do
        result = string.append(result, v:sub(1, 1))
    end
    return result
end

local test_one, test_two = 'CMZ', 'MCD'
return Day:new(part_one, test_one, parse, part_two, test_two)
