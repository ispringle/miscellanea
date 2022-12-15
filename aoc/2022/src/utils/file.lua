local m = {}

-- New/Modified String Methods

-- String Related Helper Functions
function m.file_exists(filename)
    local f = io.open(filename, "rb")
    if f then f:close() end
    return f~= nil
end

function m.lines_from_file(filename)
    if not m.file_exists(filename) then return nil end
    local lines = {}
    for line in io.lines(filename) do
        lines[#lines+1] = line
    end
    return lines
end

return m