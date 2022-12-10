local M = {}

-- New/Modified String Methods

function table.copy(t)
    local new = {}
    for k, v in pairs(t) do
        new[k] = v
    end
    return setmetatable(new, getmetatable(t))
end

function table.len(t)
    local tally = 0
    for _, _ in pairs(t) do
        tally = tally + 1
    end
    return tally
end

function table.map(t, f)
    local new = t
    for i, v in ipairs(new) do
        new[i] = f(v)
    end
    return new
end

function table.newwith(kind, count)
    local new = {}
    for i = 1, count do
        new[i] = kind
    end
    return new
end

function table.smoosh(a,b)
    local new = a
    for _, v in pairs(b) do
        table.insert(new, v)
    end
    return new
end

-- String Related Helper Functions

M.print_table = function (t)
    for k, v in pairs(tree) do
        if type(v) == "table" then
            print(k .. ":")
            show_tree(v)
        else print(" - " .. k .. ": " .. v)
        end
    end
end

M.remove_lowest_maybe = function (most, value)
    local m = most
    table.insert(m, value)
    table.sort(m, function (a, b) return a > b end)
    m[4] = nil
    return m
end

M.table_sum = function (t)
    local acc = 0
    for _, v in pairs(t) do
        acc = acc + v
    end
    return acc
end

return M