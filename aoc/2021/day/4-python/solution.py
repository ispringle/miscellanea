ns, s, w, ba = (i := [*open('input.txt')])[0], [], [], [int(x) for y in [
    x.split() for x in i[2:] if x != '\n'] for x in y]
for n in [int(x) for x in ns.split(',')]:
    ba = [0 if x == n else x for x in ba]
    for i, b in enumerate(
        (g:=lambda x: [x[n:n+5] for n in range(0, len(x), 5)])(g(ba))):
        if i in s:
            pass
        elif 1 in [len(set(x)) for x in b] or 1 in [
                len(set(x)) for x in list(map(list, zip(*b)))]:
            w.append((sum(ba[(j := i*25):j+25])*n))
            s.append(i)
print(w[0], w[-1])
