def func(s):
    global alph_b, alph_a, first
    if first:
        alph_a = dict(alph)
        for i in s:
            alph_a[i] += 1
        first = False
    else:
        alph_b = dict(alph)
        for i in s:
            alph_b[i] += 1
        
        for k in alph_a.keys():
            if alph_a[k] < alph_b[k]:
                alph_a[k] = alph_b[k]

first = True
alph = {
    "a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0, "i": 0, "j": 0, "k": 0, "l": 0, "m": 0, "n": 0, "o": 0,
    "p": 0, "q": 0, "r": 0, "s": 0, "t": 0, "u": 0, "v": 0, "w": 0, "x": 0, "y": 0, "z": 0
}

answers = []
t = int(input())
for i in range(t):
    n = int(input())
    for i in range(n):
        func(input())
    answers.append(sum(alph_a.values()))
    first = True

for i in answers:
    print(i)