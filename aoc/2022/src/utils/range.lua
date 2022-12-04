local M = {}

function M.overlap(x1, x2, y1, y2)
    if x1 <= y2 and x2 >= y1 then
        return true
    end
    return false
end

function M.within(x1, x2, y1, y2)
    if (x1 <= y1 and x2 >= y2) or (y1 <= x1 and y2 >= x2) then
        return true
    end
    return false
end

return M