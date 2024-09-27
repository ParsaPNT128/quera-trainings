def calc(s):
    s = [x for x in s if x != 4]
    space = 0
    for m, i in enumerate(s):
        for n, j in enumerate(s):
            if m != n and i + j == 4:
                s.remove(i)
                s.remove(j)
            elif m != n and i + j < 4:
                for o, k in enumerate(s):
                    if o != m and o != n and i + j + k == 4:
                        s.remove(i)
                        s.remove(j)
                        s.remove(k)
                    elif o != m and o != n and i + j + k < 4:
                        for p, l in enumerate(s):
                            if p != m and p != n and p != o and i + j + k + l == 4:
                                s.remove(i)
                                s.remove(j)
                                s.remove(k)
                                s.remove(l)

    s.sort(reverse=True)
    ns = list(s)
    while True:
        if len(s) != 0:
            if sum(ns) > 4:
                ns.remove(ns[len(ns)-1])
            else:
                all = sum(ns)
                for i in ns:
                    s.remove(i)
                ns = list(s)
                if len(ns) != 0:
                    space += 4 - all

        else:
            return space


answers = []
t = int(input())
for i in range(t):
    n = int(input())
    s = input().split()

    for j in range(n):
        s[j] = int(s[j])

    answers.append(calc(s))

for i in answers:
    print(i)