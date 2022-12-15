local Day = {}

function Day:new(func_one, expect_one, parser, func_two, expect_two, parse_two, day)
    day = day or {}
    setmetatable(day, self)
    self.__index = self

    self.solver_one = func_one
    self.expect_one = expect_one

    self.parse = parser

    -- These are optional since we won't know anything about part two until one
    -- has been completed.
    self.solver_two = func_two or function() end
    self.expect_two = expect_two or nil

    return day
end

function Day:run(input, test_input, test_input2)
    self.test_input = self.parse(test_input)
    self.input = self.parse(input)
    local results = {}

    if self.solver_one(self.test_input) == self.expect_one then
        results[1] = self.solver_one(self.input)
    else
        results[1] = "Test failed!"
    end

    if test_input2 ~= nil then
        self.test_input = self.parse(test_input2)
    end

    if self.solver_two(self.test_input) == self.expect_two then
        results[2] = self.solver_two(self.input)
    else
        results[2] = "Test failed!"
    end

    return results
end

return Day
