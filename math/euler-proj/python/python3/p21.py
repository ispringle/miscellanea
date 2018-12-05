def d(n):
	divs = []
	for i in range(1,n):
		if n % i == 0:
			divs.append(i)
	return divs

sums = {}
for n in range(1,10001):
	sums[n] = sum(d(n))
pairs = []
for k, v in sums.items():
	for i in sums.keys():
		if v == i and sums[i] == k and k != v:
			pairs.append(k)
print(sum(pairs))
