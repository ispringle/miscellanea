# Answer: 171

import calendar as c

y_start = 1901
y_end = 2000
sundays = 0

for year in range(y_start, y_end + 1):
    for month in range(1, 13):
        if c.monthcalendar(year, month)[0][6] == 1:
            sundays += 1
print(sundays)
