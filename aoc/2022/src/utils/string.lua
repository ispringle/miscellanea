local M = {}
-- New/Modified String Methods

function string.append(str, x)
    return str .. x
end

-- Remove amt from beginning of string
function string.yoink(str, amt)
    local popped = str:sub(1, amt)
    local new = str:sub(amt + 1, #str)
    return { popped, new }
end

function string.prepend(str, x)
    return x .. str
end

function string.split(str, sep)
    sep = sep or "%s"
    local t = {}
    for s in string.gmatch(str, "([^" .. sep .. "]+)") do
        table.insert(t, s)
    end
    return t
end

-- String Related Helper Functions

return M