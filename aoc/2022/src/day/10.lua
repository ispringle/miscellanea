local Day = require("src.day.Day")

require("src.utils.string")
require("src.utils.table")

CYCLE_TIMES = { noop = 1, addx = 2 }

local function parse(input)
	local cycles = { 1 }
	for _, v in pairs(input) do
		local line = string.split(v, " ")
		local ins, val = line[1], tonumber(line[2] and line[2] or 0)
		for i = 1, CYCLE_TIMES[ins] do
			if i == CYCLE_TIMES[ins] then
				table.insert(cycles, cycles[#cycles] + val)
			else
				table.insert(cycles, cycles[#cycles])
			end
		end
	end
	return cycles
end

local function part_one(cycles)
	local signals = 0
	for i = 20, 220, 40 do
		signals = signals + (cycles[i] * i)
	end
	return signals
end

local function part_two(cycles)
	local crt, pixel = { {} }, 0
	for _, sprite in pairs(cycles) do
		if sprite - 1 <= pixel and sprite + 1 >= pixel then
			table.insert(crt[#crt], "#")
		else
			table.insert(crt[#crt], ".")
		end
		pixel = pixel + 1
		if pixel == 40 then
			pixel = 0
			table.insert(crt, {})
		end
	end
	for _, l in pairs(crt) do
		local s = ""
		for _, p in pairs(l) do
			s = s .. p
		end
		print(s)
	end
	return 0
end

local test_one, test_two = 13140, 0
return Day:new(part_one, test_one, parse, part_two, test_two)
