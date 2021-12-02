i, s, j, k = '825401', '37', 0, 1
while i not in s[-7:]:
	s += str(int(s[j]) + int(s[k]))
	j, k = [(x + int(s[x]) + 1) % len(s) for x in [j, k]]
print(f"Part One: {s[int(i):int(i)+10]}\nPart Two: {s.index(i)}")
