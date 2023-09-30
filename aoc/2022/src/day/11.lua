local Day = require("src.day.Day")

local function parse(input)
	local monkeys, monkey, num = {}, {}, 0
	for _, v in pairs(input) do
		if string.match(v, "Monkey (%d+):") then
			num = string.match(v, "Monkey (%d+):")
			monkey = {}
		elseif string.match(v, "Starting items: (%d+)") then
			local items = string.match(v, "Starting items: (%d+, )?")
			print(v, items)
		end
	end
	return input
end

local function part_one(input)
	return 0
end

local function part_two(input)
	return 0
end

local test_one, test_two = 0, 0
return Day:new(part_one, test_one, parse, part_two, test_two)
