local M = {}

M.print_table = function (t)
    for _, v in pairs(t) do
        print(v)
    end
    print("")
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